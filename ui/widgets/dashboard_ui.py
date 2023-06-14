# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources.images_rc as images_rc

class Ui_DashboardWidget(object):
    def setupUi(self, DashboardWidget):
        if not DashboardWidget.objectName():
            DashboardWidget.setObjectName(u"DashboardWidget")
        DashboardWidget.resize(1120, 809)
        DashboardWidget.setStyleSheet(u"background-color:#04395e;")
        self.horizontalLayout = QHBoxLayout(DashboardWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.title = QHBoxLayout()
        self.title.setObjectName(u"title")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.title.addItem(self.horizontalSpacer)

        self.label = QLabel(DashboardWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 15px;\n"
"color: white")

        self.title.addWidget(self.label)

        self.orgField = QComboBox(DashboardWidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"font-size: 15px;\n"
"color: white;\n"
"border: white")

        self.title.addWidget(self.orgField)


        self.verticalLayout.addLayout(self.title)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(DashboardWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"color: white;\n"
"font-size: 20px;\n"
"")

        self.verticalLayout_4.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 5)

        self.mainLayout.addLayout(self.verticalLayout)

        self.lowerBar = QHBoxLayout()
        self.lowerBar.setObjectName(u"lowerBar")

        self.mainLayout.addLayout(self.lowerBar)

        self.mainLayout.setStretch(0, 5)
        self.mainLayout.setStretch(1, 6)

        self.horizontalLayout.addLayout(self.mainLayout)


        self.retranslateUi(DashboardWidget)

        QMetaObject.connectSlotsByName(DashboardWidget)
    # setupUi

    def retranslateUi(self, DashboardWidget):
        DashboardWidget.setWindowTitle(QCoreApplication.translate("DashboardWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("DashboardWidget", u"Select Organization", None))
        self.groupBox.setTitle(QCoreApplication.translate("DashboardWidget", u"Total Employees", None))
    # retranslateUi

