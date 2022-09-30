#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Создание простейшей визуальной '
                            'программы на Python')

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # Задание картинки с заданием с масштабированием в компоненте
        self.label_img.setPixmap(QPixmap('main.png'))
        self.label_img.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)
        self.lineEdit_c.setVisible(False)
        self.label_c.setVisible(False)
        self.lineEdit_x.textChanged.connect(lambda text, obj=self.lineEdit_x: self.text_Changed(text))



    def text_Changed(self, text):
        try:
            k = int(text)
            if k < 4:
                self.lineEdit_c.setVisible(True)
                self.label_c.setVisible(True)
            else:
                self.lineEdit_c.setVisible(False)
                self.label_c.setVisible(False)
        except:
            self.lineEdit_c.setVisible(False)
            self.label_c.setVisible(False)

    # Процедура решения примера
    def solve(self):
        try:
            self.colorLineEdits()
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x < 4:
                c = float(self.lineEdit_c.text())
                y = pow(x,2)+pow(a,2)*c/(2*b);
            else:
                y = pow(x,3)*(a-b);
            self.label_answer.setText('Ответ: ' + str(format(y, '.2f')))
            self.label_answer.setStyleSheet("border: 1px solid green;")

        except:
            self.label_answer.setText(
                'Ошибка!')
            self.label_answer.setStyleSheet("border: 1px solid red;")
            # self.lineEdit_a.setStyleSheet("border: 1px solid red;")
            # self.lineEdit_b.setStyleSheet("border: 1px solid red;")
            # self.lineEdit_x.setStyleSheet("border: 1px solid red;")


    # Процедура очистки данных
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')


        self.label_answer.setStyleSheet("")
        self.lineEdit_a.setStyleSheet("")
        self.lineEdit_b.setStyleSheet("")
        self.lineEdit_x.setStyleSheet("")

    def colorLineEdits(self):
        self.colorChange(self.lineEdit_a)
        self.colorChange(self.lineEdit_b)
        self.colorChange(self.lineEdit_x)
        self.colorChange(self.lineEdit_c)

    def colorChange(self, obj):
        print(obj.text())
        try:
            int(obj.text())
            obj.setStyleSheet("border: 1px solid green;")
        except:
            obj.setStyleSheet("border: 1px solid red;")




# Основная часть программы
app = QApplication(sys.argv)
window = Main()  # базовый класс окна
window.show()  # отобразить окно на экране
sys.exit(app.exec_())  # запуск основного цикла приложения
