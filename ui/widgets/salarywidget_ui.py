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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

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
        self.label = QLabel(SalaryWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 30px;\n"
"color: white;")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.generateSalaryButton = QPushButton(SalaryWidget)
        self.generateSalaryButton.setObjectName(u"generateSalaryButton")
        self.generateSalaryButton.setStyleSheet(u"QPushButton{\n"
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
        self.orgField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"width:250px;\n"
"height: 25px;\n"
"margin: 3px 0;")

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
        self.label.setText(QCoreApplication.translate("SalaryWidget", u"Salary Details", None))
        self.generateSalaryButton.setText(QCoreApplication.translate("SalaryWidget", u"Generate Salary", None))
    # retranslateUi

