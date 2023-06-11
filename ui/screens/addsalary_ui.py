# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addsalary.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddSalaryWindow(object):
    def setupUi(self, AddSalaryWindow):
        if not AddSalaryWindow.objectName():
            AddSalaryWindow.setObjectName(u"AddSalaryWindow")
        AddSalaryWindow.resize(521, 672)
        self.centralwidget = QWidget(AddSalaryWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"text-align: center")

        self.titleLayout.addWidget(self.label)


        self.mainLayout.addLayout(self.titleLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(20, 30, 20, 20)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.descField = QLineEdit(self.centralwidget)
        self.descField.setObjectName(u"descField")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.descField)

        self.monthField = QComboBox(self.centralwidget)
        self.monthField.setObjectName(u"monthField")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.monthField)

        self.yearField = QComboBox(self.centralwidget)
        self.yearField.setObjectName(u"yearField")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.yearField)

        self.orgField = QComboBox(self.centralwidget)
        self.orgField.setObjectName(u"orgField")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.orgField)


        self.mainLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.confirmButton = QPushButton(self.centralwidget)
        self.confirmButton.setObjectName(u"confirmButton")

        self.horizontalLayout_2.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.mainLayout.addLayout(self.horizontalLayout_2)

        self.mainLayout.setStretch(0, 2)
        self.mainLayout.setStretch(1, 8)
        self.mainLayout.setStretch(2, 2)

        self.horizontalLayout.addLayout(self.mainLayout)

        AddSalaryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddSalaryWindow)

        QMetaObject.connectSlotsByName(AddSalaryWindow)
    # setupUi

    def retranslateUi(self, AddSalaryWindow):
        AddSalaryWindow.setWindowTitle(QCoreApplication.translate("AddSalaryWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddSalaryWindow", u"Generate Salary Sheet", None))
        self.label_2.setText(QCoreApplication.translate("AddSalaryWindow", u"Organization", None))
        self.label_3.setText(QCoreApplication.translate("AddSalaryWindow", u"Salary Month", None))
        self.label_4.setText(QCoreApplication.translate("AddSalaryWindow", u"Salary Year", None))
        self.label_5.setText(QCoreApplication.translate("AddSalaryWindow", u"Description", None))
        self.confirmButton.setText(QCoreApplication.translate("AddSalaryWindow", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("AddSalaryWindow", u"Cancel", None))
    # retranslateUi

