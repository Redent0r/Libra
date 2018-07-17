# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_cliente_modificar.ui'
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
        Dialog.resize(188, 227)
        Dialog.setMinimumSize(QtCore.QSize(188, 227))
        Dialog.setMaximumSize(QtCore.QSize(350, 227))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/resources/edit_user_male_write_pencil_man-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.leditName = QtGui.QLineEdit(Dialog)
        self.leditName.setReadOnly(True)
        self.leditName.setObjectName(_fromUtf8("leditName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.leditName)
        self.leditPhone = QtGui.QLineEdit(Dialog)
        self.leditPhone.setObjectName(_fromUtf8("leditPhone"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.leditPhone)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.leditAddress = QtGui.QLineEdit(Dialog)
        self.leditAddress.setObjectName(_fromUtf8("leditAddress"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.leditAddress)
        self.leditEmail = QtGui.QLineEdit(Dialog)
        self.leditEmail.setObjectName(_fromUtf8("leditEmail"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.leditEmail)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.leditCellphone = QtGui.QLineEdit(Dialog)
        self.leditCellphone.setObjectName(_fromUtf8("leditCellphone"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.leditCellphone)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.leditFax = QtGui.QLineEdit(Dialog)
        self.leditFax.setObjectName(_fromUtf8("leditFax"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.leditFax)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.leditID = QtGui.QLineEdit(Dialog)
        self.leditID.setMinimumSize(QtCore.QSize(0, 0))
        self.leditID.setPlaceholderText(_fromUtf8(""))
        self.leditID.setObjectName(_fromUtf8("leditID"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.leditID)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnModify = QtGui.QPushButton(Dialog)
        self.btnModify.setObjectName(_fromUtf8("btnModify"))
        self.horizontalLayout.addWidget(self.btnModify)
        self.btnUndo = QtGui.QPushButton(Dialog)
        self.btnUndo.setObjectName(_fromUtf8("btnUndo"))
        self.horizontalLayout.addWidget(self.btnUndo)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Modify Client", None))
        self.label.setText(_translate("Dialog", "Name: ", None))
        self.label_2.setText(_translate("Dialog", "Phone: ", None))
        self.label_3.setText(_translate("Dialog", "Address: ", None))
        self.label_4.setText(_translate("Dialog", "E-mail: ", None))
        self.label_5.setText(_translate("Dialog", "Cellphone: ", None))
        self.label_6.setText(_translate("Dialog", "Fax:", None))
        self.label_7.setText(_translate("Dialog", "ID:", None))
        self.btnModify.setText(_translate("Dialog", "Modify", None))
        self.btnUndo.setText(_translate("Dialog", "Undo", None))

import res_rc
