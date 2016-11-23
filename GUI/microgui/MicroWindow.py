# Micro view GUI for CPSC 444 project
#
# Author: Lukas Pihl

import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Connection import *
from Node import *

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class Values():
    buttonHeight = 51
    buttonWidth = 121
    labelHeight = 31
    graphicWidth = 111
    windHeight = 600
    windWidth = 1000


class MicroMainWindow(QMainWindow):

    def __init__(self, con1, con2, con3):
        super(MicroMainWindow, self).__init__()

        self.validFlag = False
        self.conList = []
        self.deviceList = []
        self.lineList = []
        self.central_widget = None
        self.list_size = 0

        self.setup(con1, con2, con3)

    def setup(self, con1, con2, con3):

        # get list of devices
        temp_device_list = [con1.nodes[0], con1.nodes[1], None, None]
        self.list_size = 2
        self.conList.append(con1)
        if con2 is not None:
            temp_device_list[2] = con2.nodes[1]
            self.conList.append(con2)
            self.list_size += 1
        if con3 is not None:
            temp_device_list[3] = con3.nodes[1]
            self.conList.append(con3)
            self.list_size += 1

        # Setup window
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(Values.windWidth, Values.windHeight)
        self.central_widget = QWidget(self)
        self.central_widget.setObjectName(_fromUtf8("central_widget"))

        # Setup Window
        total_width = (4 + MicroGraphicsLabel.myWidth) * (self.list_size - 1)
        for i in range(0, self.list_size):
            total_width += MicroHostFrame.myWidth

        # Setup device frames
        for i in range(0, self.list_size):
            temp_offset = 0
            for j in range(i, self.list_size):
                temp_offset += MicroHostFrame.myWidth
                if j != self.list_size-1:
                    temp_offset += MicroGraphicsLabel.myWidth + 2
            pos_x = Values.windWidth/2 + total_width/2 - temp_offset
            pos_y = Values.windHeight/2 - MicroHostFrame.myHeight / 2 + (MicroHostFrame.myHeight -
                                                                         self.getDeviceHeight(temp_device_list[i]))
            self.deviceList.append(self.makeDevicePanel(temp_device_list[i], pos_x, pos_y))

        # Setup graphic labels
        for i in range(0, self.list_size-1):
            temp_offset = 0
            for j in range(i, self.list_size-1):
                temp_offset += MicroHostFrame.getWidth() + MicroGraphicsLabel.getWidth() + 2
                pos_x = Values.windWidth/2 + total_width/2 - temp_offset
                pos_y = Values.windHeight/2 - MicroHostFrame.myHeight / 2 + (MicroHostFrame.myHeight -
                                                                             MicroGraphicsLabel.getHeight())
                self.lineList.append(self.makeLine(temp_device_list[i], temp_device_list[i+1], pos_x, pos_y))

        # Show components
        for i in self.deviceList:
            i.show()
        for i in self.lineList:
            i.show()

        self.validFlag = True

        self.setCentralWidget(self.central_widget)
        self.retranslateUi(self)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("MainWindow", "Micro View", None))
        if self.isvalid():
            for i in self.deviceList:
                i.retranslateUi()

    def isvalid(self):
        return self.validFlag

    @staticmethod
    def isValidCombo(device1, device2, device3, device4):
        # TODO replace ints with proper classes
        # 1 = Host, 2 = Router, 3 = Switch
        # Check that first and second devices are not invalid
        if device1 is None or not isinstance(device1, Host) or device2 is None:
            return False
        # If device 2 is a host, check that devices 3 & 4 are not used
        if isinstance(device2, Host):
            if device3 is not None or device4 is not None:
                return False
            return True
        # If device 2 is not a host
        # Check if device 3 is invalid
        if device3 is None:
            return False
        # If device 3 is a host, check that device 4 is not used and device 2 is a router
        if isinstance(device3, Host):
            if not isinstance(device2, Router) or device4 is not None:
                return False
            return True
        # Check device 2 and 3 are not the same
        if isinstance(device2, Router) and isinstance(device3, Router):
            return False
        if isinstance(device2, Switch) and isinstance(device3, Switch):
            return False
        # If device 3 is not a host
        # Check is device 4 is a host
        if isinstance(device4, Host):
            return True
        return False

    def getDeviceHeight(self, device):
        if isinstance(device, Host):
            return MicroHostFrame.myHeight
        if isinstance(device, Router):
            return MicroRouterFrame.myHeight
        if isinstance(device, Switch):
            return MicroSwitchFrame.myHeight
        return 0

    def makeDevicePanel(self, device, pos_x, pos_y):
        if isinstance(device, Host):
            frame = MicroHostFrame(self.central_widget, device, pos_x, pos_y)
            return frame
        if isinstance(device, Router):
            frame = MicroRouterFrame(self.central_widget, device, pos_x, pos_y)
            return frame
        if isinstance(device, Switch):
            frame = MicroSwitchFrame(self.central_widget, device, pos_x, pos_y)
            return frame

    def makeLine(self, device_left, device_right, pos_x, pos_y):
        label = MicroGraphicsLabel(self.central_widget, device_left, device_right, pos_x, pos_y)
        return label

    def update(self):
        None
        # If connection 1 in use, activate line[0]
        # If connection 2 in use, activate line[1]
        # If connection 3 in use, activate line[2]


class MicroHostFrame(QFrame):
    myHeight = Values.buttonHeight*5+Values.labelHeight-5
    myWidth = Values.buttonWidth

    def __init__(self, holder, device, pos_x, pos_y):
        super(MicroHostFrame, self).__init__(holder)

        self.myDevice = device
        self.btnHostA = QPushButton(self)
        self.btnHostT = QPushButton(self)
        self.btnHostN = QPushButton(self)
        self.btnHostL = QPushButton(self)
        self.btnHostP = QPushButton(self)
        self.lblHost = QLabel(self)

        self.setup(pos_x, pos_y)

    def setup(self, pos_x, pos_y):
        self.setGeometry(QRect(pos_x, pos_y, MicroHostFrame.myWidth, MicroHostFrame.myHeight))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName(_fromUtf8("frameHost"))
        self.btnHostA.setGeometry(QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnHostA.setObjectName(_fromUtf8("btnHostA"))
        self.btnHostA.clicked.connect(self.clickedButton_Application)
        self.btnHostT.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth, Values.buttonHeight))
        self.btnHostT.setObjectName(_fromUtf8("btnHostT"))
        self.btnHostT.clicked.connect(self.clickedButton_Transport)
        self.btnHostN.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight*2-3, Values.buttonWidth, Values.buttonHeight))
        self.btnHostN.setObjectName(_fromUtf8("btnHostN"))
        self.btnHostN.clicked.connect(self.clickedButton_Network)
        self.btnHostL.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight*3-4, Values.buttonWidth, Values.buttonHeight))
        self.btnHostL.setObjectName(_fromUtf8("btnHostL"))
        self.btnHostL.clicked.connect(self.clickedButton_Link)
        self.btnHostP.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight*4-5, Values.buttonWidth, Values.buttonHeight))
        self.btnHostP.setObjectName(_fromUtf8("btnHostP"))
        self.lblHost.setGeometry(QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblHost.setAlignment(Qt.AlignCenter)
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
        return MicroHostFrame.myHeight

    @staticmethod
    def getWidth():
        return MicroHostFrame.myWidth

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


class MicroRouterFrame(QFrame):
    myHeight = Values.buttonHeight*3+Values.labelHeight-3
    myWidth = Values.buttonWidth

    def __init__(self, holder, device, pos_x, pos_y):
        super(MicroRouterFrame, self).__init__(holder)

        self.myDevice = device
        self.btnRouterN = QPushButton(self)
        self.btnRouterL = QPushButton(self)
        self.btnRouterP = QPushButton(self)
        self.lblRouter = QLabel(self)

        self.setup(pos_x, pos_y)

    def setup(self, pos_x, pos_y):
        self.setGeometry(QRect(pos_x, pos_y, MicroRouterFrame.myWidth, MicroRouterFrame.myHeight))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName(_fromUtf8("frameRouter"))

        self.btnRouterN.setGeometry(QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnRouterN.setObjectName(_fromUtf8("btnRouterN"))
        self.btnRouterN.clicked.connect(self.clickedButton_Network)
        self.btnRouterL.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth,
                                          Values.buttonHeight))
        self.btnRouterL.setObjectName(_fromUtf8("btnRouterL"))
        self.btnRouterL.clicked.connect(self.clickedButton_Link)
        self.btnRouterP.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight*2-3, Values.buttonWidth,
                                          Values.buttonHeight))
        self.btnRouterP.setObjectName(_fromUtf8("btnRouterP"))
        self.lblRouter.setGeometry(QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblRouter.setAlignment(Qt.AlignCenter)
        self.lblRouter.setObjectName(_fromUtf8("lblRouter"))

    def retranslateUi(self):
        self.btnRouterN.setText(_translate("RouterFrame", "Network", None))
        self.btnRouterL.setText(_translate("RouterFrame", "Link", None))
        self.btnRouterP.setText(_translate("RouterFrame", "Physical", None))
        self.lblRouter.setText(_translate("RouterFrame", "Router Name", None))

    @staticmethod
    def getHeight():
        return MicroHostFrame.myHeight

    @staticmethod
    def getWidth():
        return MicroHostFrame.myWidth

    def clickedButton_Network(self):
        print "Network"
        # TODO Open Network message window

    def clickedButton_Link(self):
        print "Link"
        # TODO Open Link message window


class MicroSwitchFrame(QFrame):
    myHeight = Values.buttonHeight*2+Values.labelHeight-2
    myWidth = Values.buttonWidth

    def __init__(self, holder, device, pos_x, pos_y):
        super(MicroSwitchFrame, self).__init__(holder)

        self.myDevice = device
        self.btnSwitchL = QPushButton(self)
        self.btnSwitchP = QPushButton(self)
        self.lblSwitch = QLabel(self)

        self.setup(pos_x, pos_y)

    def setup(self, pos_x, pos_y):
        self.setGeometry(QRect(pos_x, pos_y, MicroSwitchFrame.myWidth, MicroSwitchFrame.myHeight))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName(_fromUtf8("frameSwitch"))
        self.btnSwitchL.setGeometry(QRect(0, Values.labelHeight-1, Values.buttonWidth, Values.buttonHeight))
        self.btnSwitchL.setObjectName(_fromUtf8("btnSwitchL"))
        self.btnSwitchL.clicked.connect(self.clickedButton_Link)
        self.btnSwitchP.setGeometry(QRect(0, Values.labelHeight+Values.buttonHeight-2, Values.buttonWidth, Values.buttonHeight))
        self.btnSwitchP.setObjectName(_fromUtf8("btnSwitchP"))
        self.lblSwitch.setGeometry(QRect(0, 0, Values.buttonWidth, Values.labelHeight))
        self.lblSwitch.setAlignment(Qt.AlignCenter)
        self.lblSwitch.setObjectName(_fromUtf8("lblSwitch"))

    def retranslateUi(self):
        self.btnSwitchL.setText(_translate("SwitchFrame", "Link", None))
        self.btnSwitchP.setText(_translate("SwitchFrame", "Physical", None))
        self.lblSwitch.setText(_translate("SwitchFrame", "Switch Name", None))

    @staticmethod
    def getHeight():
        return MicroHostFrame.myHeight

    @staticmethod
    def getWidth():
        return MicroHostFrame.myWidth

    def clickedButton_Link(self):
        print "Link"
        # TODO Open Link message window


class MicroGraphicsLabel(QLabel):
    myHeight = Values.buttonHeight*5-5
    myWidth = Values.graphicWidth

    def __init__(self, holder, device_left, device_right, pos_x, pos_y):
        super(MicroGraphicsLabel, self).__init__(holder)

        self.myType = 0
        self.active = False
        self.myMaps = []

        self.setup(device_left, device_right, pos_x, pos_y)

    def setup(self, leftDevice, rightDevice, posX, posY):
        self.setGeometry(posX, posY, MicroGraphicsLabel.myWidth, MicroGraphicsLabel.myHeight)
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
            self.setPixmap(self.myMaps[0])
        elif self.myType == 12:
            self.setPixmap(self.myMaps[2])
        elif self.myType == 13:
            self.setPixmap(self.myMaps[4])
        elif self.myType == 21:
            self.setPixmap(self.myMaps[6])
        elif self.myType == 23:
            self.setPixmap(self.myMaps[8])
        elif self.myType == 31:
            self.setPixmap(self.myMaps[10])
        elif self.myType == 32:
            self.setPixmap(self.myMaps[12])
        self.setAlignment(Qt.AlignBottom)
        self.myLabel = self

    def buildMap(self, path):
        this_map = QPixmap(path)
        return this_map

    @staticmethod
    def getHeight():
        return MicroGraphicsLabel.myHeight

    @staticmethod
    def getWidth():
        return MicroGraphicsLabel.myWidth

    def setActive(self, state):
        self.active = state
        self.updateStatus()

    def getType(self, device_left, device_right):
        if isinstance(device_left, Host):
            if isinstance(device_right, Host):
                return 11
            if isinstance(device_right, Router):
                return 12
            if isinstance(device_right, Switch):
                return 13
        if isinstance(device_left, Router):
            if isinstance(device_right, Host):
                return 21
            if isinstance(device_right, Switch):
                return 23
        if isinstance(device_left, Switch):
            if isinstance(device_right, Host):
                return 31
            if isinstance(device_right, Router):
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
    app = QApplication(sys.argv)
    host1 = Host()
    host2 = Host()
    router = Router()
    switch = Switch()
    con1 = Connection(host1, router, None)
    con2 = Connection(router, switch, None)
    con3 = Connection(switch, host2, None)
    ui = MicroMainWindow(con1, con2, con3)
    ui.show()
    sys.exit(app.exec_())



