# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowSW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1398, 932)
        font = QFont()
        font.setFamily(u"Cascadia Code")
        font.setPointSize(10)
        main_window.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setStyleSheet(u"/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left"
                        "-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-rad"
                        "ius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-righ"
                        "t-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargrad"
                        "ient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	"
                        "border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qli"
                        "neargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QLabel {\n"
"	color: #000000;\n"
"}\n"
"QLCDNumber {\n"
"	color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(230, 230, 230);\n"
"	border-style: solid;\n"
"	background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:pad, "
                        "x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"	color: #000000;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	border-bot"
                        "tom-color: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #000000;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	color: #000000;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(223,223,223);\n"
"		background-color:rgb(226,226,226);\n"
"		border-style: solid;\n"
"		border-width: 2px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	border-style: solid;\n"
"	border-left-width:1px;\n"
"	border-right-width:0px;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlinear"
                        "gradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"	border-style: solid;\n"
"	border-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-le"
                        "ft:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-left-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2"
                        ":0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"  	border-bottom-width:1px;\n"
"  	border-top-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QCheckBo"
                        "x {\n"
"	color: #000000;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), "
                        "stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"}\n"
"QRadioButton {\n"
"	color: 000000;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	border-style: solid;\n"
"	bord"
                        "er-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTo"
                        "olBox {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
""
                        "	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	max-width: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
""
                        "	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
""
                        "   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizo"
                        "ntal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"   background: none;\n"
"}")
        main_window.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.actionImport_CSV = QAction(main_window)
        self.actionImport_CSV.setObjectName(u"actionImport_CSV")
        self.actionImport_CSV.setCheckable(True)
        self.actionImport_CSV.setChecked(False)
        icon1 = QIcon()
        icon1.addFile(u"resources/2850900 - document download file page paper.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport_CSV.setIcon(icon1)
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        self.actionImport_CSV.setFont(font1)
        self.actionTutorial = QAction(main_window)
        self.actionTutorial.setObjectName(u"actionTutorial")
        self.actionTutorial.setFont(font1)
        self.actionDocumentation = QAction(main_window)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionDocumentation.setFont(font1)
        self.actionWebsite = QAction(main_window)
        self.actionWebsite.setObjectName(u"actionWebsite")
        self.actionWebsite.setFont(font1)
        self.actionReport_a_bug = QAction(main_window)
        self.actionReport_a_bug.setObjectName(u"actionReport_a_bug")
        self.actionReport_a_bug.setFont(font1)
        self.actionPropose_a_new_feauture = QAction(main_window)
        self.actionPropose_a_new_feauture.setObjectName(u"actionPropose_a_new_feauture")
        self.actionPropose_a_new_feauture.setFont(font1)
        self.actionBugs_and_feature_requests = QAction(main_window)
        self.actionBugs_and_feature_requests.setObjectName(u"actionBugs_and_feature_requests")
        self.actionBugs_and_feature_requests.setFont(font1)
        self.actionContact_project_creator = QAction(main_window)
        self.actionContact_project_creator.setObjectName(u"actionContact_project_creator")
        self.actionContact_project_creator.setFont(font1)
        self.actionTake_survey_to_improve_the_project = QAction(main_window)
        self.actionTake_survey_to_improve_the_project.setObjectName(u"actionTake_survey_to_improve_the_project")
        self.actionTake_survey_to_improve_the_project.setFont(font1)
        self.actionCurrent_Version = QAction(main_window)
        self.actionCurrent_Version.setObjectName(u"actionCurrent_Version")
        self.actionCurrent_Version.setFont(font1)
        self.actionImport_Data_SW = QAction(main_window)
        self.actionImport_Data_SW.setObjectName(u"actionImport_Data_SW")
        self.actionImport_Data_SW.setCheckable(False)
        self.actionImport_Data_SW.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(u"resources/SeisWare_64x64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport_Data_SW.setIcon(icon2)
        self.actionImport_Data_SW.setVisible(True)
        self.actionCheck_for_updates = QAction(main_window)
        self.actionCheck_for_updates.setObjectName(u"actionCheck_for_updates")
        self.actionCheck_for_updates.setFont(font1)
        self.actionExport_Cashflow = QAction(main_window)
        self.actionExport_Cashflow.setObjectName(u"actionExport_Cashflow")
        icon3 = QIcon()
        icon3.addFile(u"resources/2850901 - document file page paper upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport_Cashflow.setIcon(icon3)
        self.actionExport_Cashflow.setFont(font1)
        self.actionDonate = QAction(main_window)
        self.actionDonate.setObjectName(u"actionDonate")
        icon4 = QIcon()
        icon4.addFile(u"../../resources/3213304 - bank business money research search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDonate.setIcon(icon4)
        self.actionDonate.setFont(font1)
        self.actionShow_Cumulative_Volumes = QAction(main_window)
        self.actionShow_Cumulative_Volumes.setObjectName(u"actionShow_Cumulative_Volumes")
        self.actionNormalize_dates_to_Months = QAction(main_window)
        self.actionNormalize_dates_to_Months.setObjectName(u"actionNormalize_dates_to_Months")
        self.actionShow_Annual_Cashflow = QAction(main_window)
        self.actionShow_Annual_Cashflow.setObjectName(u"actionShow_Annual_Cashflow")
        self.actionComing_Soon = QAction(main_window)
        self.actionComing_Soon.setObjectName(u"actionComing_Soon")
        self.actionExport_EUR_To_SeisWare = QAction(main_window)
        self.actionExport_EUR_To_SeisWare.setObjectName(u"actionExport_EUR_To_SeisWare")
        icon5 = QIcon()
        icon5.addFile(u"resources/SeisWare_64x64.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionExport_EUR_To_SeisWare.setIcon(icon5)
        self.actionImport_CSV_2 = QAction(main_window)
        self.actionImport_CSV_2.setObjectName(u"actionImport_CSV_2")
        icon6 = QIcon()
        icon6.addFile(u"resources/2850900 - document download file page paper.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u"resources/2850900 - document download file page paper.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionImport_CSV_2.setIcon(icon6)
        self.actionImport_Data_SW_2 = QAction(main_window)
        self.actionImport_Data_SW_2.setObjectName(u"actionImport_Data_SW_2")
        icon7 = QIcon()
        icon7.addFile(u"resources/SeisWare_64x64.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u"resources/SeisWare_64x64.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionImport_Data_SW_2.setIcon(icon7)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"aqua")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBoxWellSelect = QComboBox(self.centralwidget)
        self.comboBoxWellSelect.setObjectName(u"comboBoxWellSelect")
        self.comboBoxWellSelect.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(12)
        self.comboBoxWellSelect.setFont(font2)
        self.comboBoxWellSelect.setMaxVisibleItems(25)

        self.gridLayout_2.addWidget(self.comboBoxWellSelect, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(1200, 800))
        self.tabWidget.setFont(font2)
        self.tabWidget.setFocusPolicy(Qt.WheelFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setMovable(False)
        self.tabMainMenu = QWidget()
        self.tabMainMenu.setObjectName(u"tabMainMenu")
        self.label = QLabel(self.tabMainMenu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 10, 991, 381))
        font3 = QFont()
        font3.setFamily(u"Cascadia Mono")
        font3.setPointSize(14)
        self.label.setFont(font3)
        self.wellListView = QListView(self.tabMainMenu)
        self.wellListView.setObjectName(u"wellListView")
        self.wellListView.setGeometry(QRect(10, 40, 341, 511))
        self.wellListView.setFont(font2)
        self.wellListView.setFrameShadow(QFrame.Sunken)
        self.wellListView.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.wellListView.setAlternatingRowColors(True)
        self.wellListLabel = QLabel(self.tabMainMenu)
        self.wellListLabel.setObjectName(u"wellListLabel")
        self.wellListLabel.setGeometry(QRect(30, 10, 141, 21))
        font4 = QFont()
        font4.setFamily(u"Cascadia Code SemiBold")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.wellListLabel.setFont(font4)
        icon8 = QIcon()
        icon8.addFile(u"../../resources/4288576 - and application internet seo technology web website.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabMainMenu, icon8, "")
        self.tabForecasting = QWidget()
        self.tabForecasting.setObjectName(u"tabForecasting")
        self.gridLayout = QGridLayout(self.tabForecasting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tabForecasting)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font4)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamily(u"Cascadia Code SemiBold")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_2.setFont(font5)

        self.verticalLayout.addWidget(self.label_2)

        self.comboBoxPhase = QComboBox(self.groupBox)
        self.comboBoxPhase.setObjectName(u"comboBoxPhase")
        self.comboBoxPhase.setFont(font2)

        self.verticalLayout.addWidget(self.comboBoxPhase)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)

        self.verticalLayout.addWidget(self.label_3)

        self.comboBoxUnits = QComboBox(self.groupBox)
        self.comboBoxUnits.setObjectName(u"comboBoxUnits")
        self.comboBoxUnits.setFont(font2)

        self.verticalLayout.addWidget(self.comboBoxUnits)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font5)

        self.verticalLayout.addWidget(self.label_4)

        self.dateEditCurveStart = QDateEdit(self.groupBox)
        self.dateEditCurveStart.setObjectName(u"dateEditCurveStart")
        self.dateEditCurveStart.setFont(font2)
        self.dateEditCurveStart.setCalendarPopup(True)
        self.dateEditCurveStart.setDate(QDate(2020, 1, 1))

        self.verticalLayout.addWidget(self.dateEditCurveStart)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.verticalLayout.addWidget(self.label_5)

        self.spinBoxRate = QSpinBox(self.groupBox)
        self.spinBoxRate.setObjectName(u"spinBoxRate")
        self.spinBoxRate.setFont(font2)
        self.spinBoxRate.setMaximum(1000000)

        self.verticalLayout.addWidget(self.spinBoxRate)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)

        self.verticalLayout.addWidget(self.label_6)

        self.doubleSpinBoxDi = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxDi.setObjectName(u"doubleSpinBoxDi")
        self.doubleSpinBoxDi.setFont(font2)
        self.doubleSpinBoxDi.setSingleStep(0.500000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBoxDi)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.verticalLayout.addWidget(self.label_7)

        self.doubleSpinBoxBFactor = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxBFactor.setObjectName(u"doubleSpinBoxBFactor")
        self.doubleSpinBoxBFactor.setFont(font2)
        self.doubleSpinBoxBFactor.setMaximum(2.000000000000000)
        self.doubleSpinBoxBFactor.setSingleStep(0.010000000000000)
        self.doubleSpinBoxBFactor.setValue(1.100000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBoxBFactor)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)

        self.verticalLayout.addWidget(self.label_10)

        self.doubleSpinBoxMinDecline = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBoxMinDecline.setObjectName(u"doubleSpinBoxMinDecline")
        self.doubleSpinBoxMinDecline.setFont(font2)
        self.doubleSpinBoxMinDecline.setValue(6.000000000000000)

        self.verticalLayout.addWidget(self.doubleSpinBoxMinDecline)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.verticalLayout.addWidget(self.label_8)

        self.lineEditDeclineCurveName = QLineEdit(self.groupBox)
        self.lineEditDeclineCurveName.setObjectName(u"lineEditDeclineCurveName")
        self.lineEditDeclineCurveName.setFont(font2)
        self.lineEditDeclineCurveName.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.lineEditDeclineCurveName)

        self.pushButtonCreateDeclineCurve = QPushButton(self.groupBox)
        self.pushButtonCreateDeclineCurve.setObjectName(u"pushButtonCreateDeclineCurve")
        font6 = QFont()
        font6.setFamily(u"Cascadia Code SemiBold")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.pushButtonCreateDeclineCurve.setFont(font6)
        self.pushButtonCreateDeclineCurve.setCheckable(False)

        self.verticalLayout.addWidget(self.pushButtonCreateDeclineCurve)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.verticalLayout.addWidget(self.label_9)

        self.comboBoxOilDeclineCurves = QComboBox(self.groupBox)
        self.comboBoxOilDeclineCurves.setObjectName(u"comboBoxOilDeclineCurves")
        self.comboBoxOilDeclineCurves.setFont(font)

        self.verticalLayout.addWidget(self.comboBoxOilDeclineCurves)

        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)

        self.verticalLayout.addWidget(self.label_24)

        self.comboBoxGasDeclineCurves = QComboBox(self.groupBox)
        self.comboBoxGasDeclineCurves.setObjectName(u"comboBoxGasDeclineCurves")
        self.comboBoxGasDeclineCurves.setFont(font)

        self.verticalLayout.addWidget(self.comboBoxGasDeclineCurves)

        self.checkBoxUseOil = QCheckBox(self.groupBox)
        self.checkBoxUseOil.setObjectName(u"checkBoxUseOil")
        self.checkBoxUseOil.setFont(font2)

        self.verticalLayout.addWidget(self.checkBoxUseOil)

        self.checkBoxUseGas = QCheckBox(self.groupBox)
        self.checkBoxUseGas.setObjectName(u"checkBoxUseGas")
        self.checkBoxUseGas.setFont(font2)

        self.verticalLayout.addWidget(self.checkBoxUseGas)

        self.pushButtonRemoveDeclineCurves = QPushButton(self.groupBox)
        self.pushButtonRemoveDeclineCurves.setObjectName(u"pushButtonRemoveDeclineCurves")
        self.pushButtonRemoveDeclineCurves.setFont(font6)

        self.verticalLayout.addWidget(self.pushButtonRemoveDeclineCurves)

        self.pushButtonPlotDeclineCurve = QPushButton(self.groupBox)
        self.pushButtonPlotDeclineCurve.setObjectName(u"pushButtonPlotDeclineCurve")
        self.pushButtonPlotDeclineCurve.setFont(font6)

        self.verticalLayout.addWidget(self.pushButtonPlotDeclineCurve)

        self.pushButtonDeleteDeclineCurve = QPushButton(self.groupBox)
        self.pushButtonDeleteDeclineCurve.setObjectName(u"pushButtonDeleteDeclineCurve")
        self.pushButtonDeleteDeclineCurve.setFont(font6)

        self.verticalLayout.addWidget(self.pushButtonDeleteDeclineCurve)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.widgetProductionPlot = QWidget(self.tabForecasting)
        self.widgetProductionPlot.setObjectName(u"widgetProductionPlot")
        sizePolicy1.setHeightForWidth(self.widgetProductionPlot.sizePolicy().hasHeightForWidth())
        self.widgetProductionPlot.setSizePolicy(sizePolicy1)
        self.widgetProductionPlot.setSizeIncrement(QSize(10, 10))
        self.widgetProductionPlot.setFont(font2)

        self.gridLayout.addWidget(self.widgetProductionPlot, 0, 1, 1, 1)

        icon9 = QIcon()
        icon9.addFile(u"../../resources/4288598 - analysis analytics chart data pie.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabForecasting, icon9, "")
        self.tabCashflow = QWidget()
        self.tabCashflow.setObjectName(u"tabCashflow")
        self.tabCashflow.setFont(font)
        self.gridLayout_3 = QGridLayout(self.tabCashflow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBoxCashflowSetup = QGroupBox(self.tabCashflow)
        self.groupBoxCashflowSetup.setObjectName(u"groupBoxCashflowSetup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBoxCashflowSetup.sizePolicy().hasHeightForWidth())
        self.groupBoxCashflowSetup.setSizePolicy(sizePolicy2)
        self.groupBoxCashflowSetup.setMinimumSize(QSize(600, 400))
        self.groupBoxCashflowSetup.setMaximumSize(QSize(400, 16777215))
        self.groupBoxCashflowSetup.setFont(font4)
        self.formLayout = QFormLayout(self.groupBoxCashflowSetup)
        self.formLayout.setObjectName(u"formLayout")
        self.label_11 = QLabel(self.groupBoxCashflowSetup)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.comboBoxOilDeclineCurve = QComboBox(self.groupBoxCashflowSetup)
        self.comboBoxOilDeclineCurve.setObjectName(u"comboBoxOilDeclineCurve")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBoxOilDeclineCurve.sizePolicy().hasHeightForWidth())
        self.comboBoxOilDeclineCurve.setSizePolicy(sizePolicy3)
        self.comboBoxOilDeclineCurve.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBoxOilDeclineCurve)

        self.label_12 = QLabel(self.groupBoxCashflowSetup)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.comboBoxGasDeclineCurve = QComboBox(self.groupBoxCashflowSetup)
        self.comboBoxGasDeclineCurve.setObjectName(u"comboBoxGasDeclineCurve")
        sizePolicy3.setHeightForWidth(self.comboBoxGasDeclineCurve.sizePolicy().hasHeightForWidth())
        self.comboBoxGasDeclineCurve.setSizePolicy(sizePolicy3)
        self.comboBoxGasDeclineCurve.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBoxGasDeclineCurve)

        self.label_13 = QLabel(self.groupBoxCashflowSetup)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.dateEditCashflowStart = QDateEdit(self.groupBoxCashflowSetup)
        self.dateEditCashflowStart.setObjectName(u"dateEditCashflowStart")
        self.dateEditCashflowStart.setFont(font2)
        self.dateEditCashflowStart.setCalendarPopup(True)
        self.dateEditCashflowStart.setDate(QDate(2020, 1, 1))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEditCashflowStart)

        self.label_14 = QLabel(self.groupBoxCashflowSetup)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_14)

        self.doubleSpinBoxWorkingInterest = QDoubleSpinBox(self.groupBoxCashflowSetup)
        self.doubleSpinBoxWorkingInterest.setObjectName(u"doubleSpinBoxWorkingInterest")
        self.doubleSpinBoxWorkingInterest.setFont(font2)
        self.doubleSpinBoxWorkingInterest.setMaximum(100.000000000000000)
        self.doubleSpinBoxWorkingInterest.setValue(100.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBoxWorkingInterest)

        self.label_15 = QLabel(self.groupBoxCashflowSetup)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_15)

        self.doubleSpinBoxNetRevenueInterest = QDoubleSpinBox(self.groupBoxCashflowSetup)
        self.doubleSpinBoxNetRevenueInterest.setObjectName(u"doubleSpinBoxNetRevenueInterest")
        self.doubleSpinBoxNetRevenueInterest.setFont(font2)
        self.doubleSpinBoxNetRevenueInterest.setMaximum(100.000000000000000)
        self.doubleSpinBoxNetRevenueInterest.setValue(75.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBoxNetRevenueInterest)

        self.label_16 = QLabel(self.groupBoxCashflowSetup)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_16)

        self.spinBoxDiscountRate = QSpinBox(self.groupBoxCashflowSetup)
        self.spinBoxDiscountRate.setObjectName(u"spinBoxDiscountRate")
        self.spinBoxDiscountRate.setFont(font2)
        self.spinBoxDiscountRate.setValue(10)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.spinBoxDiscountRate)

        self.label_17 = QLabel(self.groupBoxCashflowSetup)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_17)

        self.spinBoxSeveranceTax = QSpinBox(self.groupBoxCashflowSetup)
        self.spinBoxSeveranceTax.setObjectName(u"spinBoxSeveranceTax")
        self.spinBoxSeveranceTax.setFont(font2)
        self.spinBoxSeveranceTax.setValue(7)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.spinBoxSeveranceTax)

        self.label_18 = QLabel(self.groupBoxCashflowSetup)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_18)

        self.doubleSpinBoxOilPrice = QDoubleSpinBox(self.groupBoxCashflowSetup)
        self.doubleSpinBoxOilPrice.setObjectName(u"doubleSpinBoxOilPrice")
        self.doubleSpinBoxOilPrice.setFont(font2)
        self.doubleSpinBoxOilPrice.setValue(50.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.doubleSpinBoxOilPrice)

        self.label_19 = QLabel(self.groupBoxCashflowSetup)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font5)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_19)

        self.doubleSpinBoxGasPrice = QDoubleSpinBox(self.groupBoxCashflowSetup)
        self.doubleSpinBoxGasPrice.setObjectName(u"doubleSpinBoxGasPrice")
        self.doubleSpinBoxGasPrice.setFont(font2)
        self.doubleSpinBoxGasPrice.setSingleStep(0.100000000000000)
        self.doubleSpinBoxGasPrice.setValue(2.500000000000000)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.doubleSpinBoxGasPrice)

        self.label_20 = QLabel(self.groupBoxCashflowSetup)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font5)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_20)

        self.doubleSpinBoxOilDiff = QDoubleSpinBox(self.groupBoxCashflowSetup)
        self.doubleSpinBoxOilDiff.setObjectName(u"doubleSpinBoxOilDiff")
        self.doubleSpinBoxOilDiff.setFont(font2)
        self.doubleSpinBoxOilDiff.setSingleStep(0.500000000000000)
        self.doubleSpinBoxOilDiff.setValue(2.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.doubleSpinBoxOilDiff)

        self.label_21 = QLabel(self.groupBoxCashflowSetup)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_21)

        self.doubleSpinBoxGasDiff = QDoubleSpinBox(self.groupBoxCashflowSetup)
        self.doubleSpinBoxGasDiff.setObjectName(u"doubleSpinBoxGasDiff")
        self.doubleSpinBoxGasDiff.setFont(font2)
        self.doubleSpinBoxGasDiff.setSingleStep(0.500000000000000)
        self.doubleSpinBoxGasDiff.setValue(0.500000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.doubleSpinBoxGasDiff)

        self.label_22 = QLabel(self.groupBoxCashflowSetup)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font5)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_22)

        self.spinBoxOPEX = QSpinBox(self.groupBoxCashflowSetup)
        self.spinBoxOPEX.setObjectName(u"spinBoxOPEX")
        self.spinBoxOPEX.setFont(font2)
        self.spinBoxOPEX.setMaximum(100000)
        self.spinBoxOPEX.setSingleStep(500)
        self.spinBoxOPEX.setValue(10000)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.spinBoxOPEX)

        self.label_23 = QLabel(self.groupBoxCashflowSetup)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_23)

        self.doubleSpinBoxCAPEX = QDoubleSpinBox(self.groupBoxCashflowSetup)
        self.doubleSpinBoxCAPEX.setObjectName(u"doubleSpinBoxCAPEX")
        self.doubleSpinBoxCAPEX.setFont(font2)
        self.doubleSpinBoxCAPEX.setValue(8.000000000000000)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.doubleSpinBoxCAPEX)

        self.line_3 = QFrame(self.groupBoxCashflowSetup)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.line_3)

        self.dateEditCashflowEnd = QDateEdit(self.groupBoxCashflowSetup)
        self.dateEditCashflowEnd.setObjectName(u"dateEditCashflowEnd")
        self.dateEditCashflowEnd.setMinimumSize(QSize(0, 18))
        font7 = QFont()
        font7.setFamily(u"Cascadia Code")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.dateEditCashflowEnd.setFont(font7)
        self.dateEditCashflowEnd.setLayoutDirection(Qt.LeftToRight)
        self.dateEditCashflowEnd.setCalendarPopup(True)
        self.dateEditCashflowEnd.setDate(QDate(2025, 6, 1))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEditCashflowEnd)

        self.label_25 = QLabel(self.groupBoxCashflowSetup)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font5)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_25)


        self.gridLayout_3.addWidget(self.groupBoxCashflowSetup, 0, 0, 1, 1)

        self.widget = QWidget(self.tabCashflow)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.widget.setMinimumSize(QSize(600, 300))
        self.pushButtonCreateCashflow = QPushButton(self.widget)
        self.pushButtonCreateCashflow.setObjectName(u"pushButtonCreateCashflow")
        self.pushButtonCreateCashflow.setGeometry(QRect(160, 40, 200, 25))
        sizePolicy2.setHeightForWidth(self.pushButtonCreateCashflow.sizePolicy().hasHeightForWidth())
        self.pushButtonCreateCashflow.setSizePolicy(sizePolicy2)
        self.pushButtonCreateCashflow.setMinimumSize(QSize(200, 0))
        self.pushButtonCreateCashflow.setMaximumSize(QSize(250, 16777215))
        self.pushButtonCreateCashflow.setFont(font2)
        icon10 = QIcon()
        icon10.addFile(u"../../resources/4288590 - objective sight target view vision.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCreateCashflow.setIcon(icon10)
        self.tableViewSummaryValues = QTableView(self.widget)
        self.tableViewSummaryValues.setObjectName(u"tableViewSummaryValues")
        self.tableViewSummaryValues.setGeometry(QRect(30, 80, 500, 191))
        sizePolicy2.setHeightForWidth(self.tableViewSummaryValues.sizePolicy().hasHeightForWidth())
        self.tableViewSummaryValues.setSizePolicy(sizePolicy2)
        self.tableViewSummaryValues.setMinimumSize(QSize(500, 150))
        self.tableViewSummaryValues.setFont(font)
        self.tableViewSummaryValues.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tableViewSummaryValues.setAlternatingRowColors(True)
        self.tableViewSummaryValues.setShowGrid(True)
        self.tableViewSummaryValues.setGridStyle(Qt.DashLine)
        self.tableViewSummaryValues.setSortingEnabled(False)
        self.tableViewSummaryValues.horizontalHeader().setVisible(False)
        self.tableViewSummaryValues.horizontalHeader().setCascadingSectionResizes(True)
        self.tableViewSummaryValues.horizontalHeader().setMinimumSectionSize(150)
        self.tableViewSummaryValues.horizontalHeader().setDefaultSectionSize(150)
        self.tableViewSummaryValues.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)

        self.tableViewCashflow = QTableView(self.tabCashflow)
        self.tableViewCashflow.setObjectName(u"tableViewCashflow")
        sizePolicy1.setHeightForWidth(self.tableViewCashflow.sizePolicy().hasHeightForWidth())
        self.tableViewCashflow.setSizePolicy(sizePolicy1)
        self.tableViewCashflow.setMinimumSize(QSize(200, 700))
        self.tableViewCashflow.setFont(font)
        self.tableViewCashflow.setAlternatingRowColors(True)
        self.tableViewCashflow.setSortingEnabled(False)
        self.tableViewCashflow.horizontalHeader().setCascadingSectionResizes(True)
        self.tableViewCashflow.horizontalHeader().setMinimumSectionSize(150)
        self.tableViewCashflow.horizontalHeader().setDefaultSectionSize(200)
        self.tableViewCashflow.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.tableViewCashflow, 0, 1, 1, 1)

        icon11 = QIcon()
        icon11.addFile(u"../../resources/4288564 - banking business cash income money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabCashflow, icon11, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1398, 18))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font1)
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        self.menu_View = QMenu(self.menubar)
        self.menu_View.setObjectName(u"menu_View")
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        main_window.setMenuBar(self.menubar)
        self.toolBar = QToolBar(main_window)
        self.toolBar.setObjectName(u"toolBar")
        main_window.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menuFile.addAction(self.actionImport_CSV_2)
        self.menuFile.addAction(self.actionImport_Data_SW_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_Cashflow)
        self.menuFile.addAction(self.actionExport_EUR_To_SeisWare)
        self.menu_Help.addAction(self.actionTutorial)
        self.menu_Help.addAction(self.actionDocumentation)
        self.menu_Help.addAction(self.actionWebsite)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionReport_a_bug)
        self.menu_Help.addAction(self.actionPropose_a_new_feauture)
        self.menu_Help.addAction(self.actionBugs_and_feature_requests)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionContact_project_creator)
        self.menu_View.addAction(self.actionComing_Soon)
        self.menu_About.addAction(self.actionCurrent_Version)
        self.menu_About.addSeparator()
        self.menu_About.addAction(self.actionTake_survey_to_improve_the_project)
        self.menu_About.addAction(self.actionDonate)
        self.toolBar.addAction(self.actionImport_CSV)
        self.toolBar.addAction(self.actionImport_Data_SW)

        self.retranslateUi(main_window)
        self.actionImport_CSV.triggered.connect(main_window.import_csv)
        self.comboBoxWellSelect.currentTextChanged.connect(main_window.well_selected)
        self.actionTutorial.triggered.connect(main_window.help_tutorial)
        self.actionDocumentation.triggered.connect(main_window.help_documentation)
        self.actionWebsite.triggered.connect(main_window.help_website)
        self.actionReport_a_bug.triggered.connect(main_window.help_bug)
        self.actionPropose_a_new_feauture.triggered.connect(main_window.help_feature)
        self.actionBugs_and_feature_requests.triggered.connect(main_window.help_open_bugs_features)
        self.actionContact_project_creator.triggered.connect(main_window.help_contact)
        self.actionTake_survey_to_improve_the_project.triggered.connect(main_window.about_take_survey)
        self.actionCurrent_Version.triggered.connect(main_window.about_version)
        self.pushButtonCreateDeclineCurve.clicked.connect(main_window.create_decline_curve)
        self.actionImport_Data_SW.triggered.connect(main_window.import_data)
        self.comboBoxUnits.currentTextChanged.connect(main_window.units_changed)
        self.comboBoxPhase.currentTextChanged.connect(main_window.phase_changed)
        self.pushButtonRemoveDeclineCurves.clicked.connect(main_window.reset_plot)
        self.pushButtonPlotDeclineCurve.clicked.connect(main_window.plot_decline_curves)
        self.pushButtonDeleteDeclineCurve.clicked.connect(main_window.delete_decline_curves)
        self.actionDonate.triggered.connect(main_window.about_donate)
        self.pushButtonCreateCashflow.clicked.connect(main_window.create_cashflow)
        self.actionExport_Cashflow.triggered.connect(main_window.save_cashflow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"PetroAlchemy", None))
        self.actionImport_CSV.setText(QCoreApplication.translate("main_window", u"Import Data", None))
#if QT_CONFIG(tooltip)
        self.actionImport_CSV.setToolTip(QCoreApplication.translate("main_window", u"Select file containing production data", None))
#endif // QT_CONFIG(tooltip)
        self.actionTutorial.setText(QCoreApplication.translate("main_window", u"Tutorial", None))
        self.actionDocumentation.setText(QCoreApplication.translate("main_window", u"Documentation", None))
        self.actionWebsite.setText(QCoreApplication.translate("main_window", u"Website", None))
        self.actionReport_a_bug.setText(QCoreApplication.translate("main_window", u"Report a bug", None))
        self.actionPropose_a_new_feauture.setText(QCoreApplication.translate("main_window", u"Propose a new feauture", None))
        self.actionBugs_and_feature_requests.setText(QCoreApplication.translate("main_window", u"Bugs and feature requests", None))
        self.actionContact_project_creator.setText(QCoreApplication.translate("main_window", u"Contact project creator", None))
        self.actionTake_survey_to_improve_the_project.setText(QCoreApplication.translate("main_window", u"Take survey to improve the project   ", None))
#if QT_CONFIG(tooltip)
        self.actionTake_survey_to_improve_the_project.setToolTip(QCoreApplication.translate("main_window", u"Take survey to improve the project    ", None))
#endif // QT_CONFIG(tooltip)
        self.actionCurrent_Version.setText(QCoreApplication.translate("main_window", u"Current Version  ", None))
        self.actionImport_Data_SW.setText(QCoreApplication.translate("main_window", u"Import SeisWare Data", None))
        self.actionCheck_for_updates.setText(QCoreApplication.translate("main_window", u"Check for updates", None))
        self.actionExport_Cashflow.setText(QCoreApplication.translate("main_window", u"Export Cashflow", None))
        self.actionDonate.setText(QCoreApplication.translate("main_window", u"Donate", None))
        self.actionShow_Cumulative_Volumes.setText(QCoreApplication.translate("main_window", u"Show Cumulative Volumes", None))
        self.actionNormalize_dates_to_Months.setText(QCoreApplication.translate("main_window", u"Normalize Dates to Months", None))
        self.actionShow_Annual_Cashflow.setText(QCoreApplication.translate("main_window", u"Show Annual Cashflow", None))
        self.actionComing_Soon.setText(QCoreApplication.translate("main_window", u"Coming Soon", None))
        self.actionExport_EUR_To_SeisWare.setText(QCoreApplication.translate("main_window", u"Export EUR To SeisWare", None))
        self.actionImport_CSV_2.setText(QCoreApplication.translate("main_window", u"Import CSV Data", None))
        self.actionImport_Data_SW_2.setText(QCoreApplication.translate("main_window", u"Import SeisWare Data", None))
#if QT_CONFIG(tooltip)
        self.comboBoxWellSelect.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comboBoxWellSelect.setCurrentText("")
        self.label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Welcome!</span></p><p>You need to import production data to get started. </p><p>Use at your own discretion. </p><p>This application is open source to provide useful software to engineers and evaluators. </p><p>PetroAlchemy will never require a subscription or fee to use.</p></body></html>", None))
        self.wellListLabel.setText(QCoreApplication.translate("main_window", u"Well List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMainMenu), QCoreApplication.translate("main_window", u"Main Menu", None))
        self.groupBox.setTitle(QCoreApplication.translate("main_window", u"Decline Curve Analysis", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"Select Phase", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"Select Units", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"Start of Decline Curve", None))
#if QT_CONFIG(tooltip)
        self.dateEditCurveStart.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Automatically set as first date in production data</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("main_window", u"Initial Rate", None))
#if QT_CONFIG(tooltip)
        self.spinBoxRate.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Automatically set as max rate of first six months of production data</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("main_window", u"Di (effective %), 1/yr", None))
        self.doubleSpinBoxDi.setSuffix(QCoreApplication.translate("main_window", u"%", None))
        self.label_7.setText(QCoreApplication.translate("main_window", u"B Factor", None))
        self.label_10.setText(QCoreApplication.translate("main_window", u"Minimum Decline (effective %), 1/yr", None))
        self.doubleSpinBoxMinDecline.setSuffix(QCoreApplication.translate("main_window", u"%", None))
        self.label_8.setText(QCoreApplication.translate("main_window", u"Enter New Decline Curve Name", None))
#if QT_CONFIG(tooltip)
        self.pushButtonCreateDeclineCurve.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Creates decline curve from current parameters and saves it under the name entered in the box</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCreateDeclineCurve.setText(QCoreApplication.translate("main_window", u"Create New Decline Curve", None))
        self.label_9.setText(QCoreApplication.translate("main_window", u"Oil Decline Curves", None))
        self.label_24.setText(QCoreApplication.translate("main_window", u"Gas Decline Curves", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUseOil.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Check this to use the Oil Decline Curve with the Remove, Plot, or Delete buttons</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUseOil.setText(QCoreApplication.translate("main_window", u"Use Selected Oil Decline Curve", None))
#if QT_CONFIG(tooltip)
        self.checkBoxUseGas.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Check this to use the Gas Decline Curve with the Remove, Plot, or Delete buttons</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUseGas.setText(QCoreApplication.translate("main_window", u"Use Selected Gas Decline Curve", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRemoveDeclineCurves.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Removes the decline curves from the plot, but does not delete them form the application</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRemoveDeclineCurves.setText(QCoreApplication.translate("main_window", u"Remove Decline Curves", None))
#if QT_CONFIG(tooltip)
        self.pushButtonPlotDeclineCurve.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Plots selected decline curves from the Oil Decline Curves and Gas Decline Curves comboboxes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonPlotDeclineCurve.setText(QCoreApplication.translate("main_window", u"Plot Decline Curves", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDeleteDeclineCurve.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Deletes selected decline curve from the application</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDeleteDeclineCurve.setText(QCoreApplication.translate("main_window", u"Delete Decline Curves", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabForecasting), QCoreApplication.translate("main_window", u"Forecasting", None))
        self.groupBoxCashflowSetup.setTitle(QCoreApplication.translate("main_window", u"Cashflow Parameters", None))
        self.label_11.setText(QCoreApplication.translate("main_window", u"Oil Decline Curve", None))
        self.label_12.setText(QCoreApplication.translate("main_window", u"Gas Decline Curve", None))
        self.label_13.setText(QCoreApplication.translate("main_window", u"Beginning of Cashflow", None))
#if QT_CONFIG(tooltip)
        self.dateEditCashflowStart.setToolTip(QCoreApplication.translate("main_window", u"<html><head/><body><p>Automatically set as first date in production data</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("main_window", u"Working Interest", None))
        self.doubleSpinBoxWorkingInterest.setSuffix(QCoreApplication.translate("main_window", u"%", None))
        self.label_15.setText(QCoreApplication.translate("main_window", u"Net Revenue Interest", None))
        self.doubleSpinBoxNetRevenueInterest.setSuffix(QCoreApplication.translate("main_window", u"%", None))
        self.label_16.setText(QCoreApplication.translate("main_window", u"Primary Annual Discout Rate", None))
        self.spinBoxDiscountRate.setSuffix(QCoreApplication.translate("main_window", u"%", None))
        self.label_17.setText(QCoreApplication.translate("main_window", u"Severance Tax Rate", None))
        self.spinBoxSeveranceTax.setSuffix(QCoreApplication.translate("main_window", u"%", None))
        self.spinBoxSeveranceTax.setPrefix("")
        self.label_18.setText(QCoreApplication.translate("main_window", u"Flat Oil Price", None))
        self.doubleSpinBoxOilPrice.setPrefix(QCoreApplication.translate("main_window", u"$", None))
        self.doubleSpinBoxOilPrice.setSuffix(QCoreApplication.translate("main_window", u"/BBL", None))
        self.label_19.setText(QCoreApplication.translate("main_window", u"Flat Gas Price", None))
        self.doubleSpinBoxGasPrice.setPrefix(QCoreApplication.translate("main_window", u"$", None))
        self.doubleSpinBoxGasPrice.setSuffix(QCoreApplication.translate("main_window", u"/MCF", None))
        self.label_20.setText(QCoreApplication.translate("main_window", u"Oil Differential", None))
        self.doubleSpinBoxOilDiff.setPrefix(QCoreApplication.translate("main_window", u"$", None))
        self.doubleSpinBoxOilDiff.setSuffix(QCoreApplication.translate("main_window", u"/BBL", None))
        self.label_21.setText(QCoreApplication.translate("main_window", u"Gas Differential", None))
        self.doubleSpinBoxGasDiff.setPrefix(QCoreApplication.translate("main_window", u"$", None))
        self.doubleSpinBoxGasDiff.setSuffix(QCoreApplication.translate("main_window", u"/MCF", None))
        self.label_22.setText(QCoreApplication.translate("main_window", u"OPEX", None))
        self.spinBoxOPEX.setSuffix(QCoreApplication.translate("main_window", u"/Month", None))
        self.spinBoxOPEX.setPrefix(QCoreApplication.translate("main_window", u"$", None))
        self.label_23.setText(QCoreApplication.translate("main_window", u"CAPEX", None))
        self.doubleSpinBoxCAPEX.setPrefix(QCoreApplication.translate("main_window", u"$", None))
        self.doubleSpinBoxCAPEX.setSuffix(QCoreApplication.translate("main_window", u" Million", None))
        self.label_25.setText(QCoreApplication.translate("main_window", u"End of Cashflow", None))
        self.pushButtonCreateCashflow.setText(QCoreApplication.translate("main_window", u"Create Cashflow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCashflow), QCoreApplication.translate("main_window", u"Cashflow", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("main_window", u"&Help", None))
        self.menu_View.setTitle(QCoreApplication.translate("main_window", u"&View", None))
        self.menu_About.setTitle(QCoreApplication.translate("main_window", u"&About", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("main_window", u"toolBar", None))
#if QT_CONFIG(tooltip)
        self.toolBar.setToolTip(QCoreApplication.translate("main_window", u"Tooltip", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

