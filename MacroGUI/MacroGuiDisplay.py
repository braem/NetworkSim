#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from myTools.ToolWidget import TableFunction

def one():
    print 'arrow button'

def two():
    print 'x button'

def three():
    print 'pc button'

def main():
    # Create an PyQT4 application object.
    a = QApplication(sys.argv)

    #Creates a widget wilth buttons
    toolBar = TableFunction.createWidget2(1)
# The QWidget widget is the base class of all user interface objects in PyQt4.
    mainWindow = QMainWindow()


    backgroundWidget = QWidget()
    #backgroundWidget.lower()
    mainWindow.setCentralWidget(backgroundWidget)
    #palette = QPalette()
    #palette.setBrush(QPalette.Background, QBrush(QPixmap("ui_images_box\canvas_black.png")))
    #mainWindow.setPalette(palette)



    black_canvas = QLabel()

    black_canvas.setScaledContents(True)
    black_canvas.setAlignment(Qt.AlignCenter)
    black_canvas.setPixmap(QPixmap("ui_images\canvas_black.png"))
    vbox = QGridLayout()
    vbox.addWidget(black_canvas)


    backgroundWidget.setLayout(vbox)

    pixmap = QPixmap('ui_images/arrow_btn.png')
    arrow_btn = QPushButton(backgroundWidget)
    arrow_btn.setIcon(QIcon('ui_images/arrow_btn.png'))
    arrow_btn.setStyleSheet('ui_images/arrow_btn.png')
    arrow_btn.setIconSize(pixmap.rect().size())
    arrow_btn.setFixedSize(pixmap.rect().size())
    arrow_btn.move(1250, 50)
    arrow_btn.clicked.connect(lambda: one()  )

    pixmap = QPixmap('ui_images/pc_btn.png')
    pc_btn = QPushButton(backgroundWidget)
    pc_btn.setIcon(QIcon('ui_images/pc_btn.png'))
    pc_btn.setStyleSheet('ui_images/pc_btn.png')
    pc_btn.setIconSize(pixmap.rect().size())
    pc_btn.setFixedSize(pixmap.rect().size())
    pc_btn.move(1250, 100)
    pc_btn.clicked.connect(lambda: two()  )

    pixmap = QPixmap('ui_images/x_btn.png')
    x_btn = QPushButton(backgroundWidget)
    x_btn.setIcon(QIcon('ui_images/x_btn.png'))
    x_btn.setStyleSheet('ui_images/x_btn.png')
    x_btn.setIconSize(pixmap.rect().size())
    x_btn.setFixedSize(pixmap.rect().size())
    x_btn.move(1250, 150)
    pc_btn.clicked.connect(lambda: three())

    # Network Buttons
    pixmap = QPixmap('ui_images/red_btn.png')
    red_btn = QPushButton(backgroundWidget)
    red_btn.setIcon(QIcon('ui_images/red_btn.png'))
    red_btn.setStyleSheet('ui_images/red_btn.png')
    red_btn.setIconSize(pixmap.rect().size())
    red_btn.setFixedSize(pixmap.rect().size())
    red_btn.move(1150, 80)
    red_btn.clicked.connect(lambda: three())

    pixmap = QPixmap('ui_images/blue_btn.png')
    blue_btn = QPushButton(backgroundWidget)
    blue_btn.setIcon(QIcon('ui_images/blue_btn.png'))
    blue_btn.setStyleSheet('ui_images/blue_btn.png')
    blue_btn.setIconSize(pixmap.rect().size())
    blue_btn.setFixedSize(pixmap.rect().size())
    blue_btn.move(1150, 100)
    blue_btn.clicked.connect(lambda: three())

    pixmap = QPixmap('ui_images/white_btn.png')
    white_btn = QPushButton(backgroundWidget)
    white_btn.setIcon(QIcon('ui_images/white_btn.png'))
    white_btn.setStyleSheet('ui_images/white_btn.png')
    white_btn.setIconSize(pixmap.rect().size())
    white_btn.setFixedSize(pixmap.rect().size())
    white_btn.move(1150, 120)
    white_btn.clicked.connect(lambda: three())




    # Set window title
    mainWindow.setWindowTitle("Network Simulation!")
    mainWindow.setGeometry(20,20,100,100)

    # Create main menu
    mainMenu = mainWindow.menuBar()
    mainMenu.setNativeMenuBar(False)
    fileMenu = mainMenu.addMenu('&File')

    # Add exit button
    exitButton = QAction(QIcon('exit24.png'), 'Exit', mainWindow)
    exitButton.setShortcut('Ctrl+Q')
    exitButton.setStatusTip('Exit application')
    exitButton.triggered.connect(mainWindow.close)

    openToolButton = QAction(QIcon('exit24.png'),'Toggle',  mainWindow)
    openToolButton.setStatusTip('Opens the tool bar window')
    openToolButton.triggered.connect(toolBar.show)

    menubar = mainWindow.menuBar()

    #   Adds option to the exit menu on the menubar
    exitMenu = menubar.addMenu('&Exit')
    exitMenu.addAction(exitButton)

    # Adds a menu that can have actions added to it
    fileMenu = menubar.addMenu('&File')
    #fileMenu.addAction(printAction)

    menubar.addMenu('&Edit')
    menubar.addMenu('&View')
    menubar.addMenu('&?')

    toolMenu = menubar.addMenu('&Tool')
    toolMenu.addAction(openToolButton)




    mainWindow.show()
    mainWindow.showMaximized()
    sys.exit(a.exec_())

if __name__ == "__main__":
    main()