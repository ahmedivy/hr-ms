# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'loginwindow.ui'
##
# Created by: Qt User Interface Compiler version 6.5.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
                               QStatusBar, QVBoxLayout, QWidget)


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(1023, 866)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1023, 25))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
    # retranslateUi
