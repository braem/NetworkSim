# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtfiles\macroview.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from Connection import *
from Node import *

__author__ = "Darren Hendrickson"
__version__ = "1.0.0"

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


class Ui_MainWindow(QtGui.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(805, 575)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frameMain = QtGui.QFrame(self.centralwidget)
        self.frameMain.setGeometry(QtCore.QRect(0, 0, 631, 521))
        self.frameMain.setAcceptDrops(True)
        self.frameMain.setAutoFillBackground(False)
        self.frameMain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMain.setLineWidth(1)
        self.frameMain.setObjectName(_fromUtf8("frameMain"))
        self.lblHost1Image = QtGui.QLabel(self.frameMain)
        self.lblHost1Image.setGeometry(QtCore.QRect(110, 150, 41, 31))
        self.lblHost1Image.setText(_fromUtf8(""))
        self.lblHost1Image.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/pc.png")))
        self.lblHost1Image.setObjectName(_fromUtf8("lblHost1Image"))
        self.lblHost2Image = QtGui.QLabel(self.frameMain)
        self.lblHost2Image.setGeometry(QtCore.QRect(480, 150, 41, 31))
        self.lblHost2Image.setText(_fromUtf8(""))
        self.lblHost2Image.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/pc.png")))
        self.lblHost2Image.setObjectName(_fromUtf8("lblHost2Image"))
        self.lblRouterImage = QtGui.QLabel(self.frameMain)
        self.lblRouterImage.setEnabled(True)
        self.lblRouterImage.setGeometry(QtCore.QRect(280, 250, 41, 41))
        self.lblRouterImage.setText(_fromUtf8(""))
        self.lblRouterImage.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/router.png")))
        self.lblRouterImage.setObjectName(_fromUtf8("lblRouterImage"))
        self.lblSwitchImage = QtGui.QLabel(self.frameMain)
        self.lblSwitchImage.setEnabled(True)
        self.lblSwitchImage.setGeometry(QtCore.QRect(220, 250, 41, 41))
        self.lblSwitchImage.setText(_fromUtf8(""))
        self.lblSwitchImage.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/switch.png")))
        self.lblSwitchImage.setObjectName(_fromUtf8("lblSwitchImage"))
        self.linConnection1 = QtGui.QFrame(self.frameMain)
        self.linConnection1.setGeometry(QtCore.QRect(123, 180, 20, 91))
        self.linConnection1.setFrameShadow(QtGui.QFrame.Plain)
        self.linConnection1.setLineWidth(6)
        self.linConnection1.setFrameShape(QtGui.QFrame.VLine)
        self.linConnection1.setObjectName(_fromUtf8("linConnection1"))
        self.linConnection2 = QtGui.QFrame(self.frameMain)
        self.linConnection2.setGeometry(QtCore.QRect(130, 260, 120, 16))
        self.linConnection2.setFrameShadow(QtGui.QFrame.Plain)
        self.linConnection2.setLineWidth(5)
        self.linConnection2.setFrameShape(QtGui.QFrame.HLine)
        self.linConnection2.setObjectName(_fromUtf8("linConnection2"))
        self.linConnection3 = QtGui.QFrame(self.frameMain)
        self.linConnection3.setGeometry(QtCore.QRect(250, 260, 130, 16))
        self.linConnection3.setFrameShadow(QtGui.QFrame.Plain)
        self.linConnection3.setLineWidth(5)
        self.linConnection3.setFrameShape(QtGui.QFrame.HLine)
        self.linConnection3.setObjectName(_fromUtf8("linConnection3"))
        self.linConnection4 = QtGui.QFrame(self.frameMain)
        self.linConnection4.setGeometry(QtCore.QRect(380, 260, 120, 16))
        self.linConnection4.setFrameShadow(QtGui.QFrame.Plain)
        self.linConnection4.setLineWidth(5)
        self.linConnection4.setFrameShape(QtGui.QFrame.HLine)
        self.linConnection4.setObjectName(_fromUtf8("linConnection4"))
        self.linConnection5 = QtGui.QFrame(self.frameMain)
        self.linConnection5.setGeometry(QtCore.QRect(490, 180, 20, 91))
        self.linConnection5.setFrameShadow(QtGui.QFrame.Plain)
        self.linConnection5.setLineWidth(5)
        self.linConnection5.setFrameShape(QtGui.QFrame.VLine)
        self.linConnection5.setObjectName(_fromUtf8("linConnection5"))
        self.lblHost1Image.raise_()
        self.lblHost2Image.raise_()
        self.linConnection1.raise_()
        self.linConnection2.raise_()
        self.linConnection3.raise_()
        self.lblSwitchImage.raise_()
        self.lblRouterImage.raise_()
        self.dockNodesConnections = QtGui.QDockWidget(self.centralwidget)
        self.dockNodesConnections.setGeometry(QtCore.QRect(590, 20, 201, 161))
        self.dockNodesConnections.setAutoFillBackground(True)
        self.dockNodesConnections.setFloating(True)
        self.dockNodesConnections.setObjectName(_fromUtf8("dockNodesConnections"))
        self.dockNCContents = QtGui.QWidget()
        self.dockNCContents.setObjectName(_fromUtf8("dockNCContents"))
        self.btnRouter = QtGui.QPushButton(self.dockNCContents)
        self.btnRouter.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.btnRouter.setObjectName(_fromUtf8("btnRouter"))
        self.btnHost = QtGui.QPushButton(self.dockNCContents)
        self.btnHost.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.btnHost.setObjectName(_fromUtf8("btnHost"))
        self.btnSwitch = QtGui.QPushButton(self.dockNCContents)
        self.btnSwitch.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.btnSwitch.setObjectName(_fromUtf8("btnSwitch"))
        self.lblNodes = QtGui.QLabel(self.dockNCContents)
        self.lblNodes.setGeometry(QtCore.QRect(10, 10, 71, 20))
        self.lblNodes.setObjectName(_fromUtf8("lblNodes"))
        self.btnCoax = QtGui.QPushButton(self.dockNCContents)
        self.btnCoax.setGeometry(QtCore.QRect(120, 40, 75, 23))
        self.btnCoax.setObjectName(_fromUtf8("btnCoax"))
        self.btnFibre = QtGui.QPushButton(self.dockNCContents)
        self.btnFibre.setGeometry(QtCore.QRect(120, 70, 75, 23))
        self.btnFibre.setObjectName(_fromUtf8("btnFibre"))
        self.btnCustom = QtGui.QPushButton(self.dockNCContents)
        self.btnCustom.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.btnCustom.setObjectName(_fromUtf8("btnCustom"))
        self.lblConnections = QtGui.QLabel(self.dockNCContents)
        self.lblConnections.setGeometry(QtCore.QRect(120, 10, 71, 20))
        self.lblConnections.setObjectName(_fromUtf8("lblConnections"))
        self.dockNodesConnections.setWidget(self.dockNCContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionRecent = QtGui.QAction(MainWindow)
        self.actionRecent.setObjectName(_fromUtf8("actionRecent"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.retranslateUi(MainWindow)
        # I cannot figure out how create generic calls here yet so will need to redo each time .ui file is recreated
        self.initializeNetwork();
        QtCore.QObject.connect(self.btnHost, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addHost)
        QtCore.QObject.connect(self.btnSwitch, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addSwitch)
        QtCore.QObject.connect(self.btnRouter, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addRouter)
        QtCore.QObject.connect(self.btnCoax, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addCoax)
        QtCore.QObject.connect(self.btnFibre, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addFibre)
        QtCore.QObject.connect(self.btnCustom, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addCustom)
#        clickable(self.frameMain).connect(self.test())
        # copy to here
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.dockNodesConnections.setWindowTitle(_translate("MainWindow", "Nodes and Connections", None))
        self.btnRouter.setText(_translate("MainWindow", "Router", None))
        self.btnHost.setText(_translate("MainWindow", "Host", None))
        self.btnSwitch.setText(_translate("MainWindow", "Switch", None))
        self.lblNodes.setText(_translate("MainWindow", "Nodes", None))
        self.btnCoax.setText(_translate("MainWindow", "Coaxial", None))
        self.btnFibre.setText(_translate("MainWindow", "Fibre", None))
        self.btnCustom.setText(_translate("MainWindow", "Custom", None))
        self.lblConnections.setText(_translate("MainWindow", "Connections", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionRecent.setText(_translate("MainWindow", "Recent", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

# I cannot figure out how to put these calls elsewhere yet so will need to redo each time .ui file is recreated

    def initializeNetwork(self):
        # All graphics hidden to start
        self.lblHost1Image.hide();
        self.lblHost2Image.hide();
        self.lblRouterImage.hide();
        self.lblSwitchImage.hide();
        self.linConnection1.hide();
        self.linConnection2.hide();
        self.linConnection3.hide();
        self.linConnection4.hide();
        self.linConnection5.hide();




        # Only add host button should be enabled to start
        self.btnRouter.setEnabled(False);
        self.btnSwitch.setEnabled(False);
        self.btnCoax.setEnabled(False);
        self.btnFibre.setEnabled(False);
        self.btnCustom.setEnabled(False);

        myNode = Node(0, "Host", 100, 200)


        myNode2 = Node(1, "Host", 150, 200)

        connections = []

        connection = Connection(0, myNode, myNode2)

        connections.append(connection)
        print "here you are"

    def addHost(self):
        if self.lblHost1Image.isVisible():
            self.lblHost2Image.show();
            self.btnHost.setEnabled(False);
            self.btnRouter.setEnabled(True);
            self.btnSwitch.setEnabled(True);
            self.btnCoax.setEnabled(True);
            self.btnFibre.setEnabled(True);
            self.btnCustom.setEnabled(True);

        else:
            self.lblHost1Image.show();

    def addRouter(self):
        if self.lblRouterImage.isVisible():
            self.lblRouterImage.hide();
        else:
            self.lblRouterImage.show();

    def addSwitch(self):
        if self.lblSwitchImage.isVisible():
            self.lblSwitchImage.hide();
        else:
            self.lblSwitchImage.show();

        self.placeRouter();

    def addCoax(self):
        self.changeConnectionType("Coax");

    def addFibre(self):
        self.changeConnectionType("Fibre");

    def addCustom(self):
        self.changeConnectionType("Custom");

    def placeRouter(self):
        if self.lblSwitchImage.isVisible():
            self.lblRouterImage.setGeometry(QtCore.QRect(360, 250, 41, 41));
        else:
            self.lblRouterImage.setGeometry(QtCore.QRect(280, 250, 41, 41));

    def changeConnectionType(self, connectionType):

        self.linConnection1.show();
        self.linConnection2.show();
        self.linConnection3.show();
        self.linConnection4.show();
        self.linConnection5.show();

        if connectionType == "Coax":
            self.linConnection1.setStyleSheet("color:blue");
            self.linConnection2.setStyleSheet("color:blue");
            self.linConnection3.setStyleSheet("color:blue");
            self.linConnection4.setStyleSheet("color:blue");
            self.linConnection5.setStyleSheet("color:blue");
        elif connectionType == "Fibre":
            self.linConnection1.setStyleSheet("color:red");
            self.linConnection2.setStyleSheet("color:red");
            self.linConnection3.setStyleSheet("color:red");
            self.linConnection4.setStyleSheet("color:red");
            self.linConnection5.setStyleSheet("color:red");
        else:
            self.linConnection1.setStyleSheet("color:green");
            self.linConnection2.setStyleSheet("color:green");
            self.linConnection3.setStyleSheet("color:green");
            self.linConnection4.setStyleSheet("color:green");
            self.linConnection5.setStyleSheet("color:green");

    def mousePressEvent(self, event):
        print "some shit"

    def test(self):
        print "please"

