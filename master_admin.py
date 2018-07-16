
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
from gui_modify import Ui_Dialog as ModifyGui

import mec_inventory#, stresstest


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
        self.mdlClients = QtSql.QSqlQueryModel()
        self.mdlPurchases = QtSql.QSqlQueryModel()
        self.mdlSales = QtSql.QSqlQueryModel()
        self.mdlInventory = QtSql.QSqlQueryModel()
        # bal
        self.mdlPurchasesBal = QtSql.QSqlQueryModel()
        self.mdlSalesBal = QtSql.QSqlQueryModel()
       
        ### sort filter proxy model ###
        self.proxyInventory = QtGui.QSortFilterProxyModel()
        self.proxyInventory.setSourceModel(self.mdlInventory)
        self.proxyPurchases = QtGui.QSortFilterProxyModel()
        self.proxyPurchases.setSourceModel(self.mdlPurchases)
        self.proxySales = QtGui.QSortFilterProxyModel()
        self.proxySales.setSourceModel(self.mdlSales)
        self.proxyClients = QtGui.QSortFilterProxyModel()
        self.proxyClients.setSourceModel(self.mdlClients)
        # bal
        self.proxyPurchasesBal = QtGui.QSortFilterProxyModel()
        self.proxyPurchasesBal.setSourceModel(self.mdlPurchasesBal)
        self.proxySalesBal = QtGui.QSortFilterProxyModel()
        self.proxySalesBal.setSourceModel(self.mdlSalesBal)

        ### proxy filter parameters
        self.proxyInventory.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive) # case insennsitive
        self.proxyPurchases.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.proxySales.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.proxyClients.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        # bal
        self.proxyPurchasesBal.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.proxySalesBal.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)

        #### setting models to tables ###
        self.tblInventory.setModel(self.proxyInventory)
        self.tblPurchases.setModel(self.proxyPurchases)
        self.tblSales.setModel(self.proxySales)
        self.tblClients.setModel(self.proxyClients)
        # bal
        self.tblPurchasesBal.setModel(self.proxyPurchasesBal)
        self.tblSalesBal.setModel(self.proxySalesBal)

        ### Actions functionality ###
        self.actionRefresh.triggered.connect(self.refreshTables)
        self.actionPurchase.triggered.connect(self.action_purchase)
        self.actionSale.triggered.connect(self.action_sale)
        self.actionClient.triggered.connect(self.action_client)
        self.btnModifyInventory.clicked.connect(self.modify_inventory)
        self.btnRemovePurchase.clicked.connect(self.remove_purchase)
        self.btnRemoveSale.clicked.connect(self.reverse_sale)
        self.btnSettle.clicked.connect(self.settle_debt)
        self.btnRemoveClient.clicked.connect(self.remove_client)
        self.leditInventory.textEdited.connect(lambda: self.search(self.leditInventory.text(), self.proxyInventory))
        self.leditPurchases.textEdited.connect(lambda: self.search(self.leditPurchases.text(), self.proxyPurchases))
        self.leditSales.textEdited.connect(lambda: self.search(self.leditSales.text(), self.proxySales))
        self.leditClients.textEdited.connect(lambda: self.search(self.leditClients.text(), self.proxyClients))

        self.cmboxInventory.activated.connect(lambda: self.combo_box_changed(self.cmboxInventory, self.proxyInventory))
        self.cmboxPurchases.activated.connect(lambda: self.combo_box_changed(self.cmboxPurchases, self.proxyPurchases))
        self.cmboxSales.activated.connect(lambda: self.combo_box_changed(self.cmboxSales, self.proxySales))
        self.cmboxClients.activated.connect(lambda: self.combo_box_changed(self.cmboxClients, self.proxyClients))

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

        ########################## STRESSS TESTTTTTT ################################
        #stresstest.test_entries(self.conn, self.c, 10)
        #stresstest.test_entries(self.conn, self.c, 100)
        #stresstest.test_entries(self.conn, self.c, 250)
        #stresstest.test_entries(self.conn, self.c, 500)
        #stresstest.test_entries(self.conn, self.c, 1000)
        ################################################################################

        self.set_balance(self.radioHistoric)
        self.refreshTables()

        headers = ["Code", "Name", "Group", "Available Quantity", "Unit Cost",
                    "Suggested Price", "Minimum Quantity", "Maximum Quantity", "Category"]
        for i in range(len(headers)):
            self.mdlInventory.setHeaderData(i, QtCore.Qt.Horizontal, headers[i]) # +1 for id col
        self.cmboxInventory.addItems(headers) # add headers to combo box

        headers = ["Date", "Transaction", "Code", "Name", "Group", "Quantity", "Vendor",
                    "Unit Cost", "Total Cost", "Category"]
        for i in range(len(headers)):
            self.mdlPurchases.setHeaderData(i, QtCore.Qt.Horizontal, headers[i])
        self.cmboxPurchases.addItems(headers)

        headers = ["Date", "Transaction", "Code", "Name", "Group", "Quantity", "Unit Price",
                    "Total Price", "Client", "Pay"]
        for i in range(len(headers)):
            self.mdlSales.setHeaderData(i, QtCore.Qt.Horizontal, headers[i])
        self.cmboxSales.addItems(headers)

        headers = ["ID", "Name", "Invested", "Debt",
                    "E-mail", "Phone", "Cellphone"]
        for i in range(len(headers)):
            self.mdlClients.setHeaderData(i, QtCore.Qt.Horizontal, headers[i])
        self.cmboxClients.addItems(headers)

        # headers bal
        headers = ["Date", "Transaction", "Code", "Quantity", "Total Cost"]
        for i in range(len(headers)):
            self.mdlPurchasesBal.setHeaderData(i, QtCore.Qt.Horizontal, headers[i])

        headers = ["Date", "Transaction", "Code", "Quantity", "Total Price"]
        for i in range(len(headers)):
            self.mdlSalesBal.setHeaderData(i, QtCore.Qt.Horizontal, headers[i])

        ### table uniform stretch ###
        self.tblInventory.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)
        self.tblPurchases.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)
        self.tblSales.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)
        self.tblClients.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)

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

        self.mdlPurchases.setQuery("""SELECT dat, trans, code, name, groupx, quantity, 
                                provider, costUni, costItems, category FROM Entries""", self.db)

        self.mdlSales.setQuery("""SELECT dat, trans, code, name, groupx, quantity, priceUni, 
                                priceItems, client, payment FROM Outs""", self.db)

        self.mdlClients.setQuery("""SELECT identification, name, money_invested, debt,
                                     mail, num, cel FROM Clients""", self.db)

        # bal tables
        self.mdlPurchasesBal.setQuery(""" SELECT dat, trans, code, quantity, costItems 
                                                            FROM Entries """, self.db)

        self.mdlSalesBal.setQuery("""SELECT dat, trans, code, quantity,
                                priceItems FROM Outs""", self.db)


        end = time.time()
        print("refresh time: " + str(end - start))
        
    def settle_debt(self):

        index = self.tblSales.selectionModel().selectedRows()
        if index:
            row = int(index[0].row()) # selected row
            code = self.proxySales.data(self.proxySales.index(row, 1)) # 0 = fecha, 1 = codigo

            msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Settle",
                                        "Are you sure you wish to settle\n"
                                         "the debt generated by sale number: " + code + "?", parent=self)
            btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
            btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

            msgbox.exec_()

            if msgbox.clickedButton() == btnYes:
   
                mec_inventory.paid(self.conn, self.c, code)
                QtGui.QMessageBox.information(self, 'Message', "The debt generated by sale number: " + code +
                                 "\nhas been settled successfully")
                self.refreshTables()

        else:

            QtGui.QMessageBox.information(self, 'Message', "Please select the sale by\n" +
                                 "credit you wish to settle")
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

    def modify_inventory(self):

        index = self.tblInventory.selectionModel().selectedRows() ### list of indexes
        if index:
            
            row = int(index[0].row()) # selected row
            code = self.proxyInventory.data(self.proxyInventory.index(row, 0))
            group = self.proxyInventory.data(self.proxyInventory.index(row, 2))
            modifyInventory = ModifyInventory(code, group, self)
            modifyInventory.show()
            self.tblInventory.clearSelection() # clear choice

        else:
            QtGui.QMessageBox.information(self, 'Message', "Please select the \n" +
                                 "item you wish to modify")

    def remove_client(self):

        index = self.tblClients.selectionModel().selectedRows()

        if index:

            row = int(index[0].row()) # selected row
            name = self.proxyClients.data(self.proxyClients.index(row, 1)) # 0 = fecha, 1 = codigo

            msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Delete",
                                        "Are you sure you want to delete: " + name + "?", parent=self)
            btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
            btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

            msgbox.exec_()

            if msgbox.clickedButton() == btnYes:

                if mec_inventory.del_client_name(self.conn, self.c, name):
                    self.refreshTables() # refresh
                    QtGui.QMessageBox.information(self, 'Message', "The client: " + name +
                                                        "\nhas been deleted sucessfully")
                else:

                    QtGui.QMessageBox.critical(self, 'Error', 'An unexpected error has occurred.\n'+
                                                            'Please try again.')

            self.tblClients.clearSelection() # clear choice

        else:
            QtGui.QMessageBox.information(self, 'Message', "Please select the \n" +
                                 "client you wish to delete")

    def remove_purchase(self):

        index = self.tblPurchases.selectionModel().selectedRows()
        if index:
            row = int(index[0].row()) # selected row
            code = self.proxyPurchases.data(self.proxyPurchases.index(row, 1)) # 0 = fecha, 1 = codigo

            msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Delete",
                                        "Are you sure you want to delete purchase\n"
                                         " number: " + code + "?", parent=self)
            btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
            btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

            msgbox.exec_()

            if msgbox.clickedButton() == btnYes:

                if mec_inventory.del_general(self.conn, self.c, code):
                    self.refreshTables() # refresh
                    QtGui.QMessageBox.information(self, 'Message', "Purchase number: " + code +
                                                        "\nhas been deleted successfully.\n" +
                                                        "Inventory must be reduced manually")
                else:

                    QtGui.QMessageBox.critical(self, 'Error', 'An unexpected error has occurred.\n'+
                                                            'Please try again.')

            self.tblPurchases.clearSelection() # clear choice

        else:
            QtGui.QMessageBox.information(self, 'Message', "Please select the\n" +
                                 "purchase that you want to delete")

    def reverse_sale(self):

        index = self.tblSales.selectionModel().selectedRows()
        if index:
            row = int(index[0].row()) # selected row
            code = self.proxySales.data(self.proxySales.index(row, 1)) # 0 = fecha, 1 = codigo

            msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Reverse",
                                        "Are you sure you want to reverse\n"
                                         "purchase number: " + code + "?", parent=self)
            btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
            btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

            msgbox.exec_()

            if msgbox.clickedButton() == btnYes:

                if mec_inventory.del_general(self.conn, self.c, code):
                    self.refreshTables() # refresh
                    QtGui.QMessageBox.information(self, 'Message', "Purchase number: " + code +
                                                        "\nhas been reversed successfully")
                else:

                    QtGui.QMessageBox.critical(self, 'Error', 'An unexpected error has occurred.\n'+
                                                            'Please try again.')

            self.tblSales.clearSelection() # clear choice

        else:
            QtGui.QMessageBox.warning(self, 'Message', "Please select the\n" +
                                 "purchase you want to reverse")

    def action_client(self):

        client = Client(self)
        client.show()

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
        self.btnUndo.clicked.connect(self.undo)
        self.btnConfirm.clicked.connect(self.confirm)
        self.btnDelete.clicked.connect(self.delete_entry)
        self.spnboxPrice.valueChanged.connect(self.price_changed)
        self.spnBoxMargin.valueChanged.connect(self.margin_changed)
        self.spnBoxQuantity.valueChanged.connect(self.quantity_changed)
        self.tblInventory.clicked.connect(self.table_clicked)

        ### combo box nombre config ###
        self.cmboxClient.setModel(self.parent().mdlClients)
        self.cmboxClient.setModelColumn(1)
        self.cmboxClient.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.cmboxClient.setEditText("")

        ### table ###
        self.model = QtGui.QStandardItemModel()
        self.model.setColumnCount(5)
        header = ["Code", "Name",  "Item Price", "Quantity", "Total Price"]
        self.model.setHorizontalHeaderLabels(header)
        self.tblItems.setModel(self.model)

        ### abstract table / list of lists ###
        self.abstractTable = []

        ### mini innventario ###
        self.mdlInventory = QtSql.QSqlQueryModel()
        self.proxyInventory = QtGui.QSortFilterProxyModel()
        self.proxyInventory.setSourceModel(self.mdlInventory)
        self.tblInventory.setModel(self.proxyInventory)

        self.refresh_inventory()
        header = ["Code", "Name", "Available", "Group"]
        for i in range(len(header)):
            self.mdlInventory.setHeaderData(i, QtCore.Qt.Horizontal, header[i])
        self.cmboxInventory.addItems(header) # add headers to combo box

        self.tblInventory.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)

        # search funnctionality
        self.cmboxInventory.activated.connect(self.combo_box_changed)
        self.leditInventory.textChanged.connect(lambda: self.search(self.leditInventory.text()))
        self.proxyInventory.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive) # case insennsitive

        ### sqlite 3 connection from parent ###
        self.conn = self.parent().conn
        self.c = self.parent().c

    def combo_box_changed(self):

        self.proxyInventory.setFilterKeyColumn(self.cmboxInventory.currentIndex())

    def search(self, text):

        self.proxyInventory.setFilterRegExp("^" + text)

    def refresh_inventory(self):

        self.mdlInventory.setQuery("""SELECT code, name, avail, groupx
                                         FROM Inventory""", self.parent().db) # uses parent connection

    def table_clicked(self):

        self.spnBoxQuantity.setValue(1) # reset cantidad
        index = self.tblInventory.selectionModel().selectedRows() ### list of indexes
        row = int(index[0].row()) # selected row
        code = self.proxyInventory.data(self.proxyInventory.index(row, 0))
        group = self.proxyInventory.data(self.proxyInventory.index(row, 3))

        query = mec_inventory.query_sale(self.c, code, group)
 
        if query:

            self.leditCode.setText(code) # arg
            self.leditName.setText(query[0])
            self.leditGroup.setText(group)
            self.spnboxPrice.setValue(query[1])
            self.spnboxCost.setValue(query[2])
            self.price_changed()

        else:
            QtGui.QMessageBox.critical(self, 'Error', "An unexpected error has occurred.\n" +
                                                    "Please try again")
            self.refresh_inventory()

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
    
    def delete_entry(self):
        
            index = self.tblItems.selectionModel().selectedRows() ### list of indexes
            if (index):
                row = int(index[0].row()) # selected row

                self.model.removeRow(row)

                if row == 0:
                    self.cmboxClient.setEnabled(True)

                del self.abstractTable[row] # deletes from abstract table

                self.refreshTotals()

                self.tblItems.clearSelection()

            else:
                QtGui.QMessageBox.information(self, 'Message', 'Please select the line\n' +
                                                        'you wish to remove')

    def price_changed(self):

        if self.spnboxCost.value() > 0:
            margin = (self.spnboxPrice.value() / self.spnboxCost.value()) * 100 - 100
            self.spnBoxMargin.setValue(margin) # sets margin

            self.quantity_changed()

    def undo (self):
        
        self.leditCode.clear()
        self.leditName.clear()
        self.leditGroup.clear()
        self.spnboxCost.setValue(0)
        self.spnboxPrice.setValue(0)
        self.spnBoxQuantity.setValue(1)
        self.spnBoxMargin.setValue(0)
        self.spnboxDiscount.setValue(0)
        self.chkBoxItbms.setChecked(True)
        self.chkBoxCredit.setChecked(False)
        self.spnBoxTotalItemPrice.setValue(0.00)
        
    def add(self):

        ### table view ###
        code = self.leditCode.text()
        
        if code != "":
            
            client = self.cmboxClient.currentText()
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
                line.append(self.cmboxClient.currentText()) # 6
                line.append(self.leditGroup.text()) # 7
 
                self.abstractTable.append(line)
                self.refreshTotals()
                self.undo()
                self.cmboxClient.setEnabled(False) # disable edit client

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
                    self.cmboxClient.clearEditText()
                    self.undo()
                    self.cmboxClient.setEnabled(True)

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

class Client(QtGui.QDialog, ClientGui):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        ### functionality ###
        self.btnUndo.clicked.connect(self.undo)
        self.btnAdd.clicked.connect(self.anadir)

        ### validators ###
        regexpPhone = QtCore.QRegExp("^[0-9-()]*$") # 0-9 or - or ()
        phoneVal = QtGui.QRegExpValidator(regexpPhone)
        self.leditPhone.setValidator(phoneVal)
        self.leditCellphone.setValidator(phoneVal)
        self.leditFax.setValidator(phoneVal)

        ### connection, from parent ###
        self.conn = self.parent().conn
        self.c = self.parent().c

    def anadir(self):

        name = self.leditName.text().title()
        if name != "":
            msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Add Client",
                                        "Are you sure you want to\n"
                                         "add this client?", parent=self)
            btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
            btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

            msgbox.exec_()

            if msgbox.clickedButton() == btnYes:

                start = time.time()

                id = self.leditID.text()
                phone = self.leditPhone.text()
                cellphone = self.leditCellphone.text()
                address = self.leditAddress.text().capitalize()
                email = self.leditEmail.text()
                fax = self.leditFax.text()

                if mec_inventory.add_client(self.conn, self.c, id, name, email, phone, cellphone, fax, address):
                    
                    self.parent().refreshTables()
                    self.undo()
                    QtGui.QMessageBox.information(self, 'Message', 'The client has been\n'+
                                                                        'added successfully')
                    
                else:
                    QtGui.QMessageBox.warning(self, 'Error', 'The client that you are trying\n' +
                                                            'to add already exists')

                end = time.time()
                print("time cliente: " + str(end - start))

        else: # nombre == ""
            QtGui.QMessageBox.warning(self, 'Warning', 'Please insert a name')

    def undo(self):

        self.leditName.clear()
        self.leditID.clear()
        self.leditPhone.clear()
        self.leditCellphone.clear()
        self.leditAddress.clear()
        self.leditFax.clear()
        self.leditEmail.clear()

class ModifyInventory(QtGui.QDialog, ModifyGui):
        
    def __init__(self, code, group, parent=None):

        QtGui.QDialog.__init__(self, parent)
        
        self.setupUi(self)

        # parent connection
        self.conn = self.parent().conn
        self.c = self.parent().c

        self.leditCode.setText(code)
        self.cmboxGroup.addItem(group)
        self.cmboxGroup.addItem("Global")

        items = mec_inventory.query_modify(self.c, code, group)
        # Returns [disponible,precioUniSug,costoUni,categoria,stockmin,stockmax]

        if items:

            self.available = items[0]
            self.price = items[1]
            self.cost = items[2]
            self.category = items[3]
            self.min = items[4]
            self.max = items[5] 
            self.name = items[6]

            self.spnboxAvailable.setValue(self.available)
            self.spnboxPrice.setValue(self.price)
            self.spnboxCost.setValue(self.cost)
            self.cmboxCategory.setEditText(self.category)
            self.spnboxMin.setValue(self.min)
            self.spnboxMax.setValue(self.max)
            self.leditName.setText(self.name)
            self.spnboxMargin.setValue(((self.price / self.cost) - 1) * 100)

        ### functionality ###
        self.btnModify.clicked.connect(self.modify_inventory)
        self.btnUndo.clicked.connect(self.undo)
        
        self.spnboxMargin.valueChanged.connect(self.margin_changed)
        self.spnboxPrice.valueChanged.connect(self.price_changed)
        self.spnboxCost.valueChanged.connect(self.cost_changed)

    def modify_inventory(self):
        
        msgbox = QtGui.QMessageBox(QtGui.QMessageBox.Icon(4), "Modify",
                                        "Are you sure you want\n"
                                         "to modify this item?", parent=self)
        btnYes = msgbox.addButton("Yes", QtGui.QMessageBox.ButtonRole(0)) # yes
        btnNo = msgbox.addButton("No", QtGui.QMessageBox.ButtonRole(1)) # no

        msgbox.exec_()

        if msgbox.clickedButton() == btnYes:

            start = time.time()

            code = self.leditCode.text()
            name = self.leditName.text()
            cost = self.spnboxCost.value()
            margin = self.spnboxMargin.value()
            price = self.spnboxPrice.value()
            available = self.spnboxAvailable.value()
            group = self.cmboxGroup.currentText()
            cat = self.cmboxCategory.currentText().capitalize()
            stockMin = self.spnboxMin.value() 
            stockMax = self.spnboxMax.value() 
           
            ### modificando ###
            mec_inventory.modify(self.conn, self.c, code, group,
                                 available, price, cat, stockMin, stockMax, cost, name)

            self.parent().refreshTables()
            QtGui.QMessageBox.information(self, 'Message', 'The modification has been\n'+
                                                                    'registered successfully')
            self.close()
                
            end = time.time()
            print("modificar time: " + str(end-start))



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

    def undo(self):
 
        self.leditName.setText(self.name)
        self.spnboxCost.setValue(self.cost)
        self.spnboxAvailable.setValue(self.available)
        self.spnboxMargin.setValue((self.price / self.cost - 1) * 100)
        self.spnboxPrice.setValue(self.price)
        self.cmboxCategory.setEditText(self.category)
        self.cmboxGroup.setCurrentIndex(0)
        self.spnboxMin.setValue(self.min)
        self.spnboxMax.setValue(self.max)

##################### starts everything #############################################
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)

    inventory = Inventory() # borrar esto
    inventory.show() # si se va a condicionar al nas location

    # if os.path.isdir("\\\\NASPAREDES\\db"):
    #     inventario = Inventario()
    #     inventario.show()
    # else:
    #     widget = QtGui.QWidget()
    #     QtGui.QMessageBox.warning( widget, 'Error de conexin', 'Necesitamos que este conectado a\n' +
    #                                                     'la red wifi')

    sys.exit(app.exec_())
