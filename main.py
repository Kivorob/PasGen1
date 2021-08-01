import sys, random, pyperclip
from PyQt5 import QtWidgets
from test import Ui_MainWindow, Ui_authorWidget
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
authorWidget = QtWidgets.QWidget()
a_ui = Ui_authorWidget()
a_ui.setupUi(authorWidget)
MainWindow.show()


def generate():
    text = ui.lineEdit.text()
    Diff = -1
    try:
        check = int(text)
        number = int(text)
    except:
        ui.lineEdit.setText("Укажите длину!")
        number = -1
    password = ''
    if ui.radioButton.isChecked():
       chars_int = '+-/*!&=@<>1234567890'
       for x in range(number):
            password += random.choice(chars_int)
            ui.lineEdit_2.setText(str(password))
       Kf = 0

    if ui.radioButton_2.isChecked():
       chars_lit = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ'
       for x in range(number):
            password += random.choice(chars_lit)
            ui.lineEdit_2.setText(str(password))
       Kf = 1

    if ui.radioButton_3.isChecked():
       chars_lit = '+-/*!&=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ1234567890'
       for x in range(number):
            password += random.choice(chars_lit)
            ui.lineEdit_2.setText(str(password))
       Kf = 2

    if ui.radioButton_4.isChecked():
       chars_lit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
       for x in range(number):
            password += random.choice(chars_lit)
            ui.lineEdit_2.setText(str(password))
       Kf = 3

    if ui.radioButton_5.isChecked():
       chars_lit = '+-/*!&=@<>абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890'
       for x in range(number):
            password += random.choice(chars_lit)
            ui.lineEdit_2.setText(str(password))
       Kf = 4

    if ui.radioButton_6.isChecked():
       chars_lit = '+-/*!&=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890'
       for x in range(number):
            password += random.choice(chars_lit)
            ui.lineEdit_2.setText(str(password))
       Kf = 5

    Diff = (Kf + 1) * number

    if  Diff < 50 and Diff > 0:

        ui.label_4.setText("Weak password - " + str(Diff))
        ui.label_4.setStyleSheet("color: red; font-size: 18px; background-color: #bcee00;")

    if Diff >= 50 and Diff < 100:
        ui.label_4.setText("Normal password - " + str(Diff))
        ui.label_4.setStyleSheet("color: #6ed5ff; font-size: 18px; background-color: #1b00f3;")

    if Diff >= 100:
        ui.label_4.setText("Strong password - " + str(Diff))
        ui.label_4.setStyleSheet("color: #8f6300; font-size: 18px; background-color: #bcee00;")


    if Diff == -1:
        ui.lineEdit_2.setText("Выберите тип пароля")

def clear():
    ui.lineEdit.clear()
    ui.lineEdit_2.clear()

def openWidget():
    authorWidget.show()

def copyPassword():
    pyperclip.copy(ui.lineEdit_2.text())

def lovePage():
    a_ui.closeButton.setGeometry(120, 190, 120, 60)
    a_ui.closeButton.setStyleSheet("background-color: pink; color: purple;")
    a_ui.loveButton.setGeometry(0, 0, 0, 0)
    a_ui.centralWidget.setStyleSheet("background-color:#ca00e8")
    a_ui.label.setGeometry(0, 0, 0, 0)
    a_ui.label_2.setGeometry(0, 0, 0, 0)
    a_ui.label_3.setGeometry(0, 0, 0, 0)
    a_ui.label_4.setGeometry(65, 100, 250, 30)
    a_ui.label_4.setStyleSheet("font-size: 24px; color: gold;")
    a_ui.label_4.setText("От души, Братюнь =)")

def closeWidget():
    authorWidget.close()

ui.pushButton.clicked.connect(generate)
ui.pushButton_2.clicked.connect(clear)
ui.pushButton_3.clicked.connect(openWidget)
ui.pushButton_4.clicked.connect(copyPassword)
a_ui.loveButton.clicked.connect(lovePage)
a_ui.closeButton.clicked.connect(closeWidget)
sys.exit(app.exec_())
