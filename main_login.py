
import sys
import sqlite3

from PyQt4 import QtCore, QtGui, QtSql

from gui_login import Ui_Dialog as LoginGui
import master_admin

import mec_login

class Login(QtGui.QDialog, LoginGui):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        ### database ###
        self.conn = sqlite3.connect(".libra.db")
        self.c = self.conn.cursor()
        mec_login.create_login_table(self.c, self.conn)
        self.show()

    def closeEvent(self, e):
        print("closing")
        self.c.close()
        self.conn.close()
        e.accept()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtGui.QDialog.Accepted:
        mainwindow = master_admin.Inventory()
        mainwindow.show()
    sys.exit(app.exec_())