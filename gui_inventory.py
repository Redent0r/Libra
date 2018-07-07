# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_inventory.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1269, 712)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/dbIcon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Panama))
        MainWindow.setIconSize(QtCore.QSize(60, 60))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_balance = QtGui.QWidget()
        self.tab_balance.setObjectName(_fromUtf8("tab_balance"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_balance)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox = QtGui.QGroupBox(self.tab_balance)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, -1, -1, -1)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.dateAnnual = QtGui.QDateEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateAnnual.sizePolicy().hasHeightForWidth())
        self.dateAnnual.setSizePolicy(sizePolicy)
        self.dateAnnual.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 2), QtCore.QTime(0, 0, 0)))
        self.dateAnnual.setDate(QtCore.QDate(2017, 1, 2))
        self.dateAnnual.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 1, 2), QtCore.QTime(0, 0, 0)))
        self.dateAnnual.setMinimumDate(QtCore.QDate(2017, 1, 2))
        self.dateAnnual.setObjectName(_fromUtf8("dateAnnual"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dateAnnual)
        self.radioMonthly = QtGui.QRadioButton(self.groupBox)
        self.radioMonthly.setObjectName(_fromUtf8("radioMonthly"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.radioMonthly)
        self.dateMonthly = QtGui.QDateEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateMonthly.sizePolicy().hasHeightForWidth())
        self.dateMonthly.setSizePolicy(sizePolicy)
        self.dateMonthly.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 5, 1), QtCore.QTime(0, 0, 0)))
        self.dateMonthly.setDate(QtCore.QDate(2017, 5, 1))
        self.dateMonthly.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2017, 5, 1), QtCore.QTime(0, 0, 0)))
        self.dateMonthly.setMinimumDate(QtCore.QDate(2017, 5, 1))
        self.dateMonthly.setCurrentSection(QtGui.QDateTimeEdit.MonthSection)
        self.dateMonthly.setObjectName(_fromUtf8("dateMonthly"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.dateMonthly)
        self.radioAnnual = QtGui.QRadioButton(self.groupBox)
        self.radioAnnual.setObjectName(_fromUtf8("radioAnnual"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.radioAnnual)
        self.radioHistoric = QtGui.QRadioButton(self.groupBox)
        self.radioHistoric.setChecked(True)
        self.radioHistoric.setObjectName(_fromUtf8("radioHistoric"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.radioHistoric)
        self.radioDaily = QtGui.QRadioButton(self.groupBox)
        self.radioDaily.setObjectName(_fromUtf8("radioDaily"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.radioDaily)
        self.horizontalLayout.addLayout(self.formLayout)
        self.calBalance = QtGui.QCalendarWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calBalance.sizePolicy().hasHeightForWidth())
        self.calBalance.setSizePolicy(sizePolicy)
        self.calBalance.setMinimumSize(QtCore.QSize(300, 0))
        self.calBalance.setMaximumSize(QtCore.QSize(16777215, 100))
        self.calBalance.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calBalance.setSelectedDate(QtCore.QDate(2017, 3, 1))
        self.calBalance.setMinimumDate(QtCore.QDate(2017, 3, 1))
        self.calBalance.setMaximumDate(QtCore.QDate(2100, 12, 31))
        self.calBalance.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calBalance.setGridVisible(True)
        self.calBalance.setHorizontalHeaderFormat(QtGui.QCalendarWidget.NoHorizontalHeader)
        self.calBalance.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calBalance.setNavigationBarVisible(True)
        self.calBalance.setObjectName(_fromUtf8("calBalance"))
        self.horizontalLayout.addWidget(self.calBalance)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_balance)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tblPurchasesBal = QtGui.QTableView(self.groupBox_2)
        self.tblPurchasesBal.setAlternatingRowColors(True)
        self.tblPurchasesBal.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblPurchasesBal.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblPurchasesBal.setSortingEnabled(True)
        self.tblPurchasesBal.setObjectName(_fromUtf8("tblPurchasesBal"))
        self.tblPurchasesBal.horizontalHeader().setStretchLastSection(True)
        self.tblPurchasesBal.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tblPurchasesBal, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.tab_balance)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tblSalesBal = QtGui.QTableView(self.groupBox_3)
        self.tblSalesBal.setAlternatingRowColors(True)
        self.tblSalesBal.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblSalesBal.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblSalesBal.setSortingEnabled(True)
        self.tblSalesBal.setObjectName(_fromUtf8("tblSalesBal"))
        self.tblSalesBal.horizontalHeader().setStretchLastSection(True)
        self.tblSalesBal.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.tblSalesBal, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.tblBalance = QtGui.QTableWidget(self.tab_balance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblBalance.sizePolicy().hasHeightForWidth())
        self.tblBalance.setSizePolicy(sizePolicy)
        self.tblBalance.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tblBalance.setFont(font)
        self.tblBalance.setFrameShape(QtGui.QFrame.Box)
        self.tblBalance.setFrameShadow(QtGui.QFrame.Raised)
        self.tblBalance.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblBalance.setTabKeyNavigation(False)
        self.tblBalance.setProperty("showDropIndicator", False)
        self.tblBalance.setDragDropOverwriteMode(False)
        self.tblBalance.setAlternatingRowColors(False)
        self.tblBalance.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tblBalance.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tblBalance.setShowGrid(True)
        self.tblBalance.setGridStyle(QtCore.Qt.SolidLine)
        self.tblBalance.setWordWrap(True)
        self.tblBalance.setCornerButtonEnabled(False)
        self.tblBalance.setRowCount(7)
        self.tblBalance.setColumnCount(3)
        self.tblBalance.setObjectName(_fromUtf8("tblBalance"))
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(3, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(4, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(5, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tblBalance.setItem(6, 2, item)
        self.tblBalance.horizontalHeader().setVisible(False)
        self.tblBalance.verticalHeader().setVisible(False)
        self.horizontalLayout_7.addWidget(self.tblBalance)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/calculator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_balance, icon1, _fromUtf8(""))
        self.tab_inventory = QtGui.QWidget()
        self.tab_inventory.setObjectName(_fromUtf8("tab_inventory"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_inventory)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.cmboxInventory = QtGui.QComboBox(self.tab_inventory)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmboxInventory.sizePolicy().hasHeightForWidth())
        self.cmboxInventory.setSizePolicy(sizePolicy)
        self.cmboxInventory.setMinimumSize(QtCore.QSize(20, 0))
        self.cmboxInventory.setSizeIncrement(QtCore.QSize(0, 0))
        self.cmboxInventory.setEditable(False)
        self.cmboxInventory.setInsertPolicy(QtGui.QComboBox.InsertAtBottom)
        self.cmboxInventory.setModelColumn(0)
        self.cmboxInventory.setObjectName(_fromUtf8("cmboxInventory"))
        self.horizontalLayout_6.addWidget(self.cmboxInventory)
        self.leditInventory = QtGui.QLineEdit(self.tab_inventory)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leditInventory.sizePolicy().hasHeightForWidth())
        self.leditInventory.setSizePolicy(sizePolicy)
        self.leditInventory.setMinimumSize(QtCore.QSize(40, 0))
        self.leditInventory.setObjectName(_fromUtf8("leditInventory"))
        self.horizontalLayout_6.addWidget(self.leditInventory)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.tblInventory = QtGui.QTableView(self.tab_inventory)
        self.tblInventory.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblInventory.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblInventory.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblInventory.setSortingEnabled(True)
        self.tblInventory.setCornerButtonEnabled(False)
        self.tblInventory.setObjectName(_fromUtf8("tblInventory"))
        self.tblInventory.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_6.addWidget(self.tblInventory)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/paper-box-icon-63457.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_inventory, icon2, _fromUtf8(""))
        self.tab_purchases = QtGui.QWidget()
        self.tab_purchases.setObjectName(_fromUtf8("tab_purchases"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_purchases)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cmboxPurchases = QtGui.QComboBox(self.tab_purchases)
        self.cmboxPurchases.setObjectName(_fromUtf8("cmboxPurchases"))
        self.horizontalLayout_2.addWidget(self.cmboxPurchases)
        self.leditPurchases = QtGui.QLineEdit(self.tab_purchases)
        self.leditPurchases.setObjectName(_fromUtf8("leditPurchases"))
        self.horizontalLayout_2.addWidget(self.leditPurchases)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tblPurchases = QtGui.QTableView(self.tab_purchases)
        self.tblPurchases.setAlternatingRowColors(True)
        self.tblPurchases.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblPurchases.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblPurchases.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tblPurchases.setSortingEnabled(True)
        self.tblPurchases.setWordWrap(True)
        self.tblPurchases.setCornerButtonEnabled(False)
        self.tblPurchases.setObjectName(_fromUtf8("tblPurchases"))
        self.tblPurchases.horizontalHeader().setStretchLastSection(True)
        self.tblPurchases.verticalHeader().setVisible(False)
        self.tblPurchases.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.tblPurchases)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/cart-arrow-down-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_purchases, icon3, _fromUtf8(""))
        self.tab_sales = QtGui.QWidget()
        self.tab_sales.setObjectName(_fromUtf8("tab_sales"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_sales)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnRemoveSale = QtGui.QPushButton(self.tab_sales)
        self.btnRemoveSale.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/undo-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRemoveSale.setIcon(icon4)
        self.btnRemoveSale.setIconSize(QtCore.QSize(20, 20))
        self.btnRemoveSale.setObjectName(_fromUtf8("btnRemoveSale"))
        self.horizontalLayout_3.addWidget(self.btnRemoveSale)
        self.btnSettle = QtGui.QPushButton(self.tab_sales)
        self.btnSettle.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/payment-256.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSettle.setIcon(icon5)
        self.btnSettle.setIconSize(QtCore.QSize(20, 20))
        self.btnSettle.setObjectName(_fromUtf8("btnSettle"))
        self.horizontalLayout_3.addWidget(self.btnSettle)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.cmboxSales = QtGui.QComboBox(self.tab_sales)
        self.cmboxSales.setObjectName(_fromUtf8("cmboxSales"))
        self.horizontalLayout_3.addWidget(self.cmboxSales)
        self.leditSales = QtGui.QLineEdit(self.tab_sales)
        self.leditSales.setObjectName(_fromUtf8("leditSales"))
        self.horizontalLayout_3.addWidget(self.leditSales)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tblSales = QtGui.QTableView(self.tab_sales)
        self.tblSales.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblSales.setAlternatingRowColors(True)
        self.tblSales.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblSales.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblSales.setSortingEnabled(True)
        self.tblSales.setCornerButtonEnabled(False)
        self.tblSales.setObjectName(_fromUtf8("tblSales"))
        self.tblSales.horizontalHeader().setStretchLastSection(True)
        self.tblSales.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.tblSales)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/cashier-icon-png-8.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_sales, icon6, _fromUtf8(""))
        self.tab_clients = QtGui.QWidget()
        self.tab_clients.setObjectName(_fromUtf8("tab_clients"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_clients)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.cmboxClients = QtGui.QComboBox(self.tab_clients)
        self.cmboxClients.setObjectName(_fromUtf8("cmboxClients"))
        self.horizontalLayout_4.addWidget(self.cmboxClients)
        self.leditClients = QtGui.QLineEdit(self.tab_clients)
        self.leditClients.setObjectName(_fromUtf8("leditClients"))
        self.horizontalLayout_4.addWidget(self.leditClients)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.tblClients = QtGui.QTableView(self.tab_clients)
        self.tblClients.setAlternatingRowColors(True)
        self.tblClients.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tblClients.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblClients.setSortingEnabled(True)
        self.tblClients.setCornerButtonEnabled(False)
        self.tblClients.setObjectName(_fromUtf8("tblClients"))
        self.tblClients.horizontalHeader().setStretchLastSection(True)
        self.tblClients.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tblClients)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/15656.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_clients, icon7, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionPurchase = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/plus-icon-0.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPurchase.setIcon(icon8)
        self.actionPurchase.setObjectName(_fromUtf8("actionPurchase"))
        self.actionSale = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/product_basket-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSale.setIcon(icon9)
        self.actionSale.setObjectName(_fromUtf8("actionSale"))
        self.actionClient = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/manager-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClient.setIcon(icon10)
        self.actionClient.setObjectName(_fromUtf8("actionClient"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/Oxygen-Icons.org-Oxygen-Actions-view-refresh.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon11)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSale)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPurchase)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClient)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Libra v1.0.0", None))
        self.groupBox.setTitle(_translate("MainWindow", "Period", None))
        self.dateAnnual.setDisplayFormat(_translate("MainWindow", "yyyy", None))
        self.radioMonthly.setText(_translate("MainWindow", "Monthly", None))
        self.dateMonthly.setDisplayFormat(_translate("MainWindow", "MMM/yyyy", None))
        self.radioAnnual.setText(_translate("MainWindow", "Annual", None))
        self.radioHistoric.setText(_translate("MainWindow", "Historic", None))
        self.radioDaily.setText(_translate("MainWindow", "Daily", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Purchases", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sales", None))
        __sortingEnabled = self.tblBalance.isSortingEnabled()
        self.tblBalance.setSortingEnabled(False)
        item = self.tblBalance.item(0, 0)
        item.setText(_translate("MainWindow", "Sales (paid)", None))
        item = self.tblBalance.item(0, 2)
        item.setText(_translate("MainWindow", "0.00", None))
        item = self.tblBalance.item(1, 0)
        item.setText(_translate("MainWindow", "Sales (credit)", None))
        item = self.tblBalance.item(1, 2)
        item.setText(_translate("MainWindow", "0.00", None))
        item = self.tblBalance.item(2, 0)
        item.setText(_translate("MainWindow", "Total revenue", None))
        item = self.tblBalance.item(2, 2)
        item.setText(_translate("MainWindow", "0.00", None))
        item = self.tblBalance.item(3, 0)
        item.setText(_translate("MainWindow", "Costs", None))
        item = self.tblBalance.item(3, 1)
        item.setText(_translate("MainWindow", "0.00", None))
        item = self.tblBalance.item(4, 0)
        item.setText(_translate("MainWindow", "Taxes", None))
        item = self.tblBalance.item(4, 1)
        item.setText(_translate("MainWindow", "0.00", None))
        item = self.tblBalance.item(5, 0)
        item.setText(_translate("MainWindow", "Profit", None))
        item = self.tblBalance.item(5, 2)
        item.setText(_translate("MainWindow", "0.00", None))
        item = self.tblBalance.item(6, 0)
        item.setText(_translate("MainWindow", "Profit (margin)", None))
        item = self.tblBalance.item(6, 2)
        item.setText(_translate("MainWindow", "0.00", None))
        self.tblBalance.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_balance), _translate("MainWindow", "Balance", None))
        self.leditInventory.setPlaceholderText(_translate("MainWindow", "Search...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inventory), _translate("MainWindow", "Inventory", None))
        self.leditPurchases.setPlaceholderText(_translate("MainWindow", "Search...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_purchases), _translate("MainWindow", "Purchases", None))
        self.btnRemoveSale.setToolTip(_translate("MainWindow", "Reverse sale", None))
        self.btnSettle.setToolTip(_translate("MainWindow", "Settle debt", None))
        self.leditSales.setPlaceholderText(_translate("MainWindow", "Search...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sales), _translate("MainWindow", "Sales", None))
        self.leditClients.setPlaceholderText(_translate("MainWindow", "Search...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_clients), _translate("MainWindow", "Clients", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionPurchase.setText(_translate("MainWindow", "Purchase", None))
        self.actionSale.setText(_translate("MainWindow", "Sale", None))
        self.actionClient.setText(_translate("MainWindow", "Client", None))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh", None))

import res_rc
