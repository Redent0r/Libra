
### std lib ###
import sys
import sqlite3
import time
import os

### PyQt4 ###
from PyQt4 import QtCore, QtGui, QtSql

### GUIs ###
from gui_inventory import Ui_MainWindow as InventoryGui

import mec_inventory# stresstest

class Inventory (QtGui.QMainWindow, InventoryGui):
    ### constants ###
    useNas = False ### change this to use nas
    DB_LOCATION = ".libra.db" # database

    def __init__ (self, parent=None):

        start = time.time()

        ### sets up visual gui ###
        QtGui.QMainWindow.__init__(self, parent) # parent shit for exit bug; object hierarchy
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose) # maybe takes care of closing bug

    def closeEvent(self,event):

        msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Warning",
                                    "Are you sure you want to exit?", parent=self)
        btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
        btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

        msgbox.exec_()

        if msgbox.clickedButton() == btnYes:
            event.accept()

        else:
            event.ignore()

##################### starts everything #############################################
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    inventory = Inventory() # borrar esto
    inventory.show() # si se va a condicionar al nas location
    sys.exit(app.exec_())
