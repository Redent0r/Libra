
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

        ### Database Connection, for qsqlquerymodel ###
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.DB_LOCATION)
        self.db.open()

         ### Table Models ###
        self.mdlInventory = QtSql.QSqlQueryModel()

        ### Actions functionality ###
        self.actionRefresh.triggered.connect(self.refreshTables)

        self.radioHistoric.toggled.connect(lambda: self.set_balance(self.radioHistoric))
        self.radioAnnual.toggled.connect(lambda: self.set_balance(self.radioAnnual))
        self.radioMonthly.toggled.connect(lambda: self.set_balance(self.radioMonthly))
        self.dateAnnual.dateChanged.connect(lambda: self.set_balance(self.radioAnnual))
        self.dateMonthly.dateChanged.connect(lambda: self.set_balance(self.radioMonthly))

        self.calBalance.selectionChanged.connect(self.calendar_changed)
        self.calBalance.showToday()

        ### Creates tables if not exists, for mec_inventario ###
        self.conn = sqlite3.connect(self.DB_LOCATION)
        self.c = self.conn.cursor()
        mec_inventory.create_tables(self.conn, self.c)

        self.set_balance(self.radioHistoric)
        self.refreshTables()

        # bal stretch
        self.tblBalance.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tblBalance.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        end = time.time()
        print("constructor time: " + str(end - start))

    def refreshTables(self):

        start = time.time()

        self.mdlInventory.setQuery("""SELECT code, name, groupx, avail, costUni, priceUniSug,
                                   stockmin, stockmax, category FROM Inventory""", self.db)

        end = time.time()
        print("refresh time: " + str(end - start))
        
    def calendar_changed(self):
        pass
    def set_balance(self, radioButton):
        pass

    def combo_box_changed(self, comboBox, proxy):

        proxy.setFilterKeyColumn(comboBox.currentIndex())

    def search(self, text, proxy):

        proxy.setFilterRegExp("^" + text)

    def closeEvent(self,event):

        msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Warning",
                                    "Are you sure you want to exit?", parent=self)
        btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
        btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

        msgbox.exec_()

        if msgbox.clickedButton() == btnYes:

            self.db.close()
            self.c.close()
            self.conn.close()
            event.accept()

        else:
            event.ignore()

##################### starts everything #############################################
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    inventory = Inventory() # borrar esto
    inventory.show() # si se va a condicionar al nas location
    sys.exit(app.exec_())
