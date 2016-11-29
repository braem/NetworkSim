
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
class TableFunction(QWidget):
    @staticmethod
    def createWidget2(self):
        bigwin = QWidget()

        window = QVBoxLayout()

        pixmap = QPixmap('ui_images/select_btn.png')
        select_btn = QPushButton(bigwin)
        select_btn.setIcon(QIcon('ui_images/select_btn.png'))
        select_btn.setStyleSheet('ui_images/select_btn.png')
        select_btn.setIconSize(pixmap.rect().size())
        select_btn.setFixedSize(pixmap.rect().size())
        select_btn.clicked.connect(lambda: one())

        pixmap = QPixmap('ui_images/group_btn.png')
        group_btn = QPushButton(bigwin)
        group_btn.setIcon(QIcon('ui_images/group_btn.png'))
        group_btn.setStyleSheet('ui_images/group_btn.png')
        group_btn.setIconSize(pixmap.rect().size())
        group_btn.setFixedSize(pixmap.rect().size())
        group_btn.clicked.connect(lambda: one())

        pixmap = QPixmap('ui_images/ungroup_btn.png')
        ungroup_btn = QPushButton(bigwin)
        ungroup_btn.setIcon(QIcon('ui_images/ungroup_btn.png'))
        ungroup_btn.setStyleSheet('ui_images/ungroup_btn.png')
        ungroup_btn.setIconSize(pixmap.rect().size())
        ungroup_btn.setFixedSize(pixmap.rect().size())
        ungroup_btn.clicked.connect(lambda: one())

        pixmap = QPixmap('ui_images/label_btn.png')
        label_btn = QPushButton(bigwin)
        label_btn.setIcon(QIcon('ui_images/label_btn.png'))
        label_btn.setStyleSheet('ui_images/label_btn.png')
        label_btn.setIconSize(pixmap.rect().size())
        label_btn.setFixedSize(pixmap.rect().size())
        label_btn.clicked.connect(lambda: one())

        pixmap = QPixmap('ui_images/delete_btn.png')
        delete_btn = QPushButton(bigwin)
        delete_btn.setIcon(QIcon('ui_images/delete_btn.png'))
        delete_btn.setStyleSheet('ui_images/delete_btn.png')
        delete_btn.setIconSize(pixmap.rect().size())
        delete_btn.setFixedSize(pixmap.rect().size())
        delete_btn.clicked.connect(lambda: one())

        pixmap = QPixmap('ui_images/congfigure_btn.png')
        congfigure_btn = QPushButton(bigwin)
        congfigure_btn.setIcon(QIcon('ui_images/congfigure_btn.png'))
        congfigure_btn.setStyleSheet('ui_images/congfigure_btn.png')
        congfigure_btn.setIconSize(pixmap.rect().size())
        congfigure_btn.setFixedSize(pixmap.rect().size())
        congfigure_btn.clicked.connect(lambda: one())

        pixmap = QPixmap('ui_images/run_btn.png')
        run_btn = QPushButton(bigwin)
        run_btn.setIcon(QIcon('ui_images/run_btn.png'))
        run_btn.setStyleSheet('ui_images/run_btn.png')
        run_btn.setIconSize(pixmap.rect().size())
        run_btn.setFixedSize(pixmap.rect().size())
        run_btn.clicked.connect(lambda: one())

        window.setSpacing(0)
        window.setMargin(0)

        window.addWidget(select_btn)
        window.addWidget(group_btn)
        window.addWidget(ungroup_btn)
        window.addWidget(label_btn)
        window.addWidget(delete_btn)
        window.addWidget(congfigure_btn)
        window.addWidget(run_btn)

        bigwin.setLayout(window)
        bigwin.setGeometry(1150, 300, 190, 360)
        return bigwin