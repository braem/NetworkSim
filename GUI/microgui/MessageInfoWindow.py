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
    protocol_stack = ["Application", "Transport", "Network", "Link"]

    def __init__(self, MainWindow, Message, layer_designator):
        self.message = Message
        # Store the layer designator with first letter capitalized
        self.layer = layer_designator.lower().capitalize()
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
        self.messageInfoTable.setRowCount(self.getSpecifiedDepth() + 1)
        self.messageInfoTable.setColumnCount(1)
        self.messageInfoTable.setObjectName(_fromUtf8("messageInfoTable"))
        self.messageInfoTable.horizontalHeader().setVisible(True)
        self.messageInfoTable.horizontalHeader().setDefaultSectionSize(100)
        self.messageInfoTable.verticalHeader().setVisible(True)
        self.messageInfoTable.setHorizontalHeaderLabels(QtCore.QStringList() << "Protocol Stack")
        self.fillTable()
        self.verticalLayout_3.addWidget(self.messageInfoTable)
        self.selectedItemView = QtGui.QLabel(self.centralwidget)
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
    def fillTable(self):
        message_parts = self.parseMessageContents()
        for index in range(self.getSpecifiedDepth() + 1):
            self.addItem(index, message_parts[index])

    # Extracts the message and headers from the core message object.
    def parseMessageContents(self):
        parts_array = []
        # Application message
        parts_array.append(self.message.ip_datagram.segment.message)
        # Segment Header
        parts_array.append('src/dest port: ' +
                           str(self.message.ip_datagram.segment.header.src_port) +
                           '/' +
                           str(self.message.ip_datagram.segment.header.dest_port) +
                           ', length: ' +
                           str(self.message.ip_datagram.segment.header.length) +
                           ', checksum: ' +
                           str(self.message.ip_datagram.segment.header.length))
        # IPDatagram Header
        parts_array.append(self.message.ip_datagram.ip_header)
        # Ethernet Frame Header
        parts_array.append(self.message.frame_header)
        return parts_array

    def addItem(self, row_index, item_text):
        self.messageInfoTable.setItem(row_index, 0, QtGui.QTableWidgetItem(QtCore.QString(item_text)))
        # Resizes all columns to fit their contents.
        self.messageInfoTable.resizeColumnsToContents()

    def setInfoText(self, text):
        self.selectedItemView.setText(QtCore.QString(text))

    def getSpecifiedDepth(self):
        for index in range(len(self.protocol_stack)):
            if self.protocol_stack[index] == self.layer:
                return index
