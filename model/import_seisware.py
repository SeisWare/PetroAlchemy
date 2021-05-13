import SeisWare
import sys
import pandas as pd
import numpy as np
from PySide2.QtWidgets import QInputDialog


def handle_error(message, error):
    """
    Helper function to print out the error message to stderr and exit the program.
    """
    print(message, file=sys.stderr)
    print("Error: %s" % (error), file=sys.stderr)
    sys.exit(1)


def SWconnect(project_name):
    connection = SeisWare.Connection()
    
    try:
        serverInfo = SeisWare.Connection.CreateServer()
        connection.Connect(serverInfo.Endpoint(), 5000)
    except RuntimeError as err:
        handle_error("Failed to connect to the server", err)

    project_list = SeisWare.ProjectList()

    try:
        connection.ProjectManager().GetAll(project_list)
    except RuntimeError as err:
        handle_error("Failed to get the project list from the server", err)

    projects = [project for project in project_list if project.Name() == project_name]
    if not projects:
        print("No project was found", file=sys.stderr)
        sys.exit(1)
        
    login_instance = SeisWare.LoginInstance()
    try:
        login_instance.Open(connection, projects[0])
    except RuntimeError as err:
        handle_error("Failed to connect to the project", err)
        
    return login_instance

def SWprojlist():
    connection = SeisWare.Connection()
    
    try:
        serverInfo = SeisWare.Connection.CreateServer()
        connection.Connect(serverInfo.Endpoint(), 5000)
    except RuntimeError as err:
        handle_error("Failed to connect to the server", err)

    project_list = SeisWare.ProjectList()
    
    connection.ProjectManager().GetAll(project_list)
    
    return project_list


def get_prod_from_proj(project_name):

    # Fix date time in dataframe

    get_prod_from_proj.login_instance = SWconnect(project_name)

    # Create a production list
    production_list = SeisWare.ProductionList()

    # Add all the production to the list
    get_prod_from_proj.login_instance.ProductionManager().GetAll(production_list)

    volumesDF = pd.DataFrame(columns=["UWI","Date","Oil","Gas"])
    dflist = []


    for i in production_list:
    #Print all the entities in the list

        # Populate the wells with production volumes
        get_prod_from_proj.login_instance.ProductionManager().PopulateWells(i)
        
        get_prod_from_proj.login_instance.ProductionManager().PopulateVolumes(i)

        # Create a bunch of empty lists and sets
        prod_well_list = SeisWare.ProductionWellList()
        prod_ID_list = SeisWare.IDSet()
        failed_IDs = SeisWare.IDSet()
        prod_volumes = SeisWare.ProductionVolumeList()

        i.Volumes(prod_volumes)
        i.Wells(prod_well_list)
        
        for i in prod_well_list:
            prod_ID_list.append(i.WellID())

        well_list = SeisWare.WellList()

        get_prod_from_proj.login_instance.WellManager().GetByKeys(prod_ID_list,well_list,failed_IDs)

        wellname = well_list[0].UWI()

        print(wellname)
        if len(prod_volumes) > 0:
            volumesDF=pd.DataFrame([(
            f"{i.VolumeDate().year}"+'-'+f"{i.VolumeDate().month}"+'-'+f"{i.VolumeDate().day}",
            i.OilVolume(),i.OilVolumeUnits(),
            i.GasVolume(),i.GasVolumeUnits(),
            wellname
            ) 
            for i in prod_volumes],
            columns=["Date","Oil","Oil Units","Gas","Gas Units","Well Name"])
        
        dflist.append(volumesDF) 
        

    volumes = pd.concat(dflist)

    volumes["Date"] = pd.to_datetime(volumes["Date"])
    
    cols = ["Oil","Gas"]

    volumes = volumes[volumes["Gas Units"] == 4]
    volumes = volumes[volumes["Oil Units"] == 8]

    #volumes["Oil"] = volumes["Oil"].replace({0:np.nan})
    #volumes["Gas"] = volumes["Gas"].replace({0:np.nan})
    
    volumes.drop(columns = ["Gas Units","Oil Units"])

    volumes.drop_duplicates(inplace = True)
    #volumes.to_csv("test.csv")

    return volumes.sort_values(by=['Well Name', 'Date']).dropna()

def import_seisware_data(self):

    projects = SWprojlist()

    item, ok = QInputDialog.getItem(self, "Select SeisWare Project", "List of SeisWare Projects", projects,0,False)
    
    if ok and item:
         self.model.add(item)