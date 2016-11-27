# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendMessageWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from src import Network
from networkobjects.Node import Host

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


class SendMessage_Window(object):

    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi()

    def setupUi(self):
        self.MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.MainWindow.resize(200, 200)
        self.centralwidget = QtGui.QWidget(self.MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.toComboBox = QtGui.QComboBox(self.centralwidget)
        self.toComboBox.setEditable(False)
        self.toComboBox.setObjectName(_fromUtf8("fromComboBox"))
        self.toComboBox.lineEdit().setInputMask("NNN")
        self.gridLayout.addWidget(self.toComboBox, 1, 2, 1, 1)
        self.toLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toLabel.setFont(font)
        self.toLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.toLabel.setObjectName(_fromUtf8("fromLabel"))
        self.gridLayout.addWidget(self.toLabel, 0, 2, 1, 1)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.sendButton.clicked.connect(self.send_message)
        self.gridLayout.addWidget(self.sendButton, 5, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.fromComboBox = QtGui.QComboBox(self.centralwidget)
        self.fromComboBox.setEditable(False)
        self.fromComboBox.setObjectName(_fromUtf8("toComboBox"))
        self.fromComboBox.lineEdit().setInputMask("NNN")
        self.gridLayout.addWidget(self.fromComboBox, 3, 2, 1, 1)
        self.fromLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fromLabel.setFont(font)
        self.fromLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fromLabel.setObjectName(_fromUtf8("toLabel"))
        self.gridLayout.addWidget(self.fromLabel, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.refreshDropdowns()
        self.MainWindow.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Send Message", None))
        self.fromLabel.setText(_translate("MainWindow", "From:", None))
        self.sendButton.setText(_translate("MainWindow", "Send Message", None))
        self.toLabel.setText(_translate("MainWindow", "To:", None))

    def refreshDropdowns(self):
        # Clear the current dropdown information.
        self.toComboBox.clear()
        self.toComboBox.clearEditText()
        self.fromComboBox.clear()
        self.fromComboBox.clearEditText()
        array = [1, 2, 3]
        # Repopulate the dropdowns with updated info from the network.
        for index in range(len(array)):
            if isinstance(array[index], Host):
                self.toComboBox.addItem(QtCore.QString(array[index]))
                self.fromComboBox.addItem(QtCore.QString(array[index]))

    def send_message(self):
        # Use this for sending the standard string to the network/nodes.
        print str(self.toComboBox.currentText())
        print str(self.fromComboBox.currentText())
        # Send message to the toNode.

        self.refreshDropdowns()

    def getHosts(self):
        array = []
        for index in range(len(Network.nodes)):
            if isinstance(Network.nodes[index], Host):
                array.append(Network.nodes[index])
        return array