import os
from pathlib import Path

import pandas as pd
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QFile, QObject, Signal, Slot
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox, QInputDialog
from model.import_seisware import get_prod_from_proj, SWprojlist

def import_data(self):

    wells_total = 0

    projects = sorted(i.Name() for i in SWprojlist())

    print(projects)

    dialog = QInputDialog(self)

    item, ok = dialog.getItem(self, "Select SeisWare Project", "List of SeisWare Projects", projects,0, False)
    
    print(item)

    if ok and item:
        df = get_prod_from_proj(item)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Please select a project")
        msg.setWindowTitle("Import Failed")
        msg.exec_()
        return


    df.columns = map(str.lower, df.columns)

    well_names = df["well name"].unique().tolist()

    num_wells = len(well_names)

    wells_total = wells_total + num_wells

    for well_name in well_names:

        well_name = str(well_name)

        # checks if the exact well name is already in the model

        if well_name not in self.model.list:

            self.model.add(well_name)

            dict_well_name = well_name.replace(" ", "_")
            self.well_dataframes_dict[dict_well_name] = df.loc[
                df["well name"] == well_name
            ].reset_index()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"{well_name} already exists, check the file and try again")
            msg.setWindowTitle("Import Failed")
            msg.exec_()
            return

    if wells_total > 1:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"{wells_total} wells have been added 🚀")
        msg.setWindowTitle("Import Finished")
        msg.exec_()
    elif wells_total == 1:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"{well_name} has been added 🚀")
        msg.setWindowTitle("Import Finished")
        msg.exec_()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("No wells have been found")
        msg.setWindowTitle("Import Failed")
        msg.exec_()
