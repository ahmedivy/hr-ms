# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salarydetails.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_SalaryDetailWindow(object):
    def setupUi(self, SalaryDetailWindow):
        if not SalaryDetailWindow.objectName():
            SalaryDetailWindow.setObjectName(u"SalaryDetailWindow")
        SalaryDetailWindow.resize(829, 733)
        self.centralwidget = QWidget(SalaryDetailWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleBar = QHBoxLayout()
        self.titleBar.setObjectName(u"titleBar")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.titleBar.addWidget(self.label)


        self.titleLayout.addLayout(self.titleBar)

        self.filterBar = QHBoxLayout()
        self.filterBar.setObjectName(u"filterBar")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.filterBar.addItem(self.horizontalSpacer)

        self.monthField = QLineEdit(self.centralwidget)
        self.monthField.setObjectName(u"monthField")

        self.filterBar.addWidget(self.monthField)


        self.titleLayout.addLayout(self.filterBar)


        self.mainLayout.addLayout(self.titleLayout)

        self.tableLayout = QHBoxLayout()
        self.tableLayout.setObjectName(u"tableLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.tableLayout.addWidget(self.tableView)


        self.mainLayout.addLayout(self.tableLayout)

        self.mainLayout.setStretch(0, 3)
        self.mainLayout.setStretch(1, 8)

        self.horizontalLayout.addLayout(self.mainLayout)

        SalaryDetailWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SalaryDetailWindow)

        QMetaObject.connectSlotsByName(SalaryDetailWindow)
    # setupUi

    def retranslateUi(self, SalaryDetailWindow):
        SalaryDetailWindow.setWindowTitle(QCoreApplication.translate("SalaryDetailWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SalaryDetailWindow", u"Salary Details", None))
    # retranslateUi

