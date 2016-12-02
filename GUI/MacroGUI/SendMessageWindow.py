# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendMessageWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

__version__ = "1.0.2"

from PyQt4 import QtCore, QtGui
import src
from src.Node import Host
from src.Network import network

# from src.Network import *

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


class SendMessage_Window(QtGui.QMainWindow):
    def __init__(self, current_nodes):
        super(SendMessage_Window, self).__init__()
        self.cnodes = current_nodes
        self.setupUi(self.cnodes)


    def setupUi(self, current_nodes):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(200, 200)
        self.centralwidget = QtGui.QWidget()
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.toComboBox = QtGui.QComboBox(self.centralwidget)
        self.toComboBox.setEditable(False)
        self.toComboBox.setObjectName(_fromUtf8("fromComboBox"))
        self.gridLayout.addWidget(self.toComboBox, 1, 2, 1, 1)
        self.toLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toLabel.setFont(font)
        self.toLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.toLabel.setObjectName(_fromUtf8("fromLabel"))
        self.gridLayout.addWidget(self.toLabel, 0, 2, 1, 1)
        # Prep the protocol radios.
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TCPradioButton = QtGui.QRadioButton(self.centralwidget)
        self.TCPradioButton.setFont(font)
        self.TCPradioButton.setText(QtCore.QString('TCP'))
        self.TCPradioButton.setObjectName(_fromUtf8("TCPradioButton"))
        self.gridLayout.addWidget(self.TCPradioButton, 5, 1, 1, 1)
        self.UDPradioButton = QtGui.QRadioButton(self.centralwidget)
        self.UDPradioButton.setFont(font)
        self.UDPradioButton.setText(QtCore.QString('UDP'))
        self.UDPradioButton.setObjectName(_fromUtf8("UDPradioButton"))
        self.gridLayout.addWidget(self.UDPradioButton, 5, 3, 1, 1)
        # Prep the send button.

        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.fromComboBox = QtGui.QComboBox(self.centralwidget)
        self.fromComboBox.setEditable(False)
        self.fromComboBox.setObjectName(_fromUtf8("toComboBox"))
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
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar()
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.sendButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.sendButton.clicked.connect(self.send_message)
        self.gridLayout.addWidget(self.sendButton, 6, 2, 1, 1)

        self.retranslateUi()

        self.refreshDropdowns(current_nodes)
        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("MainWindow", "Send Message", None))
        self.fromLabel.setText(_translate("MainWindow", "From:", None))
        self.sendButton.setText(_translate("MainWindow", "Send Message", None))
        self.toLabel.setText(_translate("MainWindow", "To:", None))

    def refreshDropdowns(self,current_nodes):
        # Clear the current dropdown information.
        self.toComboBox.clear()
        self.toComboBox.clearEditText()
        self.fromComboBox.clear()
        self.fromComboBox.clearEditText()
        array = current_nodes #[1, 2, 3]
        # Repopulate the dropdowns with updated info from the network.
        for index in range(len(array)):
            # if isinstance(array[index], Host):
            if (array[index].type == "Host"):  # Only includes hosts in the options
                self.toComboBox.addItem(QtCore.QString(array[index].id))
                self.fromComboBox.addItem(QtCore.QString(array[index].id))

    def send_message(self):
        # Use this for sending the standard string to the network/nodes.
        #print str(self.toComboBox.currentText())
        #print str(self.fromComboBox.currentText())
        # Send message to the toNode.
        if self.TCPradioButton.isChecked():
            print str("TCP Message")
            network.create_messageTCP(self.toComboBox.currentText(), self.fromComboBox.currentText(), "TCP Message")
        else:
            print str("UDP Message")
            network.create_messageUDP(self.toComboBox.currentText(), self.fromComboBox.currentText(), "UDP Message")

        self.refreshDropdowns(self.cnodes)

    def getHosts(self):
        array = []
        for index in range(len(src.Network.nodes)):
            if isinstance(src.Network.nodes[index], Host):
                array.append(src.Network.nodes[index])
        return array
