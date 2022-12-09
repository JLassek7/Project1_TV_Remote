# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remote.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 577)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        MainWindow.setMaximumSize(QtCore.QSize(300, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.power_button = QtWidgets.QPushButton(self.centralwidget)
        self.power_button.setGeometry(QtCore.QRect(200, 20, 81, 31))
        self.power_button.setObjectName("power_button")
        self.volume_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.volume_up_button.setGeometry(QtCore.QRect(190, 320, 71, 41))
        self.volume_up_button.setObjectName("volume_up_button")
        self.volume_down_button = QtWidgets.QPushButton(self.centralwidget)
        self.volume_down_button.setGeometry(QtCore.QRect(190, 390, 71, 41))
        self.volume_down_button.setObjectName("volume_down_button")
        self.channel_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.channel_up_button.setGeometry(QtCore.QRect(50, 320, 71, 41))
        self.channel_up_button.setObjectName("channel_up_button")
        self.channel_down_button = QtWidgets.QPushButton(self.centralwidget)
        self.channel_down_button.setGeometry(QtCore.QRect(50, 390, 71, 41))
        self.channel_down_button.setObjectName("channel_down_button")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(180, 260, 71, 20))
        self.volume_label.setObjectName("volume_label")
        self.mute_button = QtWidgets.QPushButton(self.centralwidget)
        self.mute_button.setGeometry(QtCore.QRect(120, 460, 71, 41))
        self.mute_button.setObjectName("mute_button")
        self.volume_level = QtWidgets.QLineEdit(self.centralwidget)
        self.volume_level.setGeometry(QtCore.QRect(230, 260, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.volume_level.setFont(font)
        self.volume_level.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.volume_level.setReadOnly(True)
        self.volume_level.setObjectName("volume_level")
        self.tv_screen = QtWidgets.QLabel(self.centralwidget)
        self.tv_screen.setGeometry(QtCore.QRect(10, 60, 271, 181))
        self.tv_screen.setText("")
        self.tv_screen.setObjectName("tv_screen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TV Remote"))
        self.power_button.setText(_translate("MainWindow", "Power"))
        self.volume_up_button.setText(_translate("MainWindow", "Volume +"))
        self.volume_down_button.setText(_translate("MainWindow", "Volume -"))
        self.channel_up_button.setText(_translate("MainWindow", "Channel + "))
        self.channel_down_button.setText(_translate("MainWindow", "Channel -"))
        self.volume_label.setText(_translate("MainWindow", "Volume:"))
        self.mute_button.setText(_translate("MainWindow", "Mute"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())