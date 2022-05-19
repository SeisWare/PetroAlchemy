import SeisWare
import pandas as pd
import numpy as np


def check_for_zone(login_instance,zone_name):

    """
    Input : Project login instance and zone name (string)

    Check to make see if the zone exists. If not, create it.

    Return : The zone object
    """



    pass


def check_for_zone_attribute(login_instance,zone_attribute_name):

    """
    Input : Project login instance and zone attribute name (string)

    Check to make see if the zone exists. If not, create it.

    If it does, return it.

    Return : The zone attribute object
    """
    zone_attribute_list = SeisWare.ZoneAttributeList()


    login_instance.ZoneAttributeManager().GetAll(zone_attribute_list)

    for i in zone_attribute_list:
        print(i.Name())

    zone_attribute = [i for i in zone_attribute_list if i.Name() == zone_attribute_name]


    return None

def export_EUR(login_instance,well_UWI,eur_dict):


    """
    Input 
    Login instance
    Well name : string
    EUR time : string
    Eur value : integer

    After EUR values are calculated in plot_decline_curve.py, send EUR values
    as a Well Zone Attribute back to SeisWare.
    """

     # Check to make sure login_instance has been created before pushing data

    if login_instance != None:
       
        # Create full well zone
        well_list = SeisWare.WellList()

        login_instance.WellManager().GetAll(well_list)

        well = [i for i in well_list if i.UWI() == well_UWI]


        # Create zone and name it EUR
        zone = SeisWare.Zone()
        zone.Name("EUR")


        well_zone = SeisWare.WellZone()


        #Create well zone
        well_zone.WellID(well[0].ID())
        well_zone.Zone(zone)
        well_zone.TopMD(SeisWare.Measurement(0,SeisWare.Unit.Meter))
        well_zone.BaseMD(well[0].TotalDepth())

        # Get the Zone Type list
        zone_type_list = SeisWare.ZoneTypeList()

        login_instance.ZoneTypeManager().GetAll(zone_type_list)

        zone_type_generic = [i.ID() for i in zone_type_list if i.Name() == "Generic"]

        well_zone.ZoneTypeID(zone_type_generic[0])

        # Create empty attribute list
        attribute_list = SeisWare.ZoneAttributeList()

        wz_attribute_list = SeisWare.WellZoneAttributeList()

        # Get the attribute list to check for existing attribute names
        login_instance.ZoneAttributeManager().GetAll(attribute_list)

        for eur_time, eur_value in eur_dict.items():

            zone_attribute = SeisWare.ZoneAttribute(eur_time,"")

            zone_attribute.ZoneTypeID(zone_type_generic[0])

            # When iterating check for the name
            if eur_time not in [i.Name() for i in attribute_list]:

                login_instance.ZoneAttributeManager().Add(zone_attribute)

            attributes = SeisWare.WellZoneAttributes()

            attribute = SeisWare.WellZoneAttribute()

            eur = SeisWare.Variant(f"{eur_value}")
            
            # Set the attribute value
            attribute.AttributeValue(eur)
            
            # Set the zone for the attribute
            attribute.ZoneAttribute(zone_attribute)

            # Add the Attribute to the attribute list
            wz_attribute_list.append(attribute)

        # Use the attribute list to set it to use attributes
        attributes.SetAttributes(wz_attribute_list)

        # Set the attributews to the well zone
        well_zone.SetAttributes(attributes)

        # Finally add the Well Zone to the project
        login_instance.WellZoneManager().Add(well_zone)


    else:
        # Display error message if failing to get project
        print("Unable to connect to project")

    return None


