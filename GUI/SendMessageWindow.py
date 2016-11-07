# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendMessageWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(200, 200)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.fromComboBox = QtGui.QComboBox(self.centralwidget)
        self.fromComboBox.setEditable(True)
        self.fromComboBox.setObjectName(_fromUtf8("fromComboBox"))
        self.fromComboBox.activated.connect(self.populate_dropdown)
        self.fromComboBox.editTextChanged.connect(self.validate_combobox_text)
        self.gridLayout.addWidget(self.fromComboBox, 1, 2, 1, 1)
        self.fromLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fromLabel.setFont(font)
        self.fromLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fromLabel.setObjectName(_fromUtf8("fromLabel"))
        self.gridLayout.addWidget(self.fromLabel, 0, 2, 1, 1)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.sendButton.clicked.connect(send_message)
        self.gridLayout.addWidget(self.sendButton, 5, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.toComboBox = QtGui.QComboBox(self.centralwidget)
        self.toComboBox.setEditable(True)
        self.toComboBox.setObjectName(_fromUtf8("toComboBox"))
        self.toComboBox.activated.connect(self.populate_dropdown)
        self.toComboBox.editTextChanged.connect(self.validate_combobox_text)
        self.gridLayout.addWidget(self.toComboBox, 3, 2, 1, 1)
        self.toLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.toLabel.setFont(font)
        self.toLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.toLabel.setObjectName(_fromUtf8("toLabel"))
        self.gridLayout.addWidget(self.toLabel, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Send Message", None))
        self.fromLabel.setText(_translate("MainWindow", "To:", None))
        self.sendButton.setText(_translate("MainWindow", "Send Message", None))
        self.toLabel.setText(_translate("MainWindow", "From:", None))

    def populate_dropdown(self):
        print("In populate_dropdown")
        # Get the list of nodes and their addresses.

    def find_node(self, node_identifier):
        print("Finding node")

    def validate_combobox_text(self):
        print "Validating combobox text"


def send_message(toComboBox, fromComboBox):
    toNode = toComboBox.itemData(toComboBox.currentIndex())
    fromNode = fromComboBox.itemData(fromComboBox.currentIndex())
    # Send message to the toNode.



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

