# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addloan.ui'
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

class Ui_AddLoanWindow(object):
    def setupUi(self, AddLoanWindow):
        if not AddLoanWindow.objectName():
            AddLoanWindow.setObjectName(u"AddLoanWindow")
        AddLoanWindow.resize(585, 447)
        AddLoanWindow.setStyleSheet(u"background-color:#04395e;")
        self.centralwidget = QWidget(AddLoanWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer_2)

        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"border-radius:15px;\n"
"padding: 0 10px;\n"
"text-transform:uppercase;\n"
"")

        self.titleLayout.addWidget(self.label)


        self.mainLayout.addLayout(self.titleLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.mainLayout.addItem(self.horizontalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.orgField = QComboBox(self.centralwidget)
        self.orgField.setObjectName(u"orgField")
        self.orgField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"margin: 3px 0;\n"
"padding: 0 5px;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.orgField)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.empField = QComboBox(self.centralwidget)
        self.empField.setObjectName(u"empField")
        self.empField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"margin: 3px 0;\n"
"padding: 0 5px;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.empField)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.amountField = QLineEdit(self.centralwidget)
        self.amountField.setObjectName(u"amountField")
        self.amountField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"margin: 3px 0;\n"
"padding: 0 5px;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.amountField)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font:bold;\n"
"color: #FFFAFB;\n"
"text-transform:uppercase;\n"
"text-decoration:underline;\n"
"font-size:13px;")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.reasonField = QLineEdit(self.centralwidget)
        self.reasonField.setObjectName(u"reasonField")
        self.reasonField.setStyleSheet(u"background-color:#FFFAFB;\n"
"border-radius:10px;\n"
"height: 25px;\n"
"margin: 3px 0;\n"
"padding: 0 5px;")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.reasonField)


        self.mainLayout.addLayout(self.formLayout)

        self.footerLayout = QHBoxLayout()
        self.footerLayout.setObjectName(u"footerLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.footerLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setStyleSheet(u"QPushButton{\n"
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
"")

        self.footerLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setStyleSheet(u"QPushButton{\n"
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
"")

        self.footerLayout.addWidget(self.cancelButton)


        self.mainLayout.addLayout(self.footerLayout)

        self.mainLayout.setStretch(1, 1)
        self.mainLayout.setStretch(4, 3)
        self.mainLayout.setStretch(5, 1)

        self.horizontalLayout.addLayout(self.mainLayout)

        AddLoanWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddLoanWindow)

        QMetaObject.connectSlotsByName(AddLoanWindow)
    # setupUi

    def retranslateUi(self, AddLoanWindow):
        AddLoanWindow.setWindowTitle(QCoreApplication.translate("AddLoanWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AddLoanWindow", u"Add New Loan", None))
        self.label_2.setText(QCoreApplication.translate("AddLoanWindow", u"Organization", None))
        self.label_3.setText(QCoreApplication.translate("AddLoanWindow", u"Employee", None))
        self.label_4.setText(QCoreApplication.translate("AddLoanWindow", u"Amount", None))
        self.label_5.setText(QCoreApplication.translate("AddLoanWindow", u"Reason", None))
        self.okButton.setText(QCoreApplication.translate("AddLoanWindow", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("AddLoanWindow", u"Cancel", None))
    # retranslateUi

