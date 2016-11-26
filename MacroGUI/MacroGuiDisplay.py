#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def main():
    # Create an PyQT4 application object.
    a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
    w = QMainWindow()
    wid = QWidget()
    w.setCentralWidget(wid)

    silver_canvas = QLabel()

    silver_canvas.setScaledContents(True)
    silver_canvas.setAlignment(Qt.AlignCenter)
    silver_canvas.setPixmap(QPixmap("ui_images\canvas_black.png"))
    vbox = QVBoxLayout()
    vbox.addWidget(silver_canvas)

    wid.setLayout(vbox)

    # Set window title
    w.setWindowTitle("Network Simulation!")
    w.setGeometry(20,20,100,100)

    # Create main menu
    mainMenu = w.menuBar()
    mainMenu.setNativeMenuBar(False)
    fileMenu = mainMenu.addMenu('&File')

# Add exit button
    exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
    exitButton.setShortcut('Ctrl+Q')
    exitButton.setStatusTip('Exit application')
    exitButton.triggered.connect(w.close)

    menubar = w.menuBar()

    exitMenu = menubar.addMenu('&Exit')
# Adds option to the exit menu on the menubar
    exitMenu.addAction(exitButton)

# Adds a menu that can have actions added to it
    fileMenu = menubar.addMenu('&File')
#fileMenu.addAction(printAction)

    menubar.addMenu('&Edit')
    menubar.addMenu('&View')
    menubar.addMenu('&?')
    menubar.addMenu('&Tool')

    # Show window
    w.show()
    sys.exit(a.exec_())

if __name__ == "__main__":
    main()