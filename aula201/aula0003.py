# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Button')
button.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Button 3')
button3.setStyleSheet('font-size: 40px;')

main_window = QWidget()

layout = QGridLayout()
main_window.setLayout(layout)

layout.addWidget(button, 1, 1)
layout.addWidget(button2, 1, 2)
layout.addWidget(button3, 3, 1, 1, 2)

main_window.show()
app.exec()
