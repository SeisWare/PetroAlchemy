import SeisWare
import pandas as pd
import numpy as np

def export_EUR_to_SeisWare(login_instance,eur_value, well):


    """
    Input : Well name(str) and eur values(list)

    After EUR values are calculated in plot_decline_curve.py, send EUR values
    as Formation Top(?) back to SeisWare.
    """

     # Check to make sure login_instance has been created before pushing data

    if login_instance != None:
       
        # Create full well zone

        well_zone = SeisWare.WellZone()
        
        well_zone.WellID(well)
        well_zone.Zone()

        # Create zone attribute in project
        
        project_zone_attributes = SeisWare.WellZoneAttributes()

        # Create the zone attribute for the well

        well_zone_attribute = SeisWare.WellZoneAttribute()

        # Set the value equal to the eur

        well_zone_attribute.AttributeValue(eur_value[0])

        # Add zone attribute to zone

        login_instance.WellZoneAttribute.Add

        # Add zone to project

        SeisWare.WellZoneManager().Add(well_zone)




    else:
        # Display error message if failing to get project

    return None