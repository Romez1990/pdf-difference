# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdf-diff.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path
from src.paths import assets_path


class Ui_main_window(object):
    def setupUi(self, Form):
        main_window_path = assets_path / "window_images" / "main_window"

        Form.setObjectName("Form")
        Form.resize(721, 539)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("QPushButton {\n"
                           "    border: 2px solid #8f8f91;\n"
                           "    border-radius: 6px;\n"
                           "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                           "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                           "    min-width: 80px;\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed {\n"
                           "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                           "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                           "}\n"
                           "\n"
                           "QPushButton:flat {\n"
                           "    border: none; /* no border for a flat push button */\n"
                           "}\n"
                           "\n"
                           "QPushButton:default {\n"
                           "    border-color: navy; /* make the default button prominent */\n"
                           "}\n"
                           "\n"
                           "QPushButton:open { /* when the button has its menu open */\n"
                           "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                           "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                           "}\n"
                           "\n"
                           "QPushButton::menu-indicator {\n"
                           "    image: url(menu_indicator.png);\n"
                           "    subcontrol-origin: padding;\n"
                           "    subcontrol-position: bottom right;\n"
                           "}\n"
                           "\n"
                           "QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {\n"
                           "    position: relative;\n"
                           "    top: 2px; left: 2px; /* shift the arrow by 2 px */\n"
                           "}\n"
                           "\n"
                           "\n"
                           "    \n"
                           "\n"
                           "QProgressBar {\n"
                           "    border: 2px solid red;\n"
                           "    border-radius: 5px;\n"
                           "    \n"
                           "}\n"
                           "\n"
                           "QProgressBar::chunk {\n"
                           "    background-color: silver;\n"
                           "    width: 20px;\n"
                           "}\n"
                           "\n"
                           "QComboBox {\n"
                           "    border: 1px solid gray;\n"
                           "    border-radius: 3px;\n"
                           "    padding: 1px 18px 1px 3px;\n"
                           "    min-width: 6em;\n"
                           "}\n"
                           "\n"
                           "\n"
                           "QComboBox:editable {\n"
                           "    background: white;\n"
                           "}\n"
                           "\n"
                           "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                           "     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                           "                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                           "                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                           "}\n"
                           "\n"
                           "/* QComboBox gets the \"on\" state when the popup is open */\n"
                           "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                           "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                           "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                           "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                           "}\n"
                           "\n"
                           "QComboBox:on { /* shift the text when the popup opens */\n"
                           "    padding-top: 3px;\n"
                           "    padding-left: 4px;\n"
                           "}\n"
                           "\n"
                           "QComboBox::drop-down {\n"
                           "    subcontrol-origin: padding;\n"
                           "    subcontrol-position: top right;\n"
                           "    width: 15px;\n"
                           "\n"
                           "    border-left-width: 1px;\n"
                           "    border-left-color: darkgray;\n"
                           "    border-left-style: solid; /* just a single line */\n"
                           "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                           "    border-bottom-right-radius: 3px;\n"
                           "}\n"
                           "\n"
                           "QComboBox::down-arrow {\n"
                           "    \n"
                           "    image: url((str(assets_path / window_images / down-arrow.png)));\n"
                           "}\n"
                           "\n"
                           "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                           "    top: 1px;\n"
                           "    left: 1px;\n"
                           "}\n"
                           "\n"
                           "url(:/newPrefix/photoshop-background-png-24711.png)\n"
                           "")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 721, 541))
        self.label_5.setText("")
        self.label_5.setPixmap(
            QtGui.QPixmap(str(main_window_path / "main_window_background.jpg")))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(310, 220, 81, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(str(main_window_path / "data-transfer.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(320, 390, 64, 64))
        self.label_8.setText("")
        self.movie = QtGui.QMovie(str(main_window_path / "loading.gif"))
        self.label_8.setMovie(self.movie)
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(170, 300, 101, 21))
        self.pushButton_1.setStyleSheet("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 320, 101, 21))
        self.textEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_2.setObjectName("textEdit_2")
        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setGeometry(QtCore.QRect(290, 360, 118, 23))
        self.progressBar_2.setStyleSheet("")
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 320, 101, 31))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 100, 151, 101))
        self.label_7.setStyleSheet("QFrame, QLabel, QToolTip {\n"
                                   "    padding: 2px;\n"
                                   "    text-align: center;\n"
                                   "    font-size: 20px;\n"
                                   "    font-family: \"Times New Roman\", Georgia, Serif;\n"
                                   "    font-weight: bold;\n"
                                   "    font-style: oblique;\n"
                                   "\n"
                                   "}")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(str(main_window_path / "scales.png")))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 300, 101, 21))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_1")
        self.textEdit_1 = QtWidgets.QTextEdit(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(420, 320, 101, 21))
        self.textEdit_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_1.setObjectName("textEdit_1")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(180, 220, 91, 71))
        self.label_9.setStyleSheet("QFrame, QLabel, QToolTip {\n"
                                   "    \n"
                                   "    padding: 2px;\n"
                                   "    text-align: center;\n"
                                   "    font-family: \"Times New Roman\", Georgia, Serif;\n"
                                   "    font-weight: bold;\n"
                                   "    font-style: oblique;\n"
                                   "    font-size: large;\n"
                                   "\n"
                                   "}")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(str(main_window_path / "pdf.png")))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(420, 220, 91, 71))
        self.label_10.setStyleSheet("QFrame, QLabel, QToolTip {\n"
                                    "    \n"
                                    "    padding: 2px;\n"
                                    "    text-align: center;\n"
                                    "    font-family: \"Times New Roman\", Georgia, Serif;\n"
                                    "    font-weight: bold;\n"
                                    "    font-style: oblique;\n"
                                    "    font-size: large;\n"
                                    "\n"
                                    "}")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(str(main_window_path / "pdf.png")))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PDF comp"))
        self.pushButton_1.setText(_translate("Form", "Browse"))
        self.pushButton_2.setText(_translate("Form", "Compare"))
        self.pushButton_3.setText(_translate("Form", "Browse"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_main_window()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())