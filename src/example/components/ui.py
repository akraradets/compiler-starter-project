# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(408, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_text = QLineEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setGeometry(QRect(60, 30, 113, 22))
        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(20, 60, 80, 22))
        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(110, 60, 80, 22))
        self.button_plus = QPushButton(self.centralwidget)
        self.button_plus.setObjectName(u"button_plus")
        self.button_plus.setGeometry(QRect(200, 60, 80, 22))
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setGeometry(QRect(20, 30, 57, 14))
        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(20, 110, 57, 14))
        self.output_lcd = QLCDNumber(self.centralwidget)
        self.output_lcd.setObjectName(u"output_lcd")
        self.output_lcd.setGeometry(QRect(70, 100, 141, 23))
        self.output_lcd.setSmallDecimalPoint(True)
        self.output_lcd.setDigitCount(9)
        self.output_lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.output_lcd.setProperty(u"value", 0.000000000000000)
        self.output_lcd.setProperty(u"intValue", 0)
        self.button_equal = QPushButton(self.centralwidget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setGeometry(QRect(290, 60, 80, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 408, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

