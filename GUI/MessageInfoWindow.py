# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageInfoWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class MessageInfo_Window(object):
    protocol_stack = {}

    def __init__(self, MainWindow, protocol_stack_list):
        self.protocol_stack = protocol_stack_list
        self.setupUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 350)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.messageInfoTable = QtGui.QTableWidget(self.centralwidget)
        self.messageInfoTable.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.messageInfoTable.setFont(font)
        self.messageInfoTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.messageInfoTable.setAlternatingRowColors(True)
        self.messageInfoTable.setRowCount(len(self.protocol_stack))
        self.messageInfoTable.setColumnCount(1)
        self.messageInfoTable.setObjectName(_fromUtf8("messageInfoTable"))
        self.messageInfoTable.horizontalHeader().setVisible(True)
        self.messageInfoTable.horizontalHeader().setDefaultSectionSize(100)
        self.messageInfoTable.verticalHeader().setVisible(True)
        self.messageInfoTable.setHorizontalHeaderLabels(QtCore.QStringList() << "Protocol Stack")
        self.fillTable(self.protocol_stack)
        self.verticalLayout_3.addWidget(self.messageInfoTable)
        self.selectedItemView = QtGui.QTextBrowser(self.centralwidget)
        self.selectedItemView.setOpenLinks(False)
        self.selectedItemView.setObjectName(_fromUtf8("selectedItemView"))
        self.verticalLayout_3.addWidget(self.selectedItemView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Info", None))

    # Fills the rows top-down in the order of the list given.
    def fillTable(self, items):
        for index in range(len(items)):
            self.addItem(index, items[index])

    def addItem(self, row_index, item_text):
        self.messageInfoTable.setItem(row_index, 0, QtGui.QTableWidgetItem(QtCore.QString(item_text)))


# Commented as this is used if you execute this file directly which we don't want.
"""
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = MessageInfo_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""

