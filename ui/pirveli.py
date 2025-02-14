from PyQt5 import QtCore, QtGui, QtWidgets
from kerdzebisgverdi import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1298, 947)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color:\n"
"rgb(255, 252, 255)")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 12, 1251, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(1251, 600))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1978203.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 350, 591, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(2000, 1000))
        self.pushButton_4.setStyleSheet("color:rgb(136, 114, 115);\n"
"\n"
"\n"
"font-size:20pt,")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(530, 150, 221, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(1000, 1000))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 150, 271, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(5000, 10000))
        self.label_8.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:18pt")
        self.label_8.setObjectName("label_8")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(750, 150, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMaximumSize(QtCore.QSize(10000, 10000))
        self.pushButton_11.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:14pt")
        self.pushButton_11.setObjectName("pushButton_11")
        self.turkey = QtWidgets.QPushButton(self.centralwidget)
        self.turkey.setGeometry(QtCore.QRect(1000, 410, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turkey.sizePolicy().hasHeightForWidth())
        self.turkey.setSizePolicy(sizePolicy)
        self.turkey.setMaximumSize(QtCore.QSize(1000, 1000))
        self.turkey.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:14pt")
        self.turkey.setObjectName("turkey")
        self.japan = QtWidgets.QPushButton(self.centralwidget)
        self.japan.setGeometry(QtCore.QRect(660, 660, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.japan.sizePolicy().hasHeightForWidth())
        self.japan.setSizePolicy(sizePolicy)
        self.japan.setMaximumSize(QtCore.QSize(1000, 1000))
        self.japan.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:14pt")
        self.japan.setObjectName("japan")
        self.kerdzebi = QtWidgets.QPushButton(self.centralwidget)
        self.kerdzebi.setGeometry(QtCore.QRect(10, 450, 221, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kerdzebi.sizePolicy().hasHeightForWidth())
        self.kerdzebi.setSizePolicy(sizePolicy)
        self.kerdzebi.setMinimumSize(QtCore.QSize(0, 0))
        self.kerdzebi.setMaximumSize(QtCore.QSize(1000, 1000))
        self.kerdzebi.setStyleSheet("color:rgb(136, 114, 115);\n"
"font: 8pt \"MS Gothic\";\n"
"font-size:18pt\n"
"")
        self.kerdzebi.setObjectName("kerdzebi")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.kerdzebi.clicked.connect(self.go_to_kerdzebi)
        self.label_2.setGeometry(QtCore.QRect(260, 440, 191, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(191, 191))
        self.label_2.setStyleSheet("border-radius: 20px;\n"
"    border: 5px solid #600;\n"
"    background: #f0f0f0;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("8d5089b2f32550b3257e8974000d86ad.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 690, 191, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(191, 191))
        self.label_6.setStyleSheet("border-radius: 20px;\n"
"    border: 5px solid #600;\n"
"    background: #f0f0f0;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("eae51f67353480505804ee6615f4e725.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(990, 690, 191, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(191, 191))
        self.label_7.setStyleSheet("border-radius: 20px;\n"
"    border: 5px solid #600;\n"
"    background: #f0f0f0;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("e3242a6aa3507a14fd7436399f35a3c5.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 350, 231, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(1000, 1000))
        self.textBrowser.setObjectName("textBrowser")
        self.wasaxemsebeli = QtWidgets.QPushButton(self.centralwidget)
        self.wasaxemsebeli.setEnabled(True)
        self.wasaxemsebeli.setGeometry(QtCore.QRect(13, 550, 221, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wasaxemsebeli.sizePolicy().hasHeightForWidth())
        self.wasaxemsebeli.setSizePolicy(sizePolicy)
        self.wasaxemsebeli.setMinimumSize(QtCore.QSize(0, 0))
        self.wasaxemsebeli.setMaximumSize(QtCore.QSize(10000, 10000))
        self.wasaxemsebeli.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:18pt")
        self.wasaxemsebeli.setObjectName("wasaxemsebeli")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 440, 191, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(191, 191))
        self.label_3.setStyleSheet("border-radius: 20px;\n"
"    border: 5px solid #600;\n"
"    background: #f0f0f0;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("9b56ab2133642cff30498e011e02b942.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.desertebi = QtWidgets.QPushButton(self.centralwidget)
        self.desertebi.setGeometry(QtCore.QRect(10, 670, 221, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desertebi.sizePolicy().hasHeightForWidth())
        self.desertebi.setSizePolicy(sizePolicy)
        self.desertebi.setMinimumSize(QtCore.QSize(0, 0))
        self.desertebi.setMaximumSize(QtCore.QSize(1000, 50))
        self.desertebi.setStyleSheet("font: 16pt \"MS Gothic\";\n"
"color:rgb(136, 114, 115)")
        self.desertebi.setIconSize(QtCore.QSize(20, 20))
        self.desertebi.setObjectName("desertebi")
        self.france = QtWidgets.QPushButton(self.centralwidget)
        self.france.setGeometry(QtCore.QRect(1000, 660, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.france.sizePolicy().hasHeightForWidth())
        self.france.setSizePolicy(sizePolicy)
        self.france.setMaximumSize(QtCore.QSize(1000, 1000))
        self.france.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:14pt")
        self.france.setObjectName("france")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 690, 191, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(191, 191))
        self.label_5.setStyleSheet("border-radius: 20px;\n"
"    border: 5px solid #600;\n"
"    background: #f0f0f0;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("666ab5cc632f3d64f6d1a1ff5b1b9255.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(990, 440, 191, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(191, 191))
        self.label_4.setStyleSheet("border-radius: 20px;\n"
"    border: 5px solid #600;\n"
"    background: #f0f0f0;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("b525e685c49affbd8c4745df56b4b5c2.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.italy = QtWidgets.QPushButton(self.centralwidget)
        self.italy.setGeometry(QtCore.QRect(650, 410, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.italy.sizePolicy().hasHeightForWidth())
        self.italy.setSizePolicy(sizePolicy)
        self.italy.setMaximumSize(QtCore.QSize(1000, 1000))
        self.italy.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:14pt")
        self.italy.setObjectName("italy")
        self.mexico = QtWidgets.QPushButton(self.centralwidget)
        self.mexico.setGeometry(QtCore.QRect(270, 660, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mexico.sizePolicy().hasHeightForWidth())
        self.mexico.setSizePolicy(sizePolicy)
        self.mexico.setMaximumSize(QtCore.QSize(1000, 1000))
        self.mexico.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:14pt")
        self.mexico.setObjectName("mexico")
        self.georgia = QtWidgets.QPushButton(self.centralwidget)
        self.georgia.setGeometry(QtCore.QRect(280, 410, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.georgia.sizePolicy().hasHeightForWidth())
        self.georgia.setSizePolicy(sizePolicy)
        self.georgia.setMaximumSize(QtCore.QSize(1000, 1000))
        self.georgia.setStyleSheet("color:rgb(136, 114, 115);\n"
"font-size:14pt")
        self.georgia.setObjectName("georgia")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 200, 461, 51))
        self.pushButton.setStyleSheet("color:rgb(136, 114, 115);\n"
"\n"
"\n"
"font-size:20pt,")
        self.pushButton.setObjectName("pushButton")
        self.turkey.raise_()
        self.japan.raise_()
        self.kerdzebi.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.textBrowser.raise_()
        self.wasaxemsebeli.raise_()
        self.label_3.raise_()
        self.desertebi.raise_()
        self.france.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.italy.raise_()
        self.mexico.raise_()
        self.georgia.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.pushButton_4.raise_()
        self.pushButton_11.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1298, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "სხვადასხვა ქვეყნის სამზარეულო"))
        self.label_8.setText(_translate("MainWindow", "მოძებნეთ რეცეპტი"))
        self.pushButton_11.setText(_translate("MainWindow", "ძებნა"))
        self.turkey.setText(_translate("MainWindow", "თურქეთი"))
        self.japan.setText(_translate("MainWindow", "იაპონია"))
        self.kerdzebi.setText(_translate("MainWindow", "კერძი"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#887273;\">კატეგორიები</span></p></body></html>"))
        self.wasaxemsebeli.setText(_translate("MainWindow", "წასახემსებელი"))
        self.desertebi.setText(_translate("MainWindow", "დესერტი"))
        self.france.setText(_translate("MainWindow", "საფრანგეთი"))
        self.italy.setText(_translate("MainWindow", "იტალია"))
        self.mexico.setText(_translate("MainWindow", "მექსიკა"))
        self.georgia.setText(_translate("MainWindow", "საქართველო "))
        self.pushButton.setText(_translate("MainWindow", "ინგრედიენტებით ძებნა"))

    def go_to_kerdzebi(self):
            self.kerdzebi_window = QtWidgets.QMainWindow()
            self.kerdzebi_ui = Ui_Form()
            self.kerdzebi_ui.setupUi(self.kerdzebi_window)

            self.kerdzebi_window.show()
import sys
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())