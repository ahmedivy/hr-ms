# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salarywidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_SalaryWidget(object):
    def setupUi(self, SalaryWidget):
        if not SalaryWidget.objectName():
            SalaryWidget.setObjectName(u"SalaryWidget")
        SalaryWidget.resize(877, 713)
        self.horizontalLayout = QHBoxLayout(SalaryWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.generateSalaryButton = QPushButton(SalaryWidget)
        self.generateSalaryButton.setObjectName(u"generateSalaryButton")

        self.horizontalLayout_2.addWidget(self.generateSalaryButton)


        self.mainLayout.addLayout(self.horizontalLayout_2)

        self.tableLayout = QVBoxLayout()
        self.tableLayout.setObjectName(u"tableLayout")
        self.filterLayout = QHBoxLayout()
        self.filterLayout.setObjectName(u"filterLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.filterLayout.addItem(self.horizontalSpacer_2)

        self.orgField = QComboBox(SalaryWidget)
        self.orgField.setObjectName(u"orgField")

        self.filterLayout.addWidget(self.orgField)


        self.tableLayout.addLayout(self.filterLayout)

        self.tableView = QTableView(SalaryWidget)
        self.tableView.setObjectName(u"tableView")

        self.tableLayout.addWidget(self.tableView)

        self.tableLayout.setStretch(0, 1)
        self.tableLayout.setStretch(1, 9)

        self.mainLayout.addLayout(self.tableLayout)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 10)

        self.horizontalLayout.addLayout(self.mainLayout)


        self.retranslateUi(SalaryWidget)

        QMetaObject.connectSlotsByName(SalaryWidget)
    # setupUi

    def retranslateUi(self, SalaryWidget):
        SalaryWidget.setWindowTitle(QCoreApplication.translate("SalaryWidget", u"Form", None))
        self.generateSalaryButton.setText(QCoreApplication.translate("SalaryWidget", u"Generate Salary", None))
    # retranslateUi

