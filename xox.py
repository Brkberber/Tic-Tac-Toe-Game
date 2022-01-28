# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_1.setGeometry(QtCore.QRect(5, 5, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_1.setFont(font)
        self.pb_1.setText("")
        self.pb_1.setObjectName("pb_1")
        self.pb_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_2.setGeometry(QtCore.QRect(110, 5, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_2.setFont(font)
        self.pb_2.setText("")
        self.pb_2.setObjectName("pb_2")
        self.pb_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_3.setGeometry(QtCore.QRect(215, 5, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_3.setFont(font)
        self.pb_3.setText("")
        self.pb_3.setObjectName("pb_3")
        self.pb_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_5.setGeometry(QtCore.QRect(110, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_5.setFont(font)
        self.pb_5.setText("")
        self.pb_5.setObjectName("pb_5")
        self.pb_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_4.setGeometry(QtCore.QRect(5, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_4.setFont(font)
        self.pb_4.setText("")
        self.pb_4.setObjectName("pb_4")
        self.pb_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_6.setGeometry(QtCore.QRect(215, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_6.setFont(font)
        self.pb_6.setText("")
        self.pb_6.setObjectName("pb_6")
        self.pb_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_8.setGeometry(QtCore.QRect(110, 215, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_8.setFont(font)
        self.pb_8.setText("")
        self.pb_8.setObjectName("pb_8")
        self.pb_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_9.setGeometry(QtCore.QRect(215, 215, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_9.setFont(font)
        self.pb_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pb_9.setText("")
        self.pb_9.setObjectName("pb_9")
        self.pb_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_7.setGeometry(QtCore.QRect(5, 215, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pb_7.setFont(font)
        self.pb_7.setText("")
        self.pb_7.setObjectName("pb_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 320, 320, 50))
        self.label.setStyleSheet("QLabel {\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.restart = QtWidgets.QPushButton(self.centralwidget)
        self.restart.setGeometry(QtCore.QRect(5, 375, 310, 60))
        self.restart.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.restart.setObjectName("restart")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
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
        self.label.setText(_translate("MainWindow", "X Goes First!"))
        self.restart.setText(_translate("MainWindow", "Start Over"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

