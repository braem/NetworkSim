# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\QTFiles\MacroView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Connection import *
from Node import *

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
    connections = []
    nodes = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(805, 575)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frameMain = NetworkFrame(self.centralwidget)

        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.darkGray)
        self.frameMain.setPalette(palette)
        self.frameMain.setAutoFillBackground(False)

        self.frameMain.setGeometry(QtCore.QRect(0, 0, 631, 521))
        self.frameMain.setAcceptDrops(True)
        self.frameMain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMain.setLineWidth(1)
        self.frameMain.setObjectName(_fromUtf8("frameMain"))
        self.dockNodeProperties = QtGui.QDockWidget(self.centralwidget)
        self.dockNodeProperties.setGeometry(QtCore.QRect(580, 30, 211, 251))
        self.dockNodeProperties.setObjectName(_fromUtf8("dockNodeProperties"))
        self.dockNCContents = QtGui.QWidget()
        self.dockNCContents.setObjectName(_fromUtf8("dockNCContents"))
        self.lblLocation = QtGui.QLabel(self.dockNCContents)
        self.lblLocation.setGeometry(QtCore.QRect(30, 50, 46, 13))
        self.lblLocation.setObjectName(_fromUtf8("lblLocation"))
        self.lblType = QtGui.QLabel(self.dockNCContents)
        self.lblType.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.lblType.setObjectName(_fromUtf8("lblType"))
        self.lblNetworkInfo = QtGui.QLabel(self.dockNCContents)
        self.lblNetworkInfo.setGeometry(QtCore.QRect(20, 90, 91, 16))
        self.lblNetworkInfo.setObjectName(_fromUtf8("lblNetworkInfo"))
        self.lblIP = QtGui.QLabel(self.dockNCContents)
        self.lblIP.setGeometry(QtCore.QRect(50, 110, 46, 13))
        self.lblIP.setObjectName(_fromUtf8("lblIP"))
        self.cboNodeType = QtGui.QComboBox(self.dockNCContents)
        self.cboNodeType.setGeometry(QtCore.QRect(108, 10, 81, 22))
        self.cboNodeType.setMaxVisibleItems(3)
        self.cboNodeType.setMaxCount(3)
        self.cboNodeType.setObjectName(_fromUtf8("cboNodeType"))
        self.lblMAC = QtGui.QLabel(self.dockNCContents)
        self.lblMAC.setGeometry(QtCore.QRect(50, 140, 46, 13))
        self.lblMAC.setObjectName(_fromUtf8("lblMAC"))
        self.txtXPos = QtGui.QPlainTextEdit(self.dockNCContents)
        self.txtXPos.setGeometry(QtCore.QRect(90, 50, 51, 21))
        self.txtXPos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtXPos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtXPos.setObjectName(_fromUtf8("txtXPos"))
        self.txtYPos = QtGui.QPlainTextEdit(self.dockNCContents)
        self.txtYPos.setGeometry(QtCore.QRect(160, 50, 51, 21))
        self.txtYPos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtYPos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtYPos.setObjectName(_fromUtf8("txtYPos"))
        self.frameMain.addPosition(self.txtXPos, self.txtYPos)
        self.txtIP = QtGui.QPlainTextEdit(self.dockNCContents)
        self.txtIP.setGeometry(QtCore.QRect(80, 110, 121, 21))
        self.txtIP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtIP.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtIP.setObjectName(_fromUtf8("txtIP"))
        self.txtMAC = QtGui.QPlainTextEdit(self.dockNCContents)
        self.txtMAC.setGeometry(QtCore.QRect(80, 140, 121, 21))
        self.txtMAC.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtMAC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtMAC.setObjectName(_fromUtf8("txtMAC"))
        self.btnModifyNode = QtGui.QPushButton(self.dockNCContents)
        self.btnModifyNode.setGeometry(QtCore.QRect(80, 200, 75, 23))
        self.btnModifyNode.setObjectName(_fromUtf8("btnModifyNode"))
        self.btnDeleteNode = QtGui.QPushButton(self.dockNCContents)
        self.btnDeleteNode.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.btnDeleteNode.setObjectName(_fromUtf8("btnDeleteNode"))
        self.btnAddNode = QtGui.QPushButton(self.dockNCContents)
        self.btnAddNode.setGeometry(QtCore.QRect(30, 170, 75, 23))
        self.btnAddNode.setObjectName(_fromUtf8("btnAddNode"))
        self.dockNodeProperties.setWidget(self.dockNCContents)
        self.dockConnectionProperties = QtGui.QDockWidget(self.centralwidget)
        self.dockConnectionProperties.setGeometry(QtCore.QRect(560, 290, 211, 231))
        self.dockConnectionProperties.setObjectName(_fromUtf8("dockConnectionProperties"))
        self.dockCPContents = QtGui.QWidget()
        self.dockCPContents.setObjectName(_fromUtf8("dockCPContents"))
        self.lblConnectionLength = QtGui.QLabel(self.dockCPContents)
        self.lblConnectionLength.setGeometry(QtCore.QRect(30, 50, 41, 16))
        self.lblConnectionLength.setObjectName(_fromUtf8("lblConnectionLength"))
        self.lblConnectionType = QtGui.QLabel(self.dockCPContents)
        self.lblConnectionType.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.lblConnectionType.setObjectName(_fromUtf8("lblConnectionType"))
        self.lblConnectionBandwidth = QtGui.QLabel(self.dockCPContents)
        self.lblConnectionBandwidth.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.lblConnectionBandwidth.setObjectName(_fromUtf8("lblConnectionBandwidth"))
        self.cboConnectionType = QtGui.QComboBox(self.dockCPContents)
        self.cboConnectionType.setGeometry(QtCore.QRect(108, 10, 81, 22))
        self.cboConnectionType.setMaxVisibleItems(3)
        self.cboConnectionType.setMaxCount(3)
        self.cboConnectionType.setObjectName(_fromUtf8("cboConnectionType"))
        self.txtConnectionLength = QtGui.QPlainTextEdit(self.dockCPContents)
        self.txtConnectionLength.setGeometry(QtCore.QRect(90, 50, 61, 21))
        self.txtConnectionLength.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtConnectionLength.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtConnectionLength.setObjectName(_fromUtf8("txtConnectionLength"))
        self.txtConnectionBandwidth = QtGui.QPlainTextEdit(self.dockCPContents)
        self.txtConnectionBandwidth.setGeometry(QtCore.QRect(90, 80, 61, 21))
        self.txtConnectionBandwidth.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtConnectionBandwidth.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtConnectionBandwidth.setObjectName(_fromUtf8("txtConnectionBandwidth"))
        self.btnModifyConnection = QtGui.QPushButton(self.dockCPContents)
        self.btnModifyConnection.setGeometry(QtCore.QRect(60, 170, 75, 23))
        self.btnModifyConnection.setObjectName(_fromUtf8("btnModifyConnection"))
        self.btnAddConnection = QtGui.QPushButton(self.dockCPContents)
        self.btnAddConnection.setGeometry(QtCore.QRect(40, 140, 75, 23))
        self.btnAddConnection.setObjectName(_fromUtf8("btnAddConnection"))
        self.btnDeleteConnection = QtGui.QPushButton(self.dockCPContents)
        self.btnDeleteConnection.setGeometry(QtCore.QRect(120, 140, 75, 23))
        self.btnDeleteConnection.setObjectName(_fromUtf8("btnDeleteConnection"))
        self.dockConnectionProperties.setWidget(self.dockCPContents)

        # some temp stuff


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

        # I cannot figure out how create generic calls here yet so will need to redo each time .ui file is recreated
        self.initializeWidgets();

        self.retranslateUi(MainWindow)
        self.cboNodeType.setCurrentIndex(-1)
        self.cboConnectionType.setCurrentIndex(-1)
        # calling functions from buttons here
        QtCore.QObject.connect(self.cboConnectionType, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.decideBandwidth)
        QtCore.QObject.connect(self.btnAddConnection, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addConnection)
        QtCore.QObject.connect(self.btnDeleteConnection, QtCore.SIGNAL(_fromUtf8("clicked()")), self.deleteConnection)
        QtCore.QObject.connect(self.btnModifyConnection, QtCore.SIGNAL(_fromUtf8("clicked()")), self.modifyConnection)
        QtCore.QObject.connect(self.btnAddNode, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addNode)
        QtCore.QObject.connect(self.btnDeleteNode, QtCore.SIGNAL(_fromUtf8("clicked()")), self.deleteNode)
        QtCore.QObject.connect(self.btnModifyNode, QtCore.SIGNAL(_fromUtf8("clicked()")), self.modifyNode)

        # copy to here


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.dockNodeProperties.setWindowTitle(_translate("MainWindow", "Node Properties", None))
        self.lblLocation.setText(_translate("MainWindow", "Location", None))
        self.lblType.setText(_translate("MainWindow", "Node Type", None))
        self.lblNetworkInfo.setText(_translate("MainWindow", "Network Info", None))
        self.lblIP.setText(_translate("MainWindow", "IP", None))
        self.lblMAC.setText(_translate("MainWindow", "MAC", None))
        self.btnModifyNode.setText(_translate("MainWindow", "Modify", None))
        self.btnDeleteNode.setText(_translate("MainWindow", "Delete", None))
        self.btnAddNode.setText(_translate("MainWindow", "Add", None))
        self.dockConnectionProperties.setWindowTitle(_translate("MainWindow", "Connection Properties", None))
        self.lblConnectionLength.setText(_translate("MainWindow", "Length", None))
        self.lblConnectionType.setText(_translate("MainWindow", "Connection Type", None))
        self.lblConnectionBandwidth.setText(_translate("MainWindow", "Bandwidth", None))
        self.btnModifyConnection.setText(_translate("MainWindow", "Modify", None))
        self.btnAddConnection.setText(_translate("MainWindow", "Add", None))
        self.btnDeleteConnection.setText(_translate("MainWindow", "Delete", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionRecent.setText(_translate("MainWindow", "Recent", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

    # I cannot figure out how to put these calls elsewhere yet so will need to copy each time .ui file is recreated

    def populateDropDown(self):
        self.cboNode1.clear()
        self.cboNode2.clear()
        for x in range(0, self.nodes.__len__()):
            self.cboNode1.addItem(str(self.nodes[x]._Node__Node_ID))
            self.cboNode2.addItem(str(self.nodes[x]._Node__Node_ID))

    def initializeWidgets(self):
        self.decideBandwidth()
        self.cboConnectionType.addItems(['Coax', 'Fibre', 'Custom'])
        self.cboNodeType.addItems(['Host', 'Router', 'Switch'])

    def decideBandwidth(self):
        if self.cboConnectionType.currentText() == "Custom":
            self.lblConnectionBandwidth.show()
            self.txtConnectionBandwidth.show()
        else:
            self.lblConnectionBandwidth.hide()
            self.txtConnectionBandwidth.hide()

    def addNode(self):
        thisNode = Node(self.cboNodeType.currentText(), self.txtXPos.toPlainText(), self.txtYPos.toPlainText())
        self.nodes.append(thisNode)
        self.placeNodeGraphic(thisNode)

    # deletes node, but doesn't repaint (node will still show on screen despite it not existing)
    def deleteNode(self):
        fullPass = False
        while fullPass == False:
            if not self.nodes:
                break
            for x in xrange(len(self.nodes)):
                if self.nodes[x].isSelected:
                    fullPass = False
                    self.nodes.pop(x)
                    break
                else:
                    fullPass = True
                x = x + 1
        # call repaint

    # modifies node, but doesn't repaint (node will not move to new location)
    # difficult to implement. Worry about add/delete working properly
    def modifyNode(self):
        foundOne = False
        for x in xrange(len(self.nodes)):
            if self.nodes[x].isSelected and not foundOne:
                foundOne = True
                nodeToModifyIndex = self.nodes[x]
            elif self.nodes[x].isSelected and foundOne:
                tooMany = True
                break
            x = x + 1
        if tooMany:
            print "Can only modify one node at a time"
        else:
            self.nodes[nodeToModifyIndex] = Node(self.cboNodeType.currentText(), self.txtXPos.toPlainText(), self.txtYPos.toPlainText())
        # call repaint

    def addConnection(self):
        tooMany = False
        numNodes = 0

        for x in xrange(len(self.nodes)):
            if self.nodes[x].isSelected and numNodes == 0:
                node1 = self.nodes[x]
                numNodes = numNodes + 1
            elif self.nodes[x].isSelected and numNodes == 1:
                node2 = self.nodes[x]
                numNodes = numNodes + 1
            elif self.nodes[x].isSelected and numNodes == 2:
                tooMany = True
            x = x + 1

        if not tooMany and numNodes == 2:
            connection = Connection(node1, node2)
            connection.connectionType = self.cboConnectionType.currentText()
            connection.connectionLength = self.txtConnectionLength.toPlainText()
            connection.connectionBandWidth = self.txtConnectionBandwidth.toPlainText()
            self.connections.append(connection)

            self.placeConnectionGraphic(connection.getUniqueID(), connection.getConnectionType(), node1, node2)
        elif tooMany:
            print "Cant select more than 2 nodes before attempting to create a connection"
        else:
            print "Must select 2 nodes before attempting to create a connection"

    def deleteConnection(self):
        print "delete: " + self
        # call repaint

    # difficult to implement. Worry about add/delete working properly
    def modifyConnection(self):
        print "modify connection"
        # call repaint

    def placeNodeGraphic(self, aNode):
        self.lblNode = NodeLabel(self.frameMain)
        self.lblNode.setGeometry(int(self.txtXPos.toPlainText()), int(self.txtYPos.toPlainText()), 41, 31)
        self.lblNode.setText(_fromUtf8(""))
        self.lblNode.nodeObject = aNode
        if self.cboNodeType.currentText() == "Host":
            self.lblNode.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/pc.png")))
        elif self.cboNodeType.currentText() == "Router":
            self.lblNode.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/router.png")))
        else:
            self.lblNode.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/switch.png")))

        self.lblNode.setObjectName(_fromUtf8(aNode.getUniqueID()))
        self.lblNode.show()

    def placeConnectionGraphic(self, uniqueName, connectionType, firstNode, secondNode):

        # connection will always be a pair of lines 1 horizontal and 1 vertical

        # find center of firstNode image as start x, y
        start = firstNode.getLocation()
        end = secondNode.getLocation()
        x1 = int(start[0]) + 20
        y1 = int(start[1]) + 15

        x2 = int(end[0]) + 20
        y2 = int(end[1]) + 15

        if connectionType == "Coax":
            connectionColor = "blue"
        elif connectionType == "Fibre":
            connectionColor = "red"
        else:
            connectionColor = "green"

        if (x2 - x1) > 0:  # x direction from node 1 to node 2 is positive
            if (y2 - y1) > 0:  # y direction from node 1 to node 2 is positive
                if (x2 - x1) > (y2 - y1):  # line in x direction is longer than y
                    self.drawHorizontalLine(x1, y1, (x2 - x1), connectionColor, uniqueName)
                    self.drawVerticalLine(x2, y1, (y2 - y1), connectionColor, uniqueName)
                else:  # line in y is longer than x
                    self.drawVerticalLine(x1, y1, (y2 - y1), connectionColor, uniqueName)
                    self.drawHorizontalLine(x1, y2, (x2 - x1), connectionColor, uniqueName)
            else:  # y direction from node 1 to node 2 is negative
                if (x2 - x1) > (y1 - y2):  # line in x direction is longer than y
                    self.drawHorizontalLine(x1, y1, (x2 - x1), connectionColor, uniqueName)
                    self.drawVerticalLine(x2, y2, (y1 - y2), connectionColor, uniqueName)
                else:  # line in y is longer than x
                    self.drawVerticalLine(x1, y2, (y1 - y2), connectionColor, uniqueName)
                    self.drawHorizontalLine(x1, y2, (x2 - x1), connectionColor, uniqueName)
        else:  # x direction from node 1 to node 2 is negative
            if (y2 - y1) > 0:  # y direction from node 1 to node 2 is positive
                if (x1 - x2) > (y2 - y1):  # line in x is longer than y
                    self.drawHorizontalLine(x2, y1, (x1 - x2), connectionColor, uniqueName)
                    self.drawVerticalLine(x2, y1, (y2 - y1), connectionColor, uniqueName)
                else:  # line in y is longer than x
                    self.drawVerticalLine(x1, y1, (y2 - y1), connectionColor, uniqueName)
                    self.drawHorizontalLine(x2, y2, (x1 - x2), connectionColor, uniqueName)
            else:  # y direction from node 1 to node 2 is negative
                if (x1 - x2) > (y1 - y2):  # line in x is longer than y
                    self.drawHorizontalLine(x2, y1, (x1 - x2), connectionColor, uniqueName)
                    self.drawVerticalLine(x2, y2, (y1 - y2), connectionColor, uniqueName)
                else:  # line in y is longer than x
                    self.drawVerticalLine(x1, y2, (y1 - y2), connectionColor, uniqueName)
                    self.drawHorizontalLine(x2, y2, (x1 - x2), connectionColor, uniqueName)

    def drawHorizontalLine(self, xPos, yPos, lineLength, lineColor, connectionName):
        self.linConnection = NetworkConnection(self.frameMain)
        self.linConnection.setGeometry(QtCore.QRect(xPos, yPos, lineLength, 6))
        self.linConnection.setStyleSheet(_fromUtf8("color:" + lineColor))

        self.linConnection.setFrameShadow(QtGui.QFrame.Plain)
        self.linConnection.setLineWidth(6)
        self.linConnection.setFrameShape(QtGui.QFrame.HLine)
        self.linConnection.setObjectName(_fromUtf8(connectionName + "H"))
        self.linConnection.lower()
        self.linConnection.show()

    def drawVerticalLine(self, xPos, yPos, lineLength, lineColor, connectionName):
        self.linConnection = NetworkConnection(self.frameMain)
        self.linConnection.setGeometry(QtCore.QRect(xPos, yPos, 6, lineLength))
        self.linConnection.setStyleSheet(_fromUtf8("color:" + lineColor))

        self.linConnection.setFrameShadow(QtGui.QFrame.Plain)
        self.linConnection.setLineWidth(6)
        self.linConnection.setFrameShape(QtGui.QFrame.VLine)
        self.linConnection.setObjectName(_fromUtf8(connectionName + "V"))
        self.linConnection.lower()
        self.linConnection.show()


class NodeLabel(QtGui.QLabel):
    myX = 0
    myY = 0
    myW = 0
    myH = 0

    comboBox1 = None
    comboBox2 = None
    nodeObject = None

    def mouseDoubleClickEvent(self, ev):
        print "double click event"

    def mousePressEvent(self, ev):
        point = ev.pos()

        self.nodeObject.toggleIsSelected()
        self.highlightSelected()

    def highlightSelected(self):
        if self.nodeObject.isSelected:
            if self.nodeObject.getType() == "Host":
                self.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/pc_hl.png")))
            elif self.nodeObject.getType() == "Router":
                self.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/router_hl.png")))
            else:
                self.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/switch_hl.png")))
        else:
            if self.nodeObject.getType() == "Host":
                self.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/pc.png")))
            elif self.nodeObject.getType() == "Router":
                self.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/router.png")))
            else:
                self.setPixmap(QtGui.QPixmap(_fromUtf8("../Resources/switch.png")))

    def setGeometry(self, ax, ay, aw, ah):
        super(NodeLabel, self).setGeometry(ax, ay, aw, ah)
        self.myX = ax
        self.myY = ay
        self.myW = aw
        self.myH = ah


class NetworkFrame(QtGui.QFrame):
    myX = 0
    myY = 0
    myW = 0
    myH = 0
    txtXPosBox = None
    txtYPosBox = None

    def addPosition(self, tbXpos, tbYpos):
        self.txtXPosBox = tbXpos
        self.txtYPosBox = tbYpos

    def mousePressEvent(self, ev):
        point = ev.pos()
        posX = self.round10((point.x() + self.myX), 10)
        posY = self.round10((point.y() + self.myY), 10)

        self.txtXPosBox.setPlainText(`posX`)
        self.txtYPosBox.setPlainText(`posY`)

    def round10(self, x, base=10):
        return int(base * round(float(x) / base))


class NetworkConnection(QtGui.QFrame):
    myX = 0
    myY = 0
    myW = 0
    myH = 0
    connectionName = ""

    def mousePressEvent(self, ev):
        point = ev.pos()
        posX = point.x() + self.myX
        posY = point.y() + self.myY

        print "connection clicked " + self.connectionName
