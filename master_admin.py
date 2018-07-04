
### std lib ###
import sys
import sqlite3
import time
import os

### PyQt4 ###
from PyQt4 import QtCore, QtGui, QtSql

### GUIs ###
from gui_inventory import Ui_MainWindow as InventoryGui
from gui_purchase import Ui_Dialog as PurchaseGui

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
        # bal
        self.mdlPurchasesBal = QtSql.QSqlQueryModel()

        # bal
        self.proxyPurchasesBal = QtGui.QSortFilterProxyModel()
        self.proxyPurchasesBal.setSourceModel(self.mdlPurchasesBal)

        # bal
        self.proxyPurchasesBal.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)

        # bal
        self.tblPurchasesBal.setModel(self.proxyPurchasesBal)

        ### Actions functionality ###
        self.actionRefresh.triggered.connect(self.refreshTables)
        self.actionPurchase.triggered.connect(self.action_purchase)

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

        # headers bal
        headers = ["Date", "Transaction", "Code", "Quantity", "Total Cost"]
        for i in range(len(headers)):
            self.mdlPurchasesBal.setHeaderData(i, QtCore.Qt.Horizontal, headers[i])

        # bal stretch
        self.tblBalance.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tblBalance.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tblPurchasesBal.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)


        end = time.time()
        print("constructor time: " + str(end - start))

    def refreshTables(self):

        start = time.time()

        self.mdlInventory.setQuery("""SELECT code, name, groupx, avail, costUni, priceUniSug,
                                   stockmin, stockmax, category FROM Inventory""", self.db)

        # bal tables
        self.mdlPurchasesBal.setQuery(""" SELECT dat, trans, code, quantity, costItems 
                                                            FROM Entries """, self.db)

        end = time.time()
        print("refresh time: " + str(end - start))
        
    def calendar_changed(self):

        start = time.time()

        self.radioDaily.setChecked(True)

        date = str(self.calBalance.selectedDate().toPyDate())
        self.search(date, self.proxyPurchasesBal)
        items = mec_inventory.calc_bal_day(self.c, date[0:4], date[5:7], date[8:10])
        self.tblBalance.setItem(0, 2, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[2]))) # ventas contado
        self.tblBalance.setItem(1, 2, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[3]))) # ventas credito 
        self.tblBalance.setItem(2, 2, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[1]))) # ingreso tot
        self.tblBalance.setItem(3, 1, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[0]))) # costo
        self.tblBalance.setItem(4, 1, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[5]))) # impuesto
        self.tblBalance.setItem(5, 2, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[6]))) # ganancia
        if items[0] != 0:
            self.tblBalance.setItem(6, 2, QtGui.QTableWidgetItem('% {0:.2f}'.format(items[6]/items[0] * 100))) 
        else:
            self.tblBalance.setItem(6, 2, QtGui.QTableWidgetItem('% 0.00'))

        end = time.time()

        print("cal: " + str(end - start))

    def set_balance(self, radioButton):

        start = time.time()

        if radioButton.isChecked():
            items = []
            if radioButton == self.radioHistoric:

                self.search("", self.proxyPurchasesBal)

                items = mec_inventory.calc_bal_his(self.c)
                # [costoTot,precioTot,cd,cc,ingresoTot,impuestoTot,gananciaTot]

            elif radioButton == self.radioAnnual:

                date = str(self.dateAnnual.date().toPyDate())
                self.search(date[0:4], self.proxyPurchasesBal)
                items = mec_inventory.calc_bal_year(self.c, date[0:4])
                # [costoTot,precioTot,cd,cc,ingresoTot,impuestoTot,gananciaTot]

            else: # radio mensual

                date = str(self.dateMonthly.date().toPyDate())
                self.search((date[0:4] + "-" + date[5:7]), self.proxyPurchasesBal)
                items = mec_inventory.calc_bal_mes(self.c, date[0:4], date[5:7])
                # [costoTot,precioTot,cd,cc,ingresoTot,impuestoTot,gananciaTot]

            self.tblBalance.setItem(0, 2, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[2])))
            self.tblBalance.setItem(1, 2, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[3])))
            self.tblBalance.setItem(2, 2, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[1])))
            self.tblBalance.setItem(3, 1, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[0])))
            self.tblBalance.setItem(4, 1, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[5])))
            self.tblBalance.setItem(5, 2, QtGui.QTableWidgetItem('$ {0:.2f}'.format(items[6])))
            if items[0] != 0:
                self.tblBalance.setItem(6, 2, QtGui.QTableWidgetItem('% {0:.2f}'.format(items[6]/items[0] * 100)))
            else:
                self.tblBalance.setItem(6, 2, QtGui.QTableWidgetItem('% 0.00'))

        end = time.time()

        print("bal: " + str(end - start))

    def combo_box_changed(self, comboBox, proxy):

        proxy.setFilterKeyColumn(comboBox.currentIndex())

    def search(self, text, proxy):

        proxy.setFilterRegExp("^" + text)

    def action_purchase(self):

        purchase = Purchase(self)
        purchase.show()

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

class Purchase(QtGui.QDialog, PurchaseGui):

    def __init__ (self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        ### connection, from parent #######
        self.conn = self.parent().conn
        self.c = self.parent().c
##################### starts everything #############################################
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    inventory = Inventory() # borrar esto
    inventory.show() # si se va a condicionar al nas location
    sys.exit(app.exec_())
