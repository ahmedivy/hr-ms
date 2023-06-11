# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(563, 475)
        LoginWindow.setStyleSheet(u"background-color:#04395e;")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"text-transform:uppercase;\n"
"font-size: 20px;\n"
"background-color: #004e89;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"border-radius:15px;\n"
"margin: 20px;\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameField = QLineEdit(self.frame_2)
        self.usernameField.setObjectName(u"usernameField")
        font1 = QFont()
        font1.setPointSize(12)
        self.usernameField.setFont(font1)
        self.usernameField.setStyleSheet(u"margin: 3px 0;\n"
"border-radius:10px;\n"
"width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;\n"
"padding:7px;\n"
"margin: 0 20px;")

        self.verticalLayout.addWidget(self.usernameField)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"margin: 3px 0;border-radius:10px;\n"
"width:250px;\n"
"height: 25px;\n"
"background-color:#FFFAFB;\n"
"padding:7px;\n"
"margin: 0 20px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: #274c77;\n"
"color:#FFFAFB;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"width: 100px;\n"
"height:25px;\n"
"margin-right:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: #4cc9f0;\n"
" color:black;\n"
"font:bold;\n"
"padding: 5px;\n"
"border-radius:7px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_3)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Login to you Account", None))
#if QT_CONFIG(tooltip)
        self.usernameField.setToolTip(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p>Username</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.usernameField.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Username", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p>Password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
    # retranslateUi

