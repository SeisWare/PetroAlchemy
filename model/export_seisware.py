import SeisWare
import pandas as pd
import numpy as np

def export_EUR(login_instance,well_UWI,eur_value):


    """
    Input : Well name(str) and eur values(list)

    After EUR values are calculated in plot_decline_curve.py, send EUR values
    as a Well Zone Attribute back to SeisWare.
    """

     # Check to make sure login_instance has been created before pushing data

    if login_instance != None:
       
        # Create full well zone
        well_list = SeisWare.WellList()

        login_instance.WellManager().GetAll(well_list)

        well = [i for i in well_list if i.UWI() == well_UWI]

        zone = SeisWare.Zone()

        zone.Name("EUR")

        print(zone.ID().toString())

        well_zone = SeisWare.WellZone()

        well = well[0]

        #Create well zone
        well_zone.WellID(well.ID())
        well_zone.Zone(zone)
        well_zone.TopMD(SeisWare.Measurement(0,SeisWare.Unit.Meter))
        well_zone.BaseMD(well.TotalDepth())

        attribute_list = SeisWare.ZoneAttributeList()

        login_instance.ZoneAttributeManager().GetAll(attribute_list)


        if "EUR" not in [i.Name() for i in attribute_list]:

            zone_attribute = SeisWare.ZoneAttribute("EUR", "")

            login_instance.ZoneAttributeManager().Add(zone_attribute)

        else:
            zone_attribute = SeisWare.ZoneAttribute("EUR","")


        attributes = SeisWare.WellZoneAttributes()

        attribute = SeisWare.WellZoneAttribute()

        wz_attribute_list = SeisWare.WellZoneAttributeList()

        

        eur = SeisWare.Variant(eur_value)
        # Set the attribute value
        attribute.AttributeValue(eur)
        attribute.ZoneAttribute(zone_attribute)

        wz_attribute_list.append(attribute)

        attributes.SetAttributes(wz_attribute_list)


        well_zone.SetAttributes(attributes)


        #print(well_zone)

        login_instance.WellZoneManager().Add(well_zone)

        #print(well_zone.Zone().ID().toString())


    else:
        # Display error message if failing to get project
        print(None)

    return None