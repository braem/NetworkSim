# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageInfoWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtCore import *
from PyQt4.QtGui import *

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

class MessageInfo_Window(QMainWindow):
    protocol_stack = ["Application", "Transport", "Network", "Link"]
    messageNum = 0

    def __init__(self, holder, layer_designator):
        super(MessageInfo_Window, self).__init__(holder)

        self.messageList = ["Hello, how are you?", "I am doing fine. Did you need something?",
                            "Lewis structures (also known as Lewis dot diagrams, Lewis dot formulas, Lewis dot "
                            "structures, and electron dot structures) are diagrams that show the bonding between "
                            "atoms of a molecule and the lone pairs of electrons that may exist in the molecule. "
                            "A Lewis structure can be drawn for any covalently bonded molecule, as well as "
                            "coordination compounds. The Lewis structure was named after Gilbert N. Lewis, who "
                            "introduced it in his 1916 article The Atom and the Molecule.[4] Lewis structures extend "
                            "the concept of the electron dot diagram by adding lines between atoms to represent "
                            "shared pairs in a chemical bond. Lewis structures show each atom and its position in "
                            "the structure of the molecule using its chemical symbol. Lines are drawn between atoms "
                            "that are bonded to one another (pairs of dots can be used instead of lines). Excess "
                            "electrons that form lone pairs are represented as pairs of dots, and are placed next to "
                            "the atoms. Although main group elements of the second period and beyond usually react "
                            "by gaining, losing, or sharing electrons until they have achieved a valence shell "
                            "electron configuration with a full octet of (8) electrons, other elements obey different "
                            "rules. Hydrogen (H) can only form bonds which share just two electrons, while transition "
                            "metals often conform to a duodectet (12)."]
        self.tcpSourceList = ["231456", "5521", "231456"]
        self.tcpDestList = ["5521", "231456", "5521"]
        self.tcpSeqnumList = ["154020", "21546", "35489"]
        self.tcpAcknumList = ["57742", "9825", "316547"]
        self.tcpDataList = ["5", "5", "5"]
        self.tcpReservedList = ["000", "000", "000"]
        self.tcpNSList = ["0", "0", "1"]
        self.tcpCWRList = ["0", "1", "0"]
        self.tcpECEList = ["0", "0", "0"]
        self.tcpURGList = ["1", "1", "1"]
        self.tcpACKList = ["0", "1", "0"]
        self.tcpPSHList = ["0", "0", "0"]
        self.tcpRSTList = ["0", "0", "1"]
        self.tcpSYNList = ["0", "1", "1"]
        self.tcpFINList = ["1", "0", "0"]
        self.tcpWindowList = ["65501", "124", "3578"]
        self.tcpChecksumList = ["2551", "2567", "742"]
        self.tcpUrgentList = ["1120", "35687", "12563"]
        self.ipVersionList = ["6", "6", "6"]
        self.ipTrafficList = ["125", "34", "250"]
        self.ipFlowList = ["11245", "32564", "75663"]
        self.ipPaylengthList = ["2435", "1125", "45378"]
        self.ipNextList = ["6", "6", "6"]
        self.ipHopList = ["21", "203", "35"]
        self.ipSourceList = ["2001:0db8:85a3:0000:0000:8a2e:0370:7334", "1560:0adb:0bad:aff9:0123:dead:0101:c1d4", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]
        self.ipDestList = ["1560:0adb:0bad:aff9:0123:dead:0101:c1d4", "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "1560:0adb:0bad:aff9:0123:dead:0101:c1d4"]


        # Store the layer designator with first letter capitalized
        self.layer = layer_designator.lower().capitalize()
        self.setupUi()

    def setupUi(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        if self.layer == MessageInfo_Window.protocol_stack[0]:
            self.resize(300, 350)
            self.messageFrame = QFrame(self.centralwidget)
            self.messageFrame.setGeometry(QRect(0, 0, 300, 20))
            self.messageFrame.setFrameShape(QFrame.StyledPanel)
            self.messageFrame.setFrameShadow(QFrame.Plain)
            self.messageFrame.setLineWidth(2)
            self.messageFrame.setObjectName(_fromUtf8("messageFrame"))
            self.messageLabel = QLabel(self.messageFrame)
            self.messageLabel.setGeometry(QRect(10, 0, 51, 16))
            self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
            self.messageTextBrowser = QTextBrowser(self.centralwidget)
            self.messageTextBrowser.setGeometry(QRect(0, 20, 300, 330))
            self.messageTextBrowser.setObjectName(_fromUtf8("messageTextBrowser"))
            self.messageTextBrowser.setText(self.messageList[2] + " " + self.messageList[2])
        elif self.layer == MessageInfo_Window.protocol_stack[1]:
            self.resize(500, 400)
            self.frame_11 = QFrame(self.centralwidget)
            self.frame_11.setGeometry(QRect(0, 0, 501, 401))
            self.frame_11.setFrameShape(QFrame.StyledPanel)
            self.frame_11.setFrameShadow(QFrame.Plain)
            self.frame_11.setObjectName(_fromUtf8("frame_11"))
            self.frame_12 = QFrame(self.frame_11)
            self.frame_12.setGeometry(QRect(0, 0, 501, 21))
            self.frame_12.setFrameShape(QFrame.StyledPanel)
            self.frame_12.setFrameShadow(QFrame.Plain)
            self.frame_12.setObjectName(_fromUtf8("frame_12"))
            self.label_11 = QLabel(self.frame_12)
            self.label_11.setGeometry(QRect(10, 0, 111, 16))
            self.label_11.setObjectName(_fromUtf8("label_11"))
            self.frame_13 = QFrame(self.frame_11)
            self.frame_13.setGeometry(QRect(0, 20, 251, 21))
            self.frame_13.setFrameShape(QFrame.StyledPanel)
            self.frame_13.setFrameShadow(QFrame.Plain)
            self.frame_13.setObjectName(_fromUtf8("frame_13"))
            self.label_26 = QLabel(self.frame_13)
            self.label_26.setGeometry(QRect(10, 0, 121, 16))
            self.label_26.setObjectName(_fromUtf8("label_26"))
            self.frame_14 = QFrame(self.frame_11)
            self.frame_14.setGeometry(QRect(250, 20, 251, 21))
            self.frame_14.setFrameShape(QFrame.StyledPanel)
            self.frame_14.setFrameShadow(QFrame.Plain)
            self.frame_14.setObjectName(_fromUtf8("frame_14"))
            self.label_27 = QLabel(self.frame_14)
            self.label_27.setGeometry(QRect(10, 0, 111, 16))
            self.label_27.setObjectName(_fromUtf8("label_27"))
            self.tcpSourceTextBrowser = QTextBrowser(self.frame_11)
            self.tcpSourceTextBrowser.setGeometry(QRect(0, 40, 251, 31))
            self.tcpSourceTextBrowser.setObjectName(_fromUtf8("textBrowser_10"))
            self.tcpDestTextBrowser = QTextBrowser(self.frame_11)
            self.tcpDestTextBrowser.setGeometry(QRect(250, 40, 251, 31))
            self.tcpDestTextBrowser.setObjectName(_fromUtf8("textBrowser_11"))
            self.frame_15 = QFrame(self.frame_11)
            self.frame_15.setGeometry(QRect(0, 70, 251, 21))
            self.frame_15.setFrameShape(QFrame.StyledPanel)
            self.frame_15.setFrameShadow(QFrame.Plain)
            self.frame_15.setObjectName(_fromUtf8("frame_15"))
            self.label_28 = QLabel(self.frame_15)
            self.label_28.setGeometry(QRect(10, 0, 181, 16))
            self.label_28.setObjectName(_fromUtf8("label_28"))
            self.tcpSequenceTextBrowser = QTextBrowser(self.frame_11)
            self.tcpSequenceTextBrowser.setGeometry(QRect(0, 90, 251, 31))
            self.tcpSequenceTextBrowser.setObjectName(_fromUtf8("textBrowser_12"))
            self.frame_17 = QFrame(self.frame_11)
            self.frame_17.setGeometry(QRect(0, 120, 81, 21))
            self.frame_17.setFrameShape(QFrame.StyledPanel)
            self.frame_17.setFrameShadow(QFrame.Plain)
            self.frame_17.setObjectName(_fromUtf8("frame_17"))
            self.label_22 = QLabel(self.frame_17)
            self.label_22.setGeometry(QRect(10, 0, 71, 16))
            self.label_22.setObjectName(_fromUtf8("label_22"))
            self.frame_19 = QFrame(self.frame_11)
            self.frame_19.setGeometry(QRect(80, 120, 61, 21))
            self.frame_19.setFrameShape(QFrame.StyledPanel)
            self.frame_19.setFrameShadow(QFrame.Plain)
            self.frame_19.setObjectName(_fromUtf8("frame_19"))
            self.label_21 = QLabel(self.frame_19)
            self.label_21.setGeometry(QRect(10, 0, 46, 13))
            self.label_21.setObjectName(_fromUtf8("label_21"))
            self.frame_20 = QFrame(self.frame_11)
            self.frame_20.setGeometry(QRect(460, 120, 41, 21))
            self.frame_20.setFrameShape(QFrame.StyledPanel)
            self.frame_20.setFrameShadow(QFrame.Plain)
            self.frame_20.setObjectName(_fromUtf8("frame_20"))
            self.label_20 = QLabel(self.frame_20)
            self.label_20.setGeometry(QRect(10, 0, 31, 16))
            self.label_20.setObjectName(_fromUtf8("label_20"))
            self.frame_21 = QFrame(self.frame_11)
            self.frame_21.setGeometry(QRect(420, 120, 41, 21))
            self.frame_21.setFrameShape(QFrame.StyledPanel)
            self.frame_21.setFrameShadow(QFrame.Plain)
            self.frame_21.setObjectName(_fromUtf8("frame_21"))
            self.label_19 = QLabel(self.frame_21)
            self.label_19.setGeometry(QRect(10, 0, 31, 16))
            self.label_19.setObjectName(_fromUtf8("label_19"))
            self.frame_22 = QFrame(self.frame_11)
            self.frame_22.setGeometry(QRect(380, 120, 41, 21))
            self.frame_22.setFrameShape(QFrame.StyledPanel)
            self.frame_22.setFrameShadow(QFrame.Plain)
            self.frame_22.setObjectName(_fromUtf8("frame_22"))
            self.label_18 = QLabel(self.frame_22)
            self.label_18.setGeometry(QRect(10, 0, 31, 16))
            self.label_18.setObjectName(_fromUtf8("label_18"))
            self.frame_23 = QFrame(self.frame_11)
            self.frame_23.setGeometry(QRect(340, 120, 41, 21))
            self.frame_23.setFrameShape(QFrame.StyledPanel)
            self.frame_23.setFrameShadow(QFrame.Plain)
            self.frame_23.setObjectName(_fromUtf8("frame_23"))
            self.label_17 = QLabel(self.frame_23)
            self.label_17.setGeometry(QRect(10, 0, 31, 16))
            self.label_17.setObjectName(_fromUtf8("label_17"))
            self.frame_24 = QFrame(self.frame_11)
            self.frame_24.setGeometry(QRect(300, 120, 41, 21))
            self.frame_24.setFrameShape(QFrame.StyledPanel)
            self.frame_24.setFrameShadow(QFrame.Plain)
            self.frame_24.setObjectName(_fromUtf8("frame_24"))
            self.label_16 = QLabel(self.frame_24)
            self.label_16.setGeometry(QRect(10, 0, 31, 16))
            self.label_16.setObjectName(_fromUtf8("label_16"))
            self.frame_25 = QFrame(self.frame_11)
            self.frame_25.setGeometry(QRect(260, 120, 41, 21))
            self.frame_25.setFrameShape(QFrame.StyledPanel)
            self.frame_25.setFrameShadow(QFrame.Plain)
            self.frame_25.setObjectName(_fromUtf8("frame_25"))
            self.label_15 = QLabel(self.frame_25)
            self.label_15.setGeometry(QRect(10, 0, 31, 16))
            self.label_15.setObjectName(_fromUtf8("label_15"))
            self.frame_26 = QFrame(self.frame_11)
            self.frame_26.setGeometry(QRect(220, 120, 41, 21))
            self.frame_26.setFrameShape(QFrame.StyledPanel)
            self.frame_26.setFrameShadow(QFrame.Plain)
            self.frame_26.setObjectName(_fromUtf8("frame_26"))
            self.label_14 = QLabel(self.frame_26)
            self.label_14.setGeometry(QRect(10, 0, 31, 16))
            self.label_14.setObjectName(_fromUtf8("label_14"))
            self.frame_27 = QFrame(self.frame_11)
            self.frame_27.setGeometry(QRect(180, 120, 41, 21))
            self.frame_27.setFrameShape(QFrame.StyledPanel)
            self.frame_27.setFrameShadow(QFrame.Plain)
            self.frame_27.setObjectName(_fromUtf8("frame_27"))
            self.label_13 = QLabel(self.frame_27)
            self.label_13.setGeometry(QRect(10, 0, 31, 16))
            self.label_13.setObjectName(_fromUtf8("label_13"))
            self.frame_28 = QFrame(self.frame_11)
            self.frame_28.setGeometry(QRect(140, 120, 41, 21))
            self.frame_28.setFrameShape(QFrame.StyledPanel)
            self.frame_28.setFrameShadow(QFrame.Plain)
            self.frame_28.setObjectName(_fromUtf8("frame_28"))
            self.label_12 = QLabel(self.frame_28)
            self.label_12.setGeometry(QRect(10, 0, 21, 16))
            self.label_12.setObjectName(_fromUtf8("label_12"))
            self.tcpDataTextBrowser = QTextBrowser(self.frame_11)
            self.tcpDataTextBrowser.setGeometry(QRect(0, 140, 81, 31))
            self.tcpDataTextBrowser.setObjectName(_fromUtf8("textBrowser_14"))
            self.tcpReservedTextBrowser = QTextBrowser(self.frame_11)
            self.tcpReservedTextBrowser.setGeometry(QRect(80, 140, 61, 31))
            self.tcpReservedTextBrowser.setObjectName(_fromUtf8("textBrowser_15"))
            self.tcpNSTextBrowser = QTextBrowser(self.frame_11)
            self.tcpNSTextBrowser.setGeometry(QRect(140, 140, 41, 31))
            self.tcpNSTextBrowser.setObjectName(_fromUtf8("textBrowser_16"))
            self.tcpCWRTextBrowser = QTextBrowser(self.frame_11)
            self.tcpCWRTextBrowser.setGeometry(QRect(180, 140, 41, 31))
            self.tcpCWRTextBrowser.setObjectName(_fromUtf8("textBrowser_17"))
            self.tcpECETextBrowser = QTextBrowser(self.frame_11)
            self.tcpECETextBrowser.setGeometry(QRect(220, 140, 41, 31))
            self.tcpECETextBrowser.setObjectName(_fromUtf8("textBrowser_18"))
            self.tcpURGTextBrowser = QTextBrowser(self.frame_11)
            self.tcpURGTextBrowser.setGeometry(QRect(260, 140, 41, 31))
            self.tcpURGTextBrowser.setObjectName(_fromUtf8("textBrowser_19"))
            self.tcpACKTextBrowser = QTextBrowser(self.frame_11)
            self.tcpACKTextBrowser.setGeometry(QRect(300, 140, 41, 31))
            self.tcpACKTextBrowser.setObjectName(_fromUtf8("textBrowser_20"))
            self.tcpPSHTextBrowser = QTextBrowser(self.frame_11)
            self.tcpPSHTextBrowser.setGeometry(QRect(340, 140, 41, 31))
            self.tcpPSHTextBrowser.setObjectName(_fromUtf8("textBrowser_21"))
            self.tcpRSTTextBrowser = QTextBrowser(self.frame_11)
            self.tcpRSTTextBrowser.setGeometry(QRect(380, 140, 41, 31))
            self.tcpRSTTextBrowser.setObjectName(_fromUtf8("textBrowser_22"))
            self.tcpSYNTextBrowser = QTextBrowser(self.frame_11)
            self.tcpSYNTextBrowser.setGeometry(QRect(420, 140, 41, 31))
            self.tcpSYNTextBrowser.setObjectName(_fromUtf8("textBrowser_23"))
            self.tcpFINTextBrowser = QTextBrowser(self.frame_11)
            self.tcpFINTextBrowser.setGeometry(QRect(460, 140, 41, 31))
            self.tcpFINTextBrowser.setObjectName(_fromUtf8("textBrowser_24"))
            self.frame_16 = QFrame(self.frame_11)
            self.frame_16.setGeometry(QRect(250, 70, 251, 21))
            self.frame_16.setFrameShape(QFrame.StyledPanel)
            self.frame_16.setFrameShadow(QFrame.Plain)
            self.frame_16.setObjectName(_fromUtf8("frame_16"))
            self.label_29 = QLabel(self.frame_16)
            self.label_29.setGeometry(QRect(10, 0, 221, 16))
            self.label_29.setObjectName(_fromUtf8("label_29"))
            self.tcpAcknumTextBrowser = QTextBrowser(self.frame_11)
            self.tcpAcknumTextBrowser.setGeometry(QRect(250, 90, 251, 31))
            self.tcpAcknumTextBrowser.setObjectName(_fromUtf8("textBrowser_25"))
            self.frame_18 = QFrame(self.frame_11)
            self.frame_18.setGeometry(QRect(0, 170, 161, 21))
            self.frame_18.setFrameShape(QFrame.StyledPanel)
            self.frame_18.setFrameShadow(QFrame.Plain)
            self.frame_18.setObjectName(_fromUtf8("frame_18"))
            self.label_23 = QLabel(self.frame_18)
            self.label_23.setGeometry(QRect(10, 0, 71, 16))
            self.label_23.setObjectName(_fromUtf8("label_23"))
            self.frame_29 = QFrame(self.frame_11)
            self.frame_29.setGeometry(QRect(160, 170, 171, 21))
            self.frame_29.setFrameShape(QFrame.StyledPanel)
            self.frame_29.setFrameShadow(QFrame.Plain)
            self.frame_29.setObjectName(_fromUtf8("frame_29"))
            self.label_24 = QLabel(self.frame_29)
            self.label_24.setGeometry(QRect(10, 0, 91, 16))
            self.label_24.setObjectName(_fromUtf8("label_24"))
            self.frame_30 = QFrame(self.frame_11)
            self.frame_30.setGeometry(QRect(330, 170, 171, 21))
            self.frame_30.setFrameShape(QFrame.StyledPanel)
            self.frame_30.setFrameShadow(QFrame.Plain)
            self.frame_30.setObjectName(_fromUtf8("frame_30"))
            self.label_25 = QLabel(self.frame_30)
            self.label_25.setGeometry(QRect(10, 0, 81, 16))
            self.label_25.setObjectName(_fromUtf8("label_25"))
            self.tcpWindowTextBrowser = QTextBrowser(self.frame_11)
            self.tcpWindowTextBrowser.setGeometry(QRect(0, 190, 161, 31))
            self.tcpWindowTextBrowser.setObjectName(_fromUtf8("textBrowser_13"))
            self.tcpChecksumTextBrowser = QTextBrowser(self.frame_11)
            self.tcpChecksumTextBrowser.setGeometry(QRect(160, 190, 171, 31))
            self.tcpChecksumTextBrowser.setObjectName(_fromUtf8("textBrowser_26"))
            self.tcpUrgentTextBrowser = QTextBrowser(self.frame_11)
            self.tcpUrgentTextBrowser.setGeometry(QRect(330, 190, 171, 31))
            self.tcpUrgentTextBrowser.setObjectName(_fromUtf8("textBrowser_27"))
            self.frame_31 = QFrame(self.frame_11)
            self.frame_31.setGeometry(QRect(0, 220, 501, 21))
            self.frame_31.setFrameShape(QFrame.StyledPanel)
            self.frame_31.setFrameShadow(QFrame.Plain)
            self.frame_31.setObjectName(_fromUtf8("frame_31"))
            self.label_30 = QLabel(self.frame_31)
            self.label_30.setGeometry(QRect(10, 0, 46, 13))
            self.label_30.setObjectName(_fromUtf8("label_30"))
            self.tcpPayloadTextBrowser = QTextBrowser(self.frame_11)
            self.tcpPayloadTextBrowser.setGeometry(QRect(0, 240, 501, 161))
            self.tcpPayloadTextBrowser.setObjectName(_fromUtf8("textBrowser_28"))
        elif self.layer == MessageInfo_Window.protocol_stack[2]:
            self.resize(410, 400)
            self.ipFrame = QFrame(self.centralwidget)
            self.ipFrame.setGeometry(QRect(0, 0, 411, 401))
            self.ipFrame.setFrameShape(QFrame.StyledPanel)
            self.ipFrame.setFrameShadow(QFrame.Plain)
            self.ipFrame.setObjectName(_fromUtf8("ipFrame"))
            self.ipLabel = QLabel(self.ipFrame)
            self.ipLabel.setGeometry(QRect(10, 0, 81, 16))
            self.ipLabel.setObjectName(_fromUtf8("ipLabel"))
            self.ipVersionFrame = QFrame(self.ipFrame)
            self.ipVersionFrame.setGeometry(QRect(0, 20, 61, 21))
            self.ipVersionFrame.setFrameShape(QFrame.StyledPanel)
            self.ipVersionFrame.setFrameShadow(QFrame.Plain)
            self.ipVersionFrame.setObjectName(_fromUtf8("ipVersionFrame"))
            self.ipVersionLabel = QLabel(self.ipVersionFrame)
            self.ipVersionLabel.setGeometry(QRect(10, 0, 46, 13))
            self.ipVersionLabel.setObjectName(_fromUtf8("ipVersionLabel"))
            self.ipVersionTextBrowser = QTextBrowser(self.ipFrame)
            self.ipVersionTextBrowser.setGeometry(QRect(0, 40, 61, 31))
            self.ipVersionTextBrowser.setObjectName(_fromUtf8("ipVersionTextBrowser"))
            self.ipTrafficFrame = QFrame(self.ipFrame)
            self.ipTrafficFrame.setGeometry(QRect(60, 20, 101, 21))
            self.ipTrafficFrame.setFrameShape(QFrame.StyledPanel)
            self.ipTrafficFrame.setFrameShadow(QFrame.Plain)
            self.ipTrafficFrame.setObjectName(_fromUtf8("ipTrafficFrame"))
            self.ipTrafficLabel = QLabel(self.ipTrafficFrame)
            self.ipTrafficLabel.setGeometry(QRect(10, 0, 81, 16))
            self.ipTrafficLabel.setObjectName(_fromUtf8("ipTrafficLabel"))
            self.ipTrafficTextBrowser = QTextBrowser(self.ipFrame)
            self.ipTrafficTextBrowser.setGeometry(QRect(60, 40, 101, 31))
            self.ipTrafficTextBrowser.setObjectName(_fromUtf8("ipTrafficTextBrowser"))
            self.ipFlowFrame = QFrame(self.ipFrame)
            self.ipFlowFrame.setGeometry(QRect(160, 20, 251, 21))
            self.ipFlowFrame.setFrameShape(QFrame.StyledPanel)
            self.ipFlowFrame.setFrameShadow(QFrame.Plain)
            self.ipFlowFrame.setObjectName(_fromUtf8("ipFlowFrame"))
            self.ipFlowLabel = QLabel(self.ipFlowFrame)
            self.ipFlowLabel.setGeometry(QRect(10, 0, 141, 16))
            self.ipFlowLabel.setObjectName(_fromUtf8("label_4"))
            self.ipFlowTextBrowser = QTextBrowser(self.ipFrame)
            self.ipFlowTextBrowser.setGeometry(QRect(160, 40, 256, 31))
            self.ipFlowTextBrowser.setObjectName(_fromUtf8("ipFlowTextBrowser"))
            self.ipPaylengthFrame = QFrame(self.ipFrame)
            self.ipPaylengthFrame.setGeometry(QRect(0, 70, 221, 21))
            self.ipPaylengthFrame.setFrameShape(QFrame.StyledPanel)
            self.ipPaylengthFrame.setFrameShadow(QFrame.Plain)
            self.ipPaylengthFrame.setObjectName(_fromUtf8("ipPaylengthFrame"))
            self.ipPaylengthLabel = QLabel(self.ipPaylengthFrame)
            self.ipPaylengthLabel.setGeometry(QRect(10, 0, 91, 16))
            self.ipPaylengthLabel.setObjectName(_fromUtf8("ipPaylengthLabel"))
            self.ipPaylengthTextBrowser = QTextBrowser(self.ipFrame)
            self.ipPaylengthTextBrowser.setGeometry(QRect(0, 90, 221, 31))
            self.ipPaylengthTextBrowser.setObjectName(_fromUtf8("ipPaylengthTextBrowser"))
            self.ipNextFrame = QFrame(self.ipFrame)
            self.ipNextFrame.setGeometry(QRect(220, 70, 101, 21))
            self.ipNextFrame.setFrameShape(QFrame.StyledPanel)
            self.ipNextFrame.setFrameShadow(QFrame.Plain)
            self.ipNextFrame.setObjectName(_fromUtf8("frame_6"))
            self.ipNextLabel = QLabel(self.ipNextFrame)
            self.ipNextLabel.setGeometry(QRect(10, 0, 71, 16))
            self.ipNextLabel.setObjectName(_fromUtf8("label_6"))
            self.ipNextTextBrowser = QTextBrowser(self.ipFrame)
            self.ipNextTextBrowser.setGeometry(QRect(220, 90, 101, 31))
            self.ipNextTextBrowser.setObjectName(_fromUtf8("textBrowser_5"))
            self.ipHopFrame = QFrame(self.ipFrame)
            self.ipHopFrame.setGeometry(QRect(320, 70, 91, 21))
            self.ipHopFrame.setFrameShape(QFrame.StyledPanel)
            self.ipHopFrame.setFrameShadow(QFrame.Plain)
            self.ipHopFrame.setObjectName(_fromUtf8("frame_7"))
            self.ipHopLabel = QLabel(self.ipHopFrame)
            self.ipHopLabel.setGeometry(QRect(10, 0, 61, 16))
            self.ipHopLabel.setObjectName(_fromUtf8("label_7"))
            self.ipHopTextBrowser = QTextBrowser(self.ipFrame)
            self.ipHopTextBrowser.setGeometry(QRect(320, 90, 91, 31))
            self.ipHopTextBrowser.setObjectName(_fromUtf8("textBrowser_6"))
            self.ipSourceFrame = QFrame(self.ipFrame)
            self.ipSourceFrame.setGeometry(QRect(0, 120, 411, 21))
            self.ipSourceFrame.setFrameShape(QFrame.StyledPanel)
            self.ipSourceFrame.setFrameShadow(QFrame.Plain)
            self.ipSourceFrame.setObjectName(_fromUtf8("frame_8"))
            self.ipSourceLabel = QLabel(self.ipSourceFrame)
            self.ipSourceLabel.setGeometry(QRect(10, 0, 131, 16))
            self.ipSourceLabel.setObjectName(_fromUtf8("label_8"))
            self.ipSourceTextBrowser = QTextBrowser(self.ipFrame)
            self.ipSourceTextBrowser.setGeometry(QRect(0, 140, 411, 31))
            self.ipSourceTextBrowser.setObjectName(_fromUtf8("textBrowser_7"))
            self.ipDestFrame = QFrame(self.ipFrame)
            self.ipDestFrame.setGeometry(QRect(0, 170, 411, 21))
            self.ipDestFrame.setFrameShape(QFrame.StyledPanel)
            self.ipDestFrame.setFrameShadow(QFrame.Plain)
            self.ipDestFrame.setObjectName(_fromUtf8("frame_9"))
            self.ipDestLabel = QLabel(self.ipDestFrame)
            self.ipDestLabel.setGeometry(QRect(10, 0, 161, 16))
            self.ipDestLabel.setObjectName(_fromUtf8("label_9"))
            self.ipDestTextBrowser = QTextBrowser(self.ipFrame)
            self.ipDestTextBrowser.setGeometry(QRect(0, 190, 411, 31))
            self.ipDestTextBrowser.setObjectName(_fromUtf8("textBrowser_8"))
            self.ipPayloadFrame = QFrame(self.ipFrame)
            self.ipPayloadFrame.setGeometry(QRect(0, 220, 411, 21))
            self.ipPayloadFrame.setFrameShape(QFrame.StyledPanel)
            self.ipPayloadFrame.setFrameShadow(QFrame.Plain)
            self.ipPayloadFrame.setObjectName(_fromUtf8("frame_10"))
            self.ipPayloadLabel = QLabel(self.ipPayloadFrame)
            self.ipPayloadLabel.setGeometry(QRect(10, 0, 121, 16))
            self.ipPayloadLabel.setObjectName(_fromUtf8("label_10"))
            self.ipPayloadTextBrowser = QTextBrowser(self.ipFrame)
            self.ipPayloadTextBrowser.setGeometry(QRect(0, 240, 411, 161))
            self.ipPayloadTextBrowser.setObjectName(_fromUtf8("textBrowser_9"))

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        self.setupMessage()
        self.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Info", None))
        if self.layer == MessageInfo_Window.protocol_stack[0]:
            self.messageLabel.setText(_translate("MainWindow", "Message:", None))
        elif self.layer == MessageInfo_Window.protocol_stack[1]:
            self.label_11.setText(_translate("MainWindow", "TCP Header", None))
            self.label_26.setText(_translate("MainWindow", "Source Port", None))
            self.label_27.setText(_translate("MainWindow", "Destination Port", None))
            self.label_28.setText(_translate("MainWindow", "Sequence Number", None))
            self.label_22.setText(_translate("MainWindow", "Data Offset", None))
            self.label_21.setText(_translate("MainWindow", "Reserved", None))
            self.label_20.setText(_translate("MainWindow", "FIN", None))
            self.label_19.setText(_translate("MainWindow", "SYN", None))
            self.label_18.setText(_translate("MainWindow", "RST", None))
            self.label_17.setText(_translate("MainWindow", "PSH", None))
            self.label_16.setText(_translate("MainWindow", "ACK", None))
            self.label_15.setText(_translate("MainWindow", "URG", None))
            self.label_14.setText(_translate("MainWindow", "ECE", None))
            self.label_13.setText(_translate("MainWindow", "CWR", None))
            self.label_12.setText(_translate("MainWindow", "NS", None))
            self.label_29.setText(_translate("MainWindow", "Acknowledgment Number", None))
            self.label_23.setText(_translate("MainWindow", "Window Size", None))
            self.label_24.setText(_translate("MainWindow", "Checksum", None))
            self.label_25.setText(_translate("MainWindow", "Urgent Pointer", None))
            self.label_30.setText(_translate("MainWindow", "Payload", None))
        elif self.layer == MessageInfo_Window.protocol_stack[2]:
            self.ipLabel.setText(_translate("MainWindow", "IP Header", None))
            self.ipVersionLabel.setText(_translate("MainWindow", "Version", None))
            self.ipTrafficLabel.setText(_translate("MainWindow", "Traffic Control", None))
            self.ipFlowLabel.setText(_translate("MainWindow", "Flow Label", None))
            self.ipPaylengthLabel.setText(_translate("MainWindow", "Payload length", None))
            self.ipNextLabel.setText(_translate("MainWindow", "Next Header", None))
            self.ipHopLabel.setText(_translate("MainWindow", "Hop Limit", None))
            self.ipSourceLabel.setText(_translate("MainWindow", "Source Address", None))
            self.ipDestLabel.setText(_translate("MainWindow", "Destination Address", None))
            self.ipPayloadLabel.setText(_translate("MainWindow", "Payload", None))

    def setupMessage(self):
        i = MessageInfo_Window.messageNum
        if i > 2:
            i = 2
        if self.layer == MessageInfo_Window.protocol_stack[0]:
            self.messageTextBrowser.setText(self.messageList[i])
        elif self.layer == MessageInfo_Window.protocol_stack[1]:
            self.tcpSourceTextBrowser.setText(self.tcpSourceList[i])
            self.tcpDestTextBrowser.setText(self.tcpDestList[i])
            self.tcpSequenceTextBrowser.setText(self.tcpSeqnumList[i])
            self.tcpAcknumTextBrowser.setText(self.tcpAcknumList[i])
            self.tcpDataTextBrowser.setText(self.tcpDataList[i])
            self.tcpReservedTextBrowser.setText(self.tcpReservedList[i])
            self.tcpNSTextBrowser.setText(self.tcpNSList[i])
            self.tcpCWRTextBrowser.setText(self.tcpCWRList[i])
            self.tcpECETextBrowser.setText(self.tcpECEList[i])
            self.tcpURGTextBrowser.setText(self.tcpURGList[i])
            self.tcpACKTextBrowser.setText(self.tcpACKList[i])
            self.tcpPSHTextBrowser.setText(self.tcpPSHList[i])
            self.tcpRSTTextBrowser.setText(self.tcpRSTList[i])
            self.tcpSYNTextBrowser.setText(self.tcpSYNList[i])
            self.tcpFINTextBrowser.setText(self.tcpFINList[i])
            self.tcpWindowTextBrowser.setText(self.tcpWindowList[i])
            self.tcpChecksumTextBrowser.setText(self.tcpChecksumList[i])
            self.tcpUrgentTextBrowser.setText(self.tcpUrgentList[i])
            self.tcpPayloadTextBrowser.setText(self.messageList[i])
        elif self.layer == MessageInfo_Window.protocol_stack[2]:
            self.ipVersionTextBrowser.setText(self.ipVersionList[i])
            self.ipTrafficTextBrowser.setText(self.ipTrafficList[i])
            self.ipFlowTextBrowser.setText(self.ipFlowList[i])
            self.ipPaylengthTextBrowser.setText(self.ipPaylengthList[i])
            self.ipNextTextBrowser.setText(self.ipNextList[i])
            self.ipHopTextBrowser.setText(self.ipHopList[i])
            self.ipSourceTextBrowser.setText(self.ipSourceList[i])
            self.ipDestTextBrowser.setText(self.ipDestList[i])
            self.ipPayloadTextBrowser.setText(self.tcpSourceList[i]+","+self.tcpDestList[i]+","+self.tcpSeqnumList[i]+
                                              ","+self.tcpAcknumList[i]+","+self.tcpDataList[i]+","+
                                              self.tcpReservedList[i]+","+self.tcpNSList[i]+","+self.tcpCWRList[i]+
                                              ","+self.tcpECEList[i]+","+self.tcpURGList[i]+","+self.tcpACKList[i]+
                                              ","+self.tcpPSHList[i]+","+self.tcpRSTList[i]+","+self.tcpSYNList[i]+
                                              ","+self.tcpFINList[i]+","+self.tcpWindowList[i]+","+
                                              self.tcpChecksumList[i]+","+self.tcpUrgentList[i]+","+self.messageList[i])

    @staticmethod
    def nextMessage():
        MessageInfo_Window.messageNum += 1

