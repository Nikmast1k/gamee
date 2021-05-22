#guess the number
from PyQt5.QtCore import Qt
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton, QRadioButton, QGroupBox, QButtonGroup, QTextEdit, QLineEdit
from random import shuffle, randint

#окно
app = QApplication([])
pril = QWidget()
pril.resize(800, 600)
pril.setWindowTitle('GuessTheNumber')
line1 = QVBoxLayout()

#направляющие
hline1 = QHBoxLayout()
hline_2 = QHBoxLayout()
hline_3 = QHBoxLayout()
hline_4 = QHBoxLayout()
line1.addLayout(hline1)
line1.addLayout(hline_2)
line1.addLayout(hline_3)
line1.addLayout(hline_4)

#надписи
text_kompa = QLabel('Я загадал случайное число от 1 до 10. Попробуй угадать:')
text_kompa.setFont(QtGui.QFont("Arial", 24, QtGui.QFont.Bold))
hline1.addWidget(text_kompa, alignment = Qt.AlignCenter)
#кнопка проверки
proverka_kn = QPushButton('Проверить')
hline_2.addWidget(proverka_kn, alignment = Qt.AlignCenter)

cifra = randint(1, 10)

def proverka():
    chifra_pol = chislo_text.text()
    if chifra_pol != str(cifra):
        print('2')
    else:
        msg.show()

msg = QMessageBox()
msg.setWindowTitle("Повезет в другой раз!")
msg.setText("К сожалению, ты не угадал") 
msg.hide()

#ввод числа
chislo_text = QLineEdit()
hline_2.addWidget(chislo_text)





#нажатия
proverka_kn.clicked.connect(proverka)


pril.setLayout(line1)
pril.show()

app.exec_()