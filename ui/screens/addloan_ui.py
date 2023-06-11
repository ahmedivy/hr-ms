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
        AddLoanWindow.resize(541, 729)
        self.centralwidget = QWidget(AddLoanWindow)
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
        font.setPointSize(16)
        self.label.setFont(font)

        self.titleLayout.addWidget(self.label)


        self.mainLayout.addLayout(self.titleLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
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

        self.orgField = QComboBox(self.centralwidget)
        self.orgField.setObjectName(u"orgField")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.orgField)

        self.empField = QComboBox(self.centralwidget)
        self.empField.setObjectName(u"empField")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.empField)

        self.amountField = QLineEdit(self.centralwidget)
        self.amountField.setObjectName(u"amountField")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.amountField)

        self.reasonField = QLineEdit(self.centralwidget)
        self.reasonField.setObjectName(u"reasonField")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.reasonField)


        self.mainLayout.addLayout(self.formLayout)

        self.footerLayout = QHBoxLayout()
        self.footerLayout.setObjectName(u"footerLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.footerLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")

        self.footerLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.footerLayout.addWidget(self.cancelButton)


        self.mainLayout.addLayout(self.footerLayout)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 3)
        self.mainLayout.setStretch(2, 1)

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

