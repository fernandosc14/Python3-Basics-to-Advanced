# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

app = QApplication(sys.argv)

button1 = QPushButton('Button')
button1.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Button 2')
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Button 3')
button3.setStyleSheet('font-size: 40px;')

main_window = QWidget()

layout = QGridLayout()
main_window.setLayout(layout)

layout.addWidget(button1, 1, 1)
layout.addWidget(button2, 1, 2)
layout.addWidget(button3, 3, 1, 1, 2)

main_window.show()
app.exec()
