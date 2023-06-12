# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'organizationWidget.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_OrganizationWidget(object):
    def setupUi(self, OrganizationWidget):
        if not OrganizationWidget.objectName():
            OrganizationWidget.setObjectName(u"OrganizationWidget")
        OrganizationWidget.resize(876, 789)
        self.horizontalLayout = QHBoxLayout(OrganizationWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLayout.setContentsMargins(20, -1, 20, -1)
        self.titleBox = QVBoxLayout()
        self.titleBox.setObjectName(u"titleBox")
        self.titleLabel = QLabel(OrganizationWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(28)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"color:white")

        self.titleBox.addWidget(self.titleLabel)

        self.buttonBox = QHBoxLayout()
        self.buttonBox.setObjectName(u"buttonBox")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonBox.addItem(self.horizontalSpacer)

        self.newButton = QPushButton(OrganizationWidget)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #4cc9f0;\n"
"  color:black;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
" background-color: rgb(255, 233, 67);\n"
"  color:black;\n"
"font:bold;\n"
"padding: 3px;\n"
"border-radius:10px;\n"
"\n"
"}")

        self.buttonBox.addWidget(self.newButton)

        self.deleteButton = QPushButton(OrganizationWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"margin-right:15px;\n"
"height: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #4cc9f0;\n"
"  color:black;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
" background-color: rgb(255, 233, 67);\n"
"  color:black;\n"
"font:bold;\n"
"padding: 3px;\n"
"border-radius:10px;\n"
"\n"
"}")

        self.buttonBox.addWidget(self.deleteButton)


        self.titleBox.addLayout(self.buttonBox)


        self.titleLayout.addLayout(self.titleBox)


        self.verticalLayout.addLayout(self.titleLayout)

        self.tableLayout = QVBoxLayout()
        self.tableLayout.setObjectName(u"tableLayout")
        self.tableView = QTableView(OrganizationWidget)
        self.tableView.setObjectName(u"tableView")

        self.tableLayout.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.tableLayout)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 7)

        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(OrganizationWidget)

        QMetaObject.connectSlotsByName(OrganizationWidget)
    # setupUi

    def retranslateUi(self, OrganizationWidget):
        OrganizationWidget.setWindowTitle(QCoreApplication.translate("OrganizationWidget", u"Form", None))
        self.titleLabel.setText(QCoreApplication.translate("OrganizationWidget", u"Associated Organizations", None))
        self.newButton.setText(QCoreApplication.translate("OrganizationWidget", u"New", None))
        self.deleteButton.setText(QCoreApplication.translate("OrganizationWidget", u"Delete", None))
    # retranslateUi

