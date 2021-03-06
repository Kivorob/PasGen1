from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 320)
        MainWindow.setMinimumSize(QtCore.QSize(558, 320))
        MainWindow.setMaximumSize(QtCore.QSize(558, 320))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #c4ff65")
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 65, 211, 21))
        self.radioButton_2.setStyleSheet("font-size:16px;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 71, 21))
        self.label_2.setStyleSheet("font-size: 18px;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 210, 421, 20))
        self.lineEdit_2.setStyleSheet("border-radius: 18px; background-color: #ffef76; font-size: 18px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(455, 210, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("font-size:18px; font-family: Verdana; background-color: #ffd7aa;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 10, 111, 21))
        self.label_3.setStyleSheet("font-size:18px;")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.label.setStyleSheet("font-size:18px;")
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(220, 40, 131, 21))
        self.radioButton.setStyleSheet("font-size:16px;")
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 45, 141, 20))
        self.lineEdit.setStyleSheet("border: solid; border-radius: 18px; background-color: #ffef76; font-size:18px;")
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(220, 90, 231, 21))
        self.radioButton_3.setStyleSheet("font-size:16px;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 260, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font-size:16px; font-family: Verdana; background-color: #ffd7aa;")
        self.pushButton.setObjectName("pushButton")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(220, 115, 221, 21))
        self.radioButton_4.setStyleSheet("font-size:16px;")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 260, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("font-size:16px; font-family: Verdana; background-color: #ffd7aa;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 260, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("font-size:16px; font-family: Verdana; background-color: #ffd7aa;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(220, 140, 241, 21))
        self.radioButton_5.setStyleSheet("font-size:16px;")
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(220, 165, 241, 21))
        self.radioButton_6.setStyleSheet("font-size:16px;")
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(10, 100, 180, 20)
        self.label_4.setStyleSheet("font-size: 18px;")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????? ??????????????"))
        self.radioButton_2.setText(_translate("MainWindow", "????????????????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.label_3.setText(_translate("MainWindow", "?????? ????????????"))
        self.label.setText(_translate("MainWindow", "?????????? ????????????"))
        self.pushButton.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "Copy"))
        self.pushButton_3.setText(_translate("MainWindow", "??????????"))
        self.radioButton_3.setText(_translate("MainWindow", "???????????????? ?? ??????????"))
        self.radioButton.setText(_translate("MainWindow", "??????????"))
        self.radioButton_4.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????????????"))
        self.radioButton_5.setText(_translate("MainWindow", "?????????????????? ?? ??????????"))
        self.radioButton_6.setText(_translate("MainWindow", "???????????? ??????????"))
        self.label_4.setText(_translate("MainWindow", "????????????????????:"))


class Ui_authorWidget(object):
    def setupUi(self, authorWidget):
        authorWidget.setObjectName("authorWidget")
        authorWidget.resize(360, 270)
        authorWidget.setMinimumSize(QtCore.QSize(360, 270))
        authorWidget.setMaximumSize(QtCore.QSize(360, 270))
        self.centralWidget = QtWidgets.QWidget(authorWidget)
        self.centralWidget.setGeometry(0, 0, 360, 270)
        self.centralWidget.setStyleSheet("background-color: #97ff00")
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(85, 100, 100, 30))
        self.label.setStyleSheet("font-size:24px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(180, 100, 100, 30))
        self.label_2.setStyleSheet("font-size:24px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(60, 45, 100, 30))
        self.label_3.setStyleSheet("font-size: 24px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(180, 45, 100, 30))
        self.label_4.setStyleSheet("font-size: 24px;")
        self.label_4.setObjectName("label_4")
        self.closeButton = QtWidgets.QPushButton(self.centralWidget)
        self.closeButton.setGeometry(QtCore.QRect(10, 190, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("font-size: 16px; font-family: Verdana; background-color: #ffd675;")
        self.closeButton.setObjectName("closeButton")
        self.loveButton = QtWidgets.QPushButton(self.centralWidget)
        self.loveButton.setGeometry(QtCore.QRect(230, 190, 120, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.loveButton.setFont(font)
        self.loveButton.setStyleSheet("font-size: 16px; font-family: Verdana; background-color: #ffd675;")
        self.loveButton.setObjectName("loveButton")

        self.retranslateUi(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(authorWidget)

    def retranslateUi(self, authorWidget):
        _translate = QtCore.QCoreApplication.translate
        authorWidget.setWindowTitle(_translate("authorWidget", "??????-???? ???????? ?????????????? ???? ????????????"))
        self.centralWidget.setWindowTitle(_translate("authorWidget", "??????????"))
        self.label.setText(_translate("authorWidget", "??????????: "))
        self.label_2.setText(_translate("authorWidget", "Kivorob"))
        self.label_3.setText(_translate("authorWidget", "????????????: "))
        self.label_4.setText(_translate("authorWidget", "??????????"))
        self.closeButton.setText(_translate("authorWidget", "??????????????"))
        self.loveButton.setText(_translate("authorWidget", "??????????????????"))