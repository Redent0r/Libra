# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_purchase.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(220, 366)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(220, 366))
        Dialog.setMaximumSize(QtCore.QSize(400, 366))
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/plus-icon-0.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.leditName = QtGui.QLineEdit(Dialog)
        self.leditName.setPlaceholderText(_fromUtf8(""))
        self.leditName.setObjectName(_fromUtf8("leditName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leditName)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spnboxCost = QtGui.QDoubleSpinBox(Dialog)
        self.spnboxCost.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spnboxCost.setKeyboardTracking(False)
        self.spnboxCost.setSuffix(_fromUtf8(""))
        self.spnboxCost.setDecimals(2)
        self.spnboxCost.setMaximum(9999.0)
        self.spnboxCost.setObjectName(_fromUtf8("spnboxCost"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spnboxCost)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Purchase", None))
        Dialog.setWhatsThis(_translate("Dialog", "Introduzca un código y presione Enter.\n"
"Si ya existe un registro del item, los campos se llenaran", None))
        self.label_2.setText(_translate("Dialog", "Name:", None))
        self.label_5.setText(_translate("Dialog", "Unit Cost:", None))
        self.spnboxCost.setPrefix(_translate("Dialog", "$ ", None))

import res_rc
