# Micro view GUI for CPSC 444 project
#
# Author: Lukas Pihl

import os
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


class Values():
    buttonHeight = 51
    buttonWidth = 121
    labelHeight = 31
    graphicWidth = 111
    windHeight = 600
    windWidth = 1000


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, device1, device2, device3, device4):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(Values.windWidth, Values.windHeight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.FrameMain = QtGui.QFrame(self.centralwidget)
        self.frameMain = Ui_MainFrame()
        self.frameMain.setupUi(self.FrameMain, Values.windWidth-20, Values.windHeight-30, device1, device2, device3, device4)
        self.FrameMain.show()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Micro View", None))
        if self.frameMain is not None:
           self.frameMain.retranslateUi()

    @staticmethod
    def isValidCombo(device1, device2, device3, device4):
        return Ui_MainFrame.isValidCombo(device1, device2, device3, device4)


# TODO Move all this code to main window
class Ui_MainFrame(object):

    validFlag = False
    deviceList = []
    lineList = []

    def setupUi(self, frameMain, width, height, device1, device2, device3, device4):
        self.myWidth = width
        self.myHeight = height

        frameMain.setGeometry(QtCore.QRect(10, 10, width, height))

        frameMain.setFrameShape(QtGui.QFrame.StyledPanel)
        frameMain.setFrameShadow(QtGui.QFrame.Plain)
        frameMain.setLineWidth(1)
        frameMain.setMidLineWidth(0)
        frameMain.setObjectName(_fromUtf8("frameMain"))

        if self.isValidCombo(device1, device2, device3, device4):
            tempDeviceList = [device1, device2, device3, device4]

            # Get the size of the device list
            size = 0;
            if device4 != None:
                size = 4
            elif device3 != None:
                size = 3
            else:
                size = 2

            totalWidth = (4+Ui_GraphicsLabel.myWidth)*(size-1)

            for i in range(0, size):
                totalWidth += Ui_HostFrame.myWidth

            # Setup device frames
            for i in range(0, size):
                tempoffset = 0
                for j in range(i, size):
                    tempoffset += Ui_HostFrame.getWidth()
                    if j != size-1:
                        tempoffset += Ui_GraphicsLabel.myWidth+2
                thisPosX = self.myWidth/2 + totalWidth/2 - tempoffset
                thisPosY = self.myHeight/2 - Ui_HostFrame.myHeight/2 + Ui_HostFrame.myHeight - self.getDeviceHeight(tempDeviceList[i])
                self.deviceList.append(self.makeDevicePanel(frameMain, tempDeviceList[i], thisPosX, thisPosY))

            for i in range(0, size-1):
                tempoffset = 0
                for j in range(i, size-1):
                    tempoffset += Ui_HostFrame.getWidth() + Ui_GraphicsLabel.getWidth()+2
                thisPosX = self.myWidth/2 + totalWidth/2 - tempoffset
                thisPosY = self.myHeight/2 - Ui_HostFrame.myHeight/2 + Ui_HostFrame.myHeight - Ui_GraphicsLabel.getHeight()
                self.lineList.append(self.makeLine(frameMain, tempDeviceList[i], tempDeviceList[i+1], thisPosX, thisPosY))

            for i in self.deviceList:
                i.getQFrame().show()
            for i in self.lineList:
                i.getQLabel().show()

            self.validFlag = True
        else:
            self.validFlag = False

    def retranslateUi(self):
        if self.isValid():
            for i in self.deviceList:
                i.retranslateUi()

    def isValid(self):
        return self.validFlag

    @staticmethod
    def isValidCombo(device1, device2, device3, device4):
        # TODO replace ints with proper classes
        # 1 = Host, 2 = Router, 3 = Switch
        # Check that first and second devices are not invalid
        if device1 is None or device1 != 1 or device2 is None:
            return False
        # If device 2 is a host, check that devices 3 & 4 are not used
        if device2 == 1:
            if device3 is not None or device4 is not None:
                return False
            return True
        # If device 2 is not a host
        # Check if device 3 is invalid
        if device3 is None:
            return False
        # If device 3 is a host, check that device 4 is not used and device 2 is a router
        if device3 == 1:
            if device2 != 2 or device4 is not None:
                return False
            return True
        # Check device 2 and 3 are not the same
        if device2 == 2 and device3 == 2:
            return False
        if device2 == 3 and device3 == 3:
            return False
        # If device 3 is not a host
        # Check is device 4 is a host
        if device4 == 1:
            return True
        return False

    def getDeviceHeight(self, device):
        if device == 1:
            return Ui_HostFrame.myHeight
        if device == 2:
            return Ui_RouterFrame.myHeight
        if device == 3:
            return Ui_SwitchFrame.myHeight
        return 0

    def makeDevicePanel(self, frameMain, device, posX, posY):
        if device == 1:
            Frame = QtGui.QFrame(frameMain)
            frame = Ui_HostFrame()
            frame.setupUi(Frame, posX, posY)
            return frame
        if device == 2:
            Frame = QtGui.QFrame(frameMain)
            frame = Ui_RouterFrame()
            frame.setupUi(Frame, posX, posY)
            return frame
        if device == 3:
            Frame = QtGui.QFrame(frameMain)
            frame = Ui_SwitchFrame()
            frame.setupUi(Frame, posX, posY)
            return frame

    def makeLine(self, frameMain, deviceLeft, deviceRight, posX, posY):
        GraphicsLabel = QtGui.QLabel(frameMain)
        graphicsLabel = Ui_GraphicsLabel()
        graphicsLabel.setupUi(GraphicsLabel, deviceLeft, deviceRight, posX, posY)
        return graphicsLabel

    def update(self):
        None
        # If device1 is sending and device2 is receiving, activate line[0]
        # If device2 is sending and device1 is receiving, activate line[0]
        # If device2 is sending and device3 is receiving, activate line[1]
        # If device3 is sending and device2 is receiving, activate line[1]
        # If device3 is sending and device4 is receiving, activate line[2]
        # If device4 is sending and device3 is receiving, activate line[2]


class Ui_HostFrame(object):
    myHeight = Values.buttonHeight*5+Values.labelHeight-5 #241
    myWidth = Values.buttonWidth
    myQFrame = None

    def setupUi(self, frameHost, posX, posY):
        frameHost.setGeometry(QtCore.QRect(posX, posY, Ui_HostFrame.myWidth, Ui_HostFrame.myHeight))
        frameHost.setFrameShape(QtGui.QFrame.StyledPanel)
        frameHost.setFrameShadow(QtGui.QFrame.Raised)
        frameHost.setObjectName(_fromUtf8("frameHost"))
        self.myQFrame = frameHost
        self.btnHostA = QtGui.QPushButton(frameHost)
        self.btnHostA.setGeometry(QtCore.QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnHostA.setObjectName(_fromUtf8("btnHostA"))
        self.btnHostA.clicked.connect(self.clickedButton_Application)
        self.btnHostT = QtGui.QPushButton(frameHost)
        self.btnHostT.setGeometry(QtCore.QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth, Values.buttonHeight))
        self.btnHostT.setObjectName(_fromUtf8("btnHostT"))
        self.btnHostT.clicked.connect(self.clickedButton_Transport)
        self.btnHostN = QtGui.QPushButton(frameHost)
        self.btnHostN.setGeometry(QtCore.QRect(0, Values.labelHeight+Values.buttonHeight*2-3, Values.buttonWidth, Values.buttonHeight))
        self.btnHostN.setObjectName(_fromUtf8("btnHostN"))
        self.btnHostN.clicked.connect(self.clickedButton_Network)
        self.btnHostL = QtGui.QPushButton(frameHost)
        self.btnHostL.setGeometry(QtCore.QRect(0, Values.labelHeight+Values.buttonHeight*3-4, Values.buttonWidth, Values.buttonHeight))
        self.btnHostL.setObjectName(_fromUtf8("btnHostL"))
        self.btnHostL.clicked.connect(self.clickedButton_Link)
        self.btnHostP = QtGui.QPushButton(frameHost)
        self.btnHostP.setGeometry(QtCore.QRect(0, Values.labelHeight+Values.buttonHeight*4-5, Values.buttonWidth, Values.buttonHeight))
        self.btnHostP.setObjectName(_fromUtf8("btnHostP"))
        self.lblHost = QtGui.QLabel(frameHost)
        self.lblHost.setGeometry(QtCore.QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblHost.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHost.setObjectName(_fromUtf8("lblHost"))

    def retranslateUi(self):
        self.btnHostA.setText(_translate("HostFrame", "Application", None))
        self.btnHostT.setText(_translate("HostFrame", "Transport", None))
        self.btnHostN.setText(_translate("HostFrame", "Network", None))
        self.btnHostL.setText(_translate("HostFrame", "Link", None))
        self.btnHostP.setText(_translate("HostFrame", "Physical", None))
        self.lblHost.setText(_translate("HostFrame", "Host Name", None))

    @staticmethod
    def getHeight():
        return Ui_HostFrame.myHeight

    @staticmethod
    def getWidth():
        return Ui_HostFrame.myWidth

    def getQFrame(self):
        return self.myQFrame

    def clickedButton_Application(self):
        print "Application"
        # TODO Open Application message window

    def clickedButton_Transport(self):
        print "Transport"
        # TODO Open Transport message window

    def clickedButton_Network(self):
        print "Network"
        # TODO Open Network message window

    def clickedButton_Link(self):
        print "Link"
        # TODO Open Link message window


class Ui_RouterFrame(object):
    myHeight = Values.buttonHeight*3+Values.labelHeight-3 #161
    myWidth = Values.buttonWidth
    myQFrame = None

    def setupUi(self, frameRouter, posX, posY):
        frameRouter.setGeometry(QtCore.QRect(posX, posY, Ui_RouterFrame.myWidth, Ui_RouterFrame.myHeight))
        frameRouter.setFrameShape(QtGui.QFrame.StyledPanel)
        frameRouter.setFrameShadow(QtGui.QFrame.Raised)
        frameRouter.setObjectName(_fromUtf8("frameRouter"))
        self.myQFrame = frameRouter
        self.btnRouterN = QtGui.QPushButton(frameRouter)
        self.btnRouterN.setGeometry(QtCore.QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnRouterN.setObjectName(_fromUtf8("btnRouterN"))
        self.btnRouterN.clicked.connect(self.clickedButton_Network)
        self.btnRouterL = QtGui.QPushButton(frameRouter)
        self.btnRouterL.setGeometry(QtCore.QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth, Values.buttonHeight))
        self.btnRouterL.setObjectName(_fromUtf8("btnRouterL"))
        self.btnRouterL.clicked.connect(self.clickedButton_Link)
        self.btnRouterP = QtGui.QPushButton(frameRouter)
        self.btnRouterP.setGeometry(QtCore.QRect(0, Values.labelHeight+Values.buttonHeight*2-3, Values.buttonWidth, Values.buttonHeight))
        self.btnRouterP.setObjectName(_fromUtf8("btnRouterP"))
        self.lblRouter = QtGui.QLabel(frameRouter)
        self.lblRouter.setGeometry(QtCore.QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblRouter.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRouter.setObjectName(_fromUtf8("lblRouter"))

    def retranslateUi(self):
        self.btnRouterN.setText(_translate("RouterFrame", "Network", None))
        self.btnRouterL.setText(_translate("RouterFrame", "Link", None))
        self.btnRouterP.setText(_translate("RouterFrame", "Physical", None))
        self.lblRouter.setText(_translate("RouterFrame", "Router Name", None))

    @staticmethod
    def getHeight():
        return Ui_HostFrame.myHeight

    @staticmethod
    def getWidth():
        return Ui_HostFrame.myWidth

    def getQFrame(self):
        return self.myQFrame

    def clickedButton_Network(self):
        print "Network"
        # TODO Open Network message window

    def clickedButton_Link(self):
        print "Link"
        # TODO Open Link message window


class Ui_SwitchFrame(object):
    myHeight = Values.buttonHeight*2+Values.labelHeight-2 #121
    myWidth = Values.buttonWidth#101
    myQFrame = None

    def setupUi(self, frameSwitch, posX, posY):
        frameSwitch.setGeometry(QtCore.QRect(posX, posY, Ui_SwitchFrame.myWidth, Ui_SwitchFrame.myHeight))
        frameSwitch.setFrameShape(QtGui.QFrame.StyledPanel)
        frameSwitch.setFrameShadow(QtGui.QFrame.Raised)
        frameSwitch.setObjectName(_fromUtf8("frameSwitch"))
        self.myQFrame = frameSwitch
        self.btnSwitchL = QtGui.QPushButton(frameSwitch)
        self.btnSwitchL.setGeometry(QtCore.QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnSwitchL.setObjectName(_fromUtf8("btnSwitchL"))
        self.btnSwitchL.clicked.connect(self.clickedButton_Link)
        self.btnSwitchP = QtGui.QPushButton(frameSwitch)
        self.btnSwitchP.setGeometry(QtCore.QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth, Values.buttonHeight))
        self.btnSwitchP.setObjectName(_fromUtf8("btnSwitchP"))
        self.lblSwitch = QtGui.QLabel(frameSwitch)
        self.lblSwitch.setGeometry(QtCore.QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblSwitch.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSwitch.setObjectName(_fromUtf8("lblSwitch"))

    def retranslateUi(self):
        self.btnSwitchL.setText(_translate("SwitchFrame", "Link", None))
        self.btnSwitchP.setText(_translate("SwitchFrame", "Physical", None))
        self.lblSwitch.setText(_translate("SwitchFrame", "Switch Name", None))

    @staticmethod
    def getHeight():
        return Ui_HostFrame.myHeight

    @staticmethod
    def getWidth():
        return Ui_HostFrame.myWidth

    def getQFrame(self):
        return self.myQFrame

    def clickedButton_Link(self):
        print "Link"
        # TODO Open Link message window


class Ui_GraphicsLabel(object):
    myHeight = Values.buttonHeight*5-5
    myWidth = Values.graphicWidth
    myType = 0
    active = False
    myLabel = None
    myMaps = []

    def setupUi(self, label, leftDevice, rightDevice, posX, posY):
        label.setGeometry(posX, posY, Ui_GraphicsLabel.myWidth, Ui_GraphicsLabel.myHeight)
        self.myType = self.getType(leftDevice, rightDevice)
        cwd = os.getcwd()
        cwd = cwd.replace("\\", "/")
        self.myMaps.append(self.buildMap(cwd + "/gfx/HH.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/HHa.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/HR.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/HRa.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/HS.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/HSa.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/RH.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/RHa.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/RS.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/RSa.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/SH.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/SHa.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/SR.png"))
        self.myMaps.append(self.buildMap(cwd + "/gfx/SRa.png"))
        if self.myType == 11:
            label.setPixmap(self.myMaps[0])
        elif self.myType == 12:
            label.setPixmap(self.myMaps[2])
        elif self.myType == 13:
            label.setPixmap(self.myMaps[4])
        elif self.myType == 21:
            label.setPixmap(self.myMaps[6])
        elif self.myType == 23:
            label.setPixmap(self.myMaps[8])
        elif self.myType == 31:
            label.setPixmap(self.myMaps[10])
        elif self.myType == 32:
            label.setPixmap(self.myMaps[12])
        label.setAlignment(QtCore.Qt.AlignBottom)
        self.myLabel = label

    def buildMap(self, path):
        map = QtGui.QPixmap(path)
        return map

    @staticmethod
    def getHeight():
        return Ui_GraphicsLabel.myHeight

    @staticmethod
    def getWidth():
        return Ui_GraphicsLabel.myWidth

    def setActive(self, state):
        self.active = state
        self.updateStatus()

    def getQLabel(self):
        return self.myLabel

    def getType(self, left, right):
        if left == 1:
            if right == 1:
                return 11
            if right == 2:
                return 12
            if right == 3:
                return 13
        if left == 2:
            if right == 1:
                return 21
            if right == 3:
                return 23
        if left == 3:
            if right == 1:
                return 31
            if right == 2:
                return 32
        return 0

    def updateStatus(self):
        if self.myType == 11:
            if self.active:
                self.myLabel.setPixmap(self.myMaps[1])
            else:
                self.myLabel.setPixmap(self.myMaps[0])
        if self.myType == 11:
            if self.active:
                self.myLabel.setPixmap(self.myMaps[3])
            else:
                self.myLabel.setPixmap(self.myMaps[2])
        if self.myType == 11:
            if self.active:
                self.myLabel.setPixmap(self.myMaps[5])
            else:
                self.myLabel.setPixmap(self.myMaps[4])
        if self.myType == 11:
            if self.active:
                self.myLabel.setPixmap(self.myMaps[7])
            else:
                self.myLabel.setPixmap(self.myMaps[6])
        if self.myType == 11:
            if self.active:
                self.myLabel.setPixmap(self.myMaps[9])
            else:
                self.myLabel.setPixmap(self.myMaps[8])
        if self.myType == 11:
            if self.active:
                self.myLabel.setPixmap(self.myMaps[11])
            else:
                self.myLabel.setPixmap(self.myMaps[10])
        if self.myType == 11:
            if self.active:
                self.myLabel.setPixmap(self.myMaps[13])
            else:
                self.myLabel.setPixmap(self.myMaps[12])


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    device1 = 1
    device2 = 2
    device3 = 3
    device4 = 1
    if Ui_MainWindow.isValidCombo(device1, device2, device3, device4):
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow, device1, device2, device3, device4)
        MainWindow.show()
    sys.exit(app.exec_())



