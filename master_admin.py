
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
from gui_sale import Ui_Dialog as SaleGui
from gui_client import Ui_Dialog as ClientGui

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
        self.mdlSalesBal = QtSql.QSqlQueryModel()

        # bal
        self.proxyPurchasesBal = QtGui.QSortFilterProxyModel()
        self.proxyPurchasesBal.setSourceModel(self.mdlPurchasesBal)
        self.proxySalesBal = QtGui.QSortFilterProxyModel()
        self.proxySalesBal.setSourceModel(self.mdlSalesBal)

        # bal
        self.proxyPurchasesBal.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.proxySalesBal.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)

        # bal
        self.tblPurchasesBal.setModel(self.proxyPurchasesBal)
        self.tblSalesBal.setModel(self.proxySalesBal)

        ### Actions functionality ###
        self.actionRefresh.triggered.connect(self.refreshTables)
        self.actionPurchase.triggered.connect(self.action_purchase)
        self.actionSale.triggered.connect(self.action_sale)

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

        headers = ["Date", "Transaction", "Code", "Quantity", "Total Price"]
        for i in range(len(headers)):
            self.mdlSalesBal.setHeaderData(i, QtCore.Qt.Horizontal, headers[i])

        # bal stretch
        self.tblBalance.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tblBalance.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tblPurchasesBal.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)
        self.tblSalesBal.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)

        end = time.time()
        print("constructor time: " + str(end - start))

    def refreshTables(self):

        start = time.time()

        self.mdlInventory.setQuery("""SELECT code, name, groupx, avail, costUni, priceUniSug,
                                   stockmin, stockmax, category FROM Inventory""", self.db)

        # bal tables
        self.mdlPurchasesBal.setQuery(""" SELECT dat, trans, code, quantity, costItems 
                                                            FROM Entries """, self.db)

        self.mdlSalesBal.setQuery("""SELECT dat, trans, code, quantity,
                                priceItems FROM Outs""", self.db)


        end = time.time()
        print("refresh time: " + str(end - start))
        
    def calendar_changed(self):

        start = time.time()

        self.radioDaily.setChecked(True)

        date = str(self.calBalance.selectedDate().toPyDate())
        self.search(date, self.proxyPurchasesBal)
        self.search(date, self.proxySalesBal)
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
                self.search("", self.proxySalesBal)
                items = mec_inventory.calc_bal_his(self.c)
                # [costoTot,precioTot,cd,cc,ingresoTot,impuestoTot,gananciaTot]

            elif radioButton == self.radioAnnual:

                date = str(self.dateAnnual.date().toPyDate())
                self.search(date[0:4], self.proxyPurchasesBal)
                self.search(date[0:4], self.proxySalesBal)
                items = mec_inventory.calc_bal_year(self.c, date[0:4])
                # [costoTot,precioTot,cd,cc,ingresoTot,impuestoTot,gananciaTot]

            else: # radio mensual

                date = str(self.dateMonthly.date().toPyDate())
                self.search((date[0:4] + "-" + date[5:7]), self.proxyPurchasesBal)
                self.search((date[0:4] + "-" + date[5:7]), self.proxySalesBal)
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


    def action_sale(self):

        sale = Sale(self)
        sale.show()

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

        ### functionality ###
        self.btnAdd.clicked.connect(self.add)
        self.btnUndo.clicked.connect(self.undo)

        self.spnboxMargin.valueChanged.connect(self.margin_changed)
        self.spnboxPrice.valueChanged.connect(self.price_changed)
        self.spnboxCost.valueChanged.connect(self.cost_changed)

        ### connection, from parent #######
        self.conn = self.parent().conn
        self.c = self.parent().c

        ### combo box categoria config
        self.cmboxCategory.addItems(mec_inventory.unique(self.c, "category", "Inventory"))
        self.cmboxCategory.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)

        ### code combo box ###
        self.cmBoxCode.addItems(mec_inventory.unique(self.c, "code", "Inventory"))
        self.cmBoxCode.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.cmBoxCode.setEditText("")

        self.cmBoxCode.activated.connect(self.code_return)
        self.cmboxGroup.activated.connect(self.group_return)

        self.code = "" # controlling multiple code input

    def cost_changed(self):

        self.spnboxMargin.setValue(0)
        self.spnboxPrice.setValue(0)

    def price_changed(self):

        cost = self.spnboxCost.value()
        if cost > 0:
            price = self.spnboxPrice.value()
            margin = (price/cost - 1) * 100

            self.spnboxMargin.setValue(margin)

    def margin_changed(self):

        margin = self.spnboxMargin.value()
        cost = self.spnboxCost.value()
        price = cost * (1 + margin/100)

        self.spnboxPrice.setValue(price)

    def code_return(self):

        code = self.cmBoxCode.currentText()
        if self.code != code:
            self.cmboxGroup.clear()
            self.cmboxGroup.addItems(mec_inventory.unique(self.c, "groupx", "Inventory", "code", code))
            self.code = code
        self.group_return()

    def group_return(self):

        code = self.cmBoxCode.currentText()

        group = self.cmboxGroup.currentText()

        query = mec_inventory.query_add(self.c, code, group) ### temp error

        if query:
            self.leditName.setText(query[0]) # nombre
            self.spnboxCost.setValue(query[1]) # costo
            self.spnboxPrice.setValue(query[2]) # precio sugerido
            self.cmboxCategory.setEditText(query[3]) # categoria
            self.spnBoxMin.setValue(query[4]) # min
            self.spnBoxMax.setValue(query[5]) # max

            self.price_changed()
            
        else:
            QtGui.QMessageBox.information(self, 'Message', ' No previous records of this code have\n'+
                                                                'been found. New records will be created.')
            
    def undo(self):

        self.leditName.clear()
        self.spnboxCost.setValue(0)
        self.spnBoxQuantity.setValue(1)
        self.spnboxMargin.setValue(0)
        self.spnboxPrice.setValue(0)
        self.cmboxCategory.clearEditText()
        self.cmboxGroup.clearEditText()
        self.leditVendor.clear()
        self.spnBoxMin.setValue(1)
        self.spnBoxMax.setValue(100)
        self.cmBoxCode.clearEditText()

    def add(self):

        code = self.cmBoxCode.currentText()
        name = self.leditName.text().capitalize()

        if code != "" and name != "":

            msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Purchase",
                                        "Are you sure you want to\n"
                                         "store this purchase?", parent=self)
            btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
            btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

            msgbox.exec_()

            if msgbox.clickedButton() == btnYes:

                start = time.time()

                cost = self.spnboxCost.value()
                margin = self.spnboxMargin.value()
                price = self.spnboxPrice.value()
                quantity = self.spnBoxQuantity.value()
                group = self.cmboxGroup.currentText()
                cat = self.cmboxCategory.currentText().capitalize()
                vendor = self.leditVendor.text().capitalize()
                stockMin = self.spnBoxMin.value() 
                stockMax = self.spnBoxMax.value() 


                ### anadiendo ###
                succesful = mec_inventory.add_item_entry(self.conn, self.c, code, name,
                                                         quantity, vendor, cost, price, group, cat, stockMin, stockMax)

                if succesful:

                    self.parent().refreshTables()
                    self.undo() # this has to go after refresh
                    QtGui.QMessageBox.information(self, 'Message', 'This purchase has been\n'+
                                                                        'regstered successfully')

                    self.close()

                else:
                   QtGui.QMessageBox.critical(self, 'Error', 'An unexpected error occurred.\n'+
                                                             'Please try again')

                end = time.time()
                print("compra time: " + str(end-start))

        elif code == "":
            QtGui.QMessageBox.warning(self, 'Warning', 'Please enter a code')

        else: # nombre == ""
            QtGui.QMessageBox.warning(self, 'Warning', 'Please enter a name')


class Sale(QtGui.QDialog, SaleGui):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        ### functionality ###
        self.btnInsert.clicked.connect(self.add)
        self.btnConfirm.clicked.connect(self.confirm)
        self.spnboxPrice.valueChanged.connect(self.price_changed)
        self.spnBoxMargin.valueChanged.connect(self.margin_changed)
        self.spnBoxQuantity.valueChanged.connect(self.quantity_changed)

        ### abstract table / list of lists ###
        self.abstractTable = []

        ### sqlite 3 connection from parent ###
        self.conn = self.parent().conn
        self.c = self.parent().c

    def margin_changed(self):

        price = (1 + (self.spnBoxMargin.value() / 100)) * self.spnboxCost.value()
        self.spnboxPrice.setValue(price)

        self.quantity_changed()

    def quantity_changed(self):

        priceTotalItem = self.spnboxPrice.value() * self.spnBoxQuantity.value()
        self.spnBoxTotalItemPrice.setValue(priceTotalItem)

    def refreshTotals(self):

        if self.abstractTable:
            taxes = 0.0
            discounts = 0.0
            subtotal = 0.0

            for line in self.abstractTable:
                taxes += line[2] * line[3] * line[1] # impuesto * precio * cantidad
                discounts += (1 + line[2]) * line [3] * line[4] * line[1] # (1 + impuesto) * precio * desc * cant
                subtotal += line[3] * line[1] # precio * cantidad

            self.spnBoxSubtotal.setValue(subtotal)
            self.spnBoxTaxT.setValue(taxes)
            self.spnBoxDiscountT.setValue(discounts)
            self.spnBoxGrandTotal.setValue(subtotal + taxes - discounts)

        else:
            self.spnBoxSubtotal.setValue(0)
            self.spnBoxTaxT.setValue(0)
            self.spnBoxDiscountT.setValue(0)
            self.spnBoxGrandTotal.setValue(0)

    def price_changed(self):

        if self.spnboxCost.value() > 0:
            margin = (self.spnboxPrice.value() / self.spnboxCost.value()) * 100 - 100
            self.spnBoxMargin.setValue(margin) # sets margin

            self.quantity_changed()


    def add(self):

        ### table view ###
        code = self.leditCode.text()

        if code != "":

            quantity = self.spnBoxQuantity.value()
            group = self.leditGroup.text()
            error = mec_inventory.sale_valid(self.c, code, client, quantity, group) # returns list of errors

            if not error:
                ### shopping cart table ###
                line = []
                line.append(QtGui.QStandardItem(self.leditCode.text()))
                line.append(QtGui.QStandardItem(self.leditName.text()))
                line.append(QtGui.QStandardItem(self.spnboxPrice.text()))
                line.append(QtGui.QStandardItem(self.spnBoxQuantity.text()))
                line.append(QtGui.QStandardItem(self.spnBoxTotalItemPrice.text()))

                self.model.appendRow(line)

                ### abstract table ###
                line = []
                line.append(self.leditCode.text()) # 0
                line.append(quantity) # 1
                line.append(float(0.07 if self.chkBoxItbms.isChecked() else 0.0)) # 2
                line.append(self.spnboxPrice.value()) # 3
                line.append(self.spnboxDiscount.value() / 100) # 4 # percentage
                line.append("CRE" if self.chkBoxCredit.isChecked() else "DEB") # 5
                line.append(self.leditGroup.text()) # 7

                self.abstractTable.append(line)
                self.refreshTotals()
                self.undo()

            elif 3 in error: # error code for missinng client
                QtGui.QMessageBox.information(self, 'Message', 'No previous records of this client\n' +
                                                    'have been found. Please create it')
                newClient = Client(self.parent())
                newClient.leditName.setText(client)
                newClient.show()

            elif 2 in error:
                QtGui.QMessageBox.warning(self, 'Warning', 'The item quantity you wish to sell\n' +
                                                    'is not available in your inventory')
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'An unexpected error has occurred.\n' +
                                                    'Please try again')
                self.refresh_inventory()
        else: # code == ""
            QtGui.QMessageBox.warning(self, 'Error', 'Please select\n' +
                                                    'an inventory item')

    def confirm(self):

        if self.abstractTable:

            msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Sell",
                                        "Are you sure you\n"
                                         "want to make this sale?", parent=self)
            btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
            btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

            msgbox.exec_()

            if msgbox.clickedButton() == btnYes:

                start = time.time()

                if mec_inventory.shopping_cart(self.conn, self.c, self.abstractTable):

                    self.parent().refreshTables()
                    del self.abstractTable [:]
                    for i in range(self.model.rowCount()):
                        self.model.removeRow(0)
                    self.refreshTotals()
                    self.undo()

                    end = time.time()
                    print("time venta: " + str(end - start))

                    QtGui.QMessageBox.information(self, 'Message', 'The transaction has been\n'+
                                                                        'registered successfully')
                else:
                    
                    QtGui.QMessageBox.critical(self, 'Error', 'An unexpected error has occurred.\n' +
                                                            'Please try again')
                self.refresh_inventory() # regardless succesful or not
        else:
            QtGui.QMessageBox.warning(self, 'Warning', 'Please insert an item\n' +
                                                        'to be sold')

##################### starts everything #############################################
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    inventory = Inventory() # borrar esto
    inventory.show() # si se va a condicionar al nas location
    sys.exit(app.exec_())
