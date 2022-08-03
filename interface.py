from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from time import sleep
import pyautogui as pgui
import mss

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(142, 132)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color : #37e668")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 0, 71, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color : #e64937")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 30, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 60, 71, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 60, 71, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 142, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Def Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Def Stop"))
        self.pushButton_3.setText(_translate("MainWindow", "Aura Start"))
        self.pushButton_4.setText(_translate("MainWindow", "Aura Stop"))
        self.pushButton_5.setText(_translate("MainWindow", "Flask Start"))
        self.pushButton_6.setText(_translate("MainWindow", "Flask Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

defense_act_orig = [[[39, 30, 128, 255]]]  # Эталон уровня включения защиты


def def_start():
    """Проверяем хп и включаем защиту"""
    flag = True  # Условие запуска защиты
    while flag:
        with mss.mss() as sct:
            monitor = {"top": 900, "left": 99, "width": 1, "height": 1}
            defense_act_new = np.array(sct.grab(monitor))

        if defense_act_orig[0][0][0] != defense_act_new[0][0][0]:
            print(flag)
            pgui.press('t')
            sleep(4)
            continue
        elif ui.pushButton_2.clicked:
            flag = False
            print('ff')
        else:
            sleep(0.1)
            print(("sss"))
def def_stop():
    pass

ui.pushButton.clicked.connect(def_start)
ui.pushButton_2.clicked.connect(def_stop)

sys.exit(app.exec_())
