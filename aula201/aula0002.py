# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

button = QPushButton('Button')
button.setStyleSheet('font-size: 80px;')
button.show()

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')
button.show()

app.exec()
