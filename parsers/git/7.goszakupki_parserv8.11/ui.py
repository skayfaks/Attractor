# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QMessageBox
import time

# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.pbar = QtWidgets.QProgressBar(self)
#         self.pbar.setGeometry(10,20, 200, 25)
#         self.pbar.setValue(0)
#
#         self.setWindowTitle("Прогресс загрузки:")
#         self.setGeometry(32, 32, 320, 200)
#         self.show()
#         last_page = 0
#         # self.timer = QTimer()
#         # self.timer.timeout.connect(self.handleTimer(last_page))
#         # self.timer.start(1000)


    # def handleTimer(self,page, last_page):
    #     value = self.pbar.value()
    #     prog = (page/last_page)*100
    #     if value < 100:
    #         value = prog
    #         self.pbar.setValue(value)
    #         if value == 100:
    #             self.pbar.setValue(0)
    #             QMessageBox.about(self, "Внимание", "Загрузка завершена")

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        Form.setObjectName("Парсер Gosuslugi")
        Form.resize(652, 516)
        Form.setFixedSize(652, 516)
        Form.setWindowIcon(QtGui.QIcon('sonic.ico'))
        Form.setStyleSheet("\n"
"QlineEdit {\n"
"    background-color:black\n"
"}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 151, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_reg2 = QtWidgets.QPushButton(Form)
        self.pushButton_reg2.setGeometry(QtCore.QRect(250, 80, 151, 41))
        self.pushButton_reg2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_reg2.setObjectName("pushButton_reg2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(320, 10, 101, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(420, 10, 111, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(320, 30, 121, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(440, 30, 121, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(170, 30, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_1 = QtWidgets.QDateEdit(Form)
        self.dateEdit_1.setGeometry(QtCore.QRect(170, 50, 110, 22))
        self.dateEdit_1.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 147, 17))
        self.label_2.setObjectName("label_2")
        # self.progressBar = QtWidgets.QProgressBar(Form)
        # self.progressBar.setEnabled(True)
        # self.progressBar.setGeometry(QtCore.QRect(10, 470, 631, 23))
        #self.progressBar.setProperty("value", 24)
        #self.progressBar.setObjectName("progressBar")
        """Чекбоксы регионов"""
        self.checkBox_reg1 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg1.setGeometry(QtCore.QRect(10, 130, 121, 17))
        self.checkBox_reg1.setObjectName("checkBox_reg1")
        self.checkBox_reg2 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg2.setGeometry(QtCore.QRect(10, 150, 121, 17))
        self.checkBox_reg2.setObjectName("checkBox_reg2")
        self.checkBox_reg3 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg3.setGeometry(QtCore.QRect(10, 170, 121, 17))
        self.checkBox_reg3.setObjectName("checkBox_reg3")
        self.checkBox_reg4 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg4.setGeometry(QtCore.QRect(10, 190, 121, 17))
        self.checkBox_reg4.setObjectName("checkBox_reg4")
        self.checkBox_reg5 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg5.setGeometry(QtCore.QRect(10, 210, 121, 17))
        self.checkBox_reg5.setObjectName("checkBox_reg5")
        self.checkBox_reg6 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg6.setGeometry(QtCore.QRect(10, 230, 121, 17))
        self.checkBox_reg6.setObjectName("checkBox_reg6")
        self.checkBox_reg7 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg7.setGeometry(QtCore.QRect(10, 250, 121, 17))
        self.checkBox_reg7.setObjectName("checkBox_reg7")
        self.checkBox_reg8 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg8.setGeometry(QtCore.QRect(10, 270, 121, 17))
        self.checkBox_reg8.setObjectName("checkBox_reg8")
        self.checkBox_reg9 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg9.setGeometry(QtCore.QRect(10, 290, 121, 17))
        self.checkBox_reg9.setObjectName("checkBox_reg9")
        self.checkBox_reg10 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg10.setGeometry(QtCore.QRect(10, 310, 121, 17))
        self.checkBox_reg10.setObjectName("checkBox_reg10")
        self.checkBox_reg11 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg11.setGeometry(QtCore.QRect(10, 330, 121, 17))
        self.checkBox_reg11.setObjectName("checkBox_reg11")
        self.checkBox_reg12 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg12.setGeometry(QtCore.QRect(10, 350, 150, 17))
        self.checkBox_reg12.setObjectName("checkBox_reg12")
        self.checkBox_reg13 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg13.setGeometry(QtCore.QRect(10, 370, 121, 17))
        self.checkBox_reg13.setObjectName("checkBox_reg13")
        self.checkBox_reg14 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg14.setGeometry(QtCore.QRect(10, 390, 121, 17))
        self.checkBox_reg14.setObjectName("checkBox_reg14")
        self.checkBox_reg15 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg15.setGeometry(QtCore.QRect(10, 410, 121, 17))
        self.checkBox_reg15.setObjectName("checkBox_reg15")
        self.checkBox_reg16 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg16.setGeometry(QtCore.QRect(10, 430, 121, 17))
        self.checkBox_reg16.setObjectName("checkBox_reg16")
        self.checkBox_reg17 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg17.setGeometry(QtCore.QRect(10, 450, 121, 17))
        self.checkBox_reg17.setObjectName("checkBox_reg17")
        self.checkBox_reg18 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg18.setGeometry(QtCore.QRect(170, 130, 121, 17))
        self.checkBox_reg18.setObjectName("checkBox_reg18")
        self.checkBox_reg19 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg19.setGeometry(QtCore.QRect(170, 150, 121, 17))
        self.checkBox_reg19.setObjectName("checkBox_reg19")
        self.checkBox_reg20 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg20.setGeometry(QtCore.QRect(170, 170, 121, 17))
        self.checkBox_reg20.setObjectName("checkBox_reg20")
        self.checkBox_reg21 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg21.setGeometry(QtCore.QRect(170, 190, 121, 17))
        self.checkBox_reg21.setObjectName("checkBox_reg21")
        self.checkBox_reg22 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg22.setGeometry(QtCore.QRect(170, 210, 121, 17))
        self.checkBox_reg22.setObjectName("checkBox_reg22")
        self.checkBox_reg23 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg23.setGeometry(QtCore.QRect(170, 230, 121, 17))
        self.checkBox_reg23.setObjectName("checkBox_reg23")
        self.checkBox_reg24 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg24.setGeometry(QtCore.QRect(170, 250, 121, 17))
        self.checkBox_reg24.setObjectName("checkBox_reg24")
        self.checkBox_reg25 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg25.setGeometry(QtCore.QRect(170, 270, 121, 17))
        self.checkBox_reg25.setObjectName("checkBox_reg25")
        self.checkBox_reg26 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg26.setGeometry(QtCore.QRect(170, 290, 121, 17))
        self.checkBox_reg26.setObjectName("checkBox_reg26")
        self.checkBox_reg27 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg27.setGeometry(QtCore.QRect(170, 310, 121, 17))
        self.checkBox_reg27.setObjectName("checkBox_reg27")
        self.checkBox_reg28 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg28.setGeometry(QtCore.QRect(170, 330, 121, 17))
        self.checkBox_reg28.setObjectName("checkBox_reg28")
        self.checkBox_reg29 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg29.setGeometry(QtCore.QRect(170, 350, 121, 17))
        self.checkBox_reg29.setObjectName("checkBox_reg29")
        self.checkBox_reg30 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg30.setGeometry(QtCore.QRect(170, 370, 121, 17))
        self.checkBox_reg30.setObjectName("checkBox_reg30")
        self.checkBox_reg31 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg31.setGeometry(QtCore.QRect(170, 390, 121, 17))
        self.checkBox_reg31.setObjectName("checkBox_reg31")
        self.checkBox_reg32 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg32.setGeometry(QtCore.QRect(170, 410, 121, 17))
        self.checkBox_reg32.setObjectName("checkBox_reg32")
        self.checkBox_reg33 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg33.setGeometry(QtCore.QRect(170, 430, 121, 17))
        self.checkBox_reg33.setObjectName("checkBox_reg33")
        self.checkBox_reg34 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg34.setGeometry(QtCore.QRect(170, 450, 121, 17))
        self.checkBox_reg34.setObjectName("checkBox_reg34")
        self.checkBox_reg35 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg35.setGeometry(QtCore.QRect(330, 130, 121, 17))
        self.checkBox_reg35.setObjectName("checkBox_reg35")
        self.checkBox_reg36 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg36.setGeometry(QtCore.QRect(330, 150, 121, 17))
        self.checkBox_reg36.setObjectName("checkBox_reg36")
        self.checkBox_reg37 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg37.setGeometry(QtCore.QRect(330, 170, 121, 17))
        self.checkBox_reg37.setObjectName("checkBox_reg37")
        self.checkBox_reg38 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg38.setGeometry(QtCore.QRect(330, 190, 121, 17))
        self.checkBox_reg38.setObjectName("checkBox_reg38")
        self.checkBox_reg39 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg39.setGeometry(QtCore.QRect(330, 210, 130, 17))
        self.checkBox_reg39.setObjectName("checkBox_reg39")
        self.checkBox_reg40 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg40.setGeometry(QtCore.QRect(330, 230, 133, 17))
        self.checkBox_reg40.setObjectName("checkBox_reg40")
        self.checkBox_reg41 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg41.setGeometry(QtCore.QRect(330, 250, 121, 17))
        self.checkBox_reg41.setObjectName("checkBox_reg41")
        self.checkBox_reg42 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg42.setGeometry(QtCore.QRect(330, 270, 121, 17))
        self.checkBox_reg42.setObjectName("checkBox_reg42")
        self.checkBox_reg43 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg43.setGeometry(QtCore.QRect(330, 290, 121, 17))
        self.checkBox_reg43.setObjectName("checkBox_reg43")
        self.checkBox_reg44 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg44.setGeometry(QtCore.QRect(330, 310, 121, 17))
        self.checkBox_reg44.setObjectName("checkBox_reg44")
        self.checkBox_reg45 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg45.setGeometry(QtCore.QRect(330, 330, 121, 17))
        self.checkBox_reg45.setObjectName("checkBox_reg45")
        self.checkBox_reg46 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg46.setGeometry(QtCore.QRect(330, 350, 121, 17))
        self.checkBox_reg46.setObjectName("checkBox_reg46")
        self.checkBox_reg47 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg47.setGeometry(QtCore.QRect(330, 370, 121, 17))
        self.checkBox_reg47.setObjectName("checkBox_reg47")
        self.checkBox_reg48 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg48.setGeometry(QtCore.QRect(330, 390, 121, 17))
        self.checkBox_reg48.setObjectName("checkBox_reg48")
        self.checkBox_reg49 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg49.setGeometry(QtCore.QRect(330, 410, 121, 17))
        self.checkBox_reg49.setObjectName("checkBox_reg49")
        self.checkBox_reg50 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg50.setGeometry(QtCore.QRect(330, 430, 121, 17))
        self.checkBox_reg50.setObjectName("checkBox_reg50")
        self.checkBox_reg51 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg51.setGeometry(QtCore.QRect(330, 450, 121, 17))
        self.checkBox_reg51.setObjectName("checkBox_reg51")
        self.checkBox_reg52 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg52.setGeometry(QtCore.QRect(490, 130, 121, 17))
        self.checkBox_reg52.setObjectName("checkBox_reg52")
        self.checkBox_reg53 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg53.setGeometry(QtCore.QRect(490, 150, 121, 17))
        self.checkBox_reg53.setObjectName("checkBox_reg53")
        self.checkBox_reg54 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg54.setGeometry(QtCore.QRect(490, 170, 121, 17))
        self.checkBox_reg54.setObjectName("checkBox_reg54")
        self.checkBox_reg55 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg55.setGeometry(QtCore.QRect(490, 190, 121, 17))
        self.checkBox_reg55.setObjectName("checkBox_reg55")
        self.checkBox_reg56 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg56.setGeometry(QtCore.QRect(490, 210, 121, 17))
        self.checkBox_reg56.setObjectName("checkBox_reg56")
        self.checkBox_reg57 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg57.setGeometry(QtCore.QRect(490, 230, 121, 17))
        self.checkBox_reg57.setObjectName("checkBox_reg57")
        self.checkBox_reg58 = QtWidgets.QCheckBox(Form)
        self.checkBox_reg58.setGeometry(QtCore.QRect(490, 250, 121, 17))
        self.checkBox_reg58.setObjectName("checkBox_reg57")
        """Кнопка Выделить все регионы"""
        self.pushButton_reg = QtWidgets.QPushButton(Form)
        self.pushButton_reg.setGeometry(QtCore.QRect(490, 270, 151, 41))
        self.pushButton_reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_reg.setObjectName("pushButton_reg")
        """Копирайт"""
        self.label_company = QtWidgets.QLabel(Form)
        self.label_company.setGeometry(QtCore.QRect(240, 490, 121, 21))
        self.label_company.setObjectName("label_company")
        # self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        # self.lineEdit_2.setGeometry(QtCore.QRect(10, 130, 631, 321))
        # self.lineEdit_2.setAutoFillBackground(False)
        # self.lineEdit_2.setFrame(True)
        # self.lineEdit_2.setReadOnly(True)
        # self.lineEdit_2.setObjectName("lineEdit_2")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Парсер Goszakupki"))
        self.pushButton.setText(_translate("Form", "Запуск"))
        """кнопка запуск по регионам"""
        self.pushButton_reg2.setText(_translate("Form", "Запуск по регионам"))
        """Кнопка выделить все регионы"""
        self.pushButton_reg.setText(_translate("Form", "Выделить все регионы"))
        self.checkBox.setText(_translate("Form", "Подача заявок"))
        self.checkBox_2.setText(_translate("Form", "Работа комиссии"))
        self.checkBox_3.setText(_translate("Form", "Закупка завершена"))
        self.checkBox_4.setText(_translate("Form", "Закупка отменена"))
        """Регионы"""
        self.checkBox_reg1.setText(_translate("Form", "[01]Адыгея"))
        self.checkBox_reg2.setText(_translate("Form", "[02]Башкортостан"))
        self.checkBox_reg3.setText(_translate("Form", "[03]Бурятия"))
        self.checkBox_reg4.setText(_translate("Form", "[04,22]Алтай"))
        self.checkBox_reg5.setText(_translate("Form", "[07]КБР"))
        self.checkBox_reg6.setText(_translate("Form", "[08]Калмыкия"))
        self.checkBox_reg7.setText(_translate("Form", "[09]КЧР"))
        self.checkBox_reg8.setText(_translate("Form", "[10]Карелия"))
        self.checkBox_reg9.setText(_translate("Form", "[11]Коми"))
        self.checkBox_reg10.setText(_translate("Form", "[12]Марий Эл"))
        self.checkBox_reg11.setText(_translate("Form", "[13]Мордовия"))
        self.checkBox_reg12.setText(_translate("Form", "[15]СеверОсетия-Алания"))
        self.checkBox_reg13.setText(_translate("Form", "[16]Татарстан"))
        self.checkBox_reg14.setText(_translate("Form", "[17]Тыва"))
        self.checkBox_reg15.setText(_translate("Form", "[18]Удмуртия"))
        self.checkBox_reg16.setText(_translate("Form", "[19]Хакасия"))
        self.checkBox_reg17.setText(_translate("Form", "[21]Чувашия"))
        self.checkBox_reg18.setText(_translate("Form", "[23]Краснодар"))
        self.checkBox_reg19.setText(_translate("Form", "[26]Ставрополь"))
        self.checkBox_reg20.setText(_translate("Form", "[29]Архангельск"))
        self.checkBox_reg21.setText(_translate("Form", "[30]Астрахань"))
        self.checkBox_reg22.setText(_translate("Form", "[31]Белгород"))
        self.checkBox_reg23.setText(_translate("Form", "[32]Брянск"))
        self.checkBox_reg24.setText(_translate("Form", "[33]Владимир"))
        self.checkBox_reg25.setText(_translate("Form", "[34]Волгоград"))
        self.checkBox_reg26.setText(_translate("Form", "[35]Вологда"))
        self.checkBox_reg27.setText(_translate("Form", "[36]Воронеж"))
        self.checkBox_reg28.setText(_translate("Form", "[37]Иваново"))
        self.checkBox_reg29.setText(_translate("Form", "[40]Калуга"))
        self.checkBox_reg30.setText(_translate("Form", "[42]Кемерово"))
        self.checkBox_reg31.setText(_translate("Form", "[43]Киров"))
        self.checkBox_reg32.setText(_translate("Form", "[44]Кострома"))
        self.checkBox_reg33.setText(_translate("Form", "[45]Курган"))
        self.checkBox_reg34.setText(_translate("Form", "[46]Курск"))
        self.checkBox_reg35.setText(_translate("Form", "[47]ЛО"))
        self.checkBox_reg36.setText(_translate("Form", "[48]Липецк"))
        self.checkBox_reg37.setText(_translate("Form", "[77,50]Москва"))
        self.checkBox_reg38.setText(_translate("Form", "[51]Мурманск"))
        self.checkBox_reg39.setText(_translate("Form", "[52]Нижний Новгород"))
        self.checkBox_reg40.setText(_translate("Form", "[53]Великий Новгород"))
        self.checkBox_reg41.setText(_translate("Form", "[57]Орел"))
        self.checkBox_reg42.setText(_translate("Form", "[58]Пенза"))
        self.checkBox_reg43.setText(_translate("Form", "[59]Пермь"))
        self.checkBox_reg44.setText(_translate("Form", "[60]Псков"))
        self.checkBox_reg45.setText(_translate("Form", "[61]Ростов"))
        self.checkBox_reg46.setText(_translate("Form", "[62]Рязань"))
        self.checkBox_reg47.setText(_translate("Form", "[63]Самара"))
        self.checkBox_reg48.setText(_translate("Form", "[64]Саратов"))
        self.checkBox_reg49.setText(_translate("Form", "[67]Смоленск"))
        self.checkBox_reg50.setText(_translate("Form", "[68]Тамбов"))
        self.checkBox_reg51.setText(_translate("Form", "[69]Тверь"))
        self.checkBox_reg52.setText(_translate("Form", "[71]Тула"))
        self.checkBox_reg53.setText(_translate("Form", "[72]Тюмень"))
        self.checkBox_reg54.setText(_translate("Form", "[73]Ульяновск"))
        self.checkBox_reg55.setText(_translate("Form", "[74]Челябинск"))
        self.checkBox_reg56.setText(_translate("Form", "[76]Ярославль"))
        self.checkBox_reg57.setText(_translate("Form", "[78]СПБ"))
        self.checkBox_reg58.setText(_translate("Form", "[27]Красноярск"))

        self.label.setText(_translate("Form", "Поисковой запрос:"))
        self.label_2.setText(_translate("Form", "Дата начала и конца поиска:"))
        """Текст копирайта"""
        self.label_company.setText(_translate("Form", "© ГлавАвтоснаб 2021"))
        # self.lineEdit_2.setPlaceholderText(_translate("Form", "Здесь вывод из консоли"))

    def progresbar(self, last_page):
        bar1 = 0
        # for i in range(101):
        #     # slowing down the loop
        #     time.sleep(0.05)
        bar = 100 / last_page
            # setting value to progress bar
        self.progressBar.setValue(bar1)
        bar1 = bar1 + bar

