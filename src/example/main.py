import sys
from PySide6 import QtUiTools
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLCDNumber

from example.components.lexica import MyLexer
from example.components.parsers import MyParser
from example.components.memory import Memory
from example.components.ui import Ui_MainWindow

class MainWindow(QMainWindow):

    # Do this for intellisense
    button_1:QPushButton
    button_2:QPushButton
    button_plus:QPushButton
    button_equal:QPushButton
    input_text:QLineEdit
    output_lcd:QLCDNumber

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #### Binding button to function ####
        # Method 1:
        self.ui.button_1.clicked.connect(self.push_1)
        # Method 2:
        self.ui.button_2.clicked.connect(lambda: self.push("2"))
        self.ui.button_plus.clicked.connect(lambda: self.push("+"))

        self.ui.button_equal.clicked.connect(self.push_equal)

    def push_1(self):
        current_text:str = self.ui.input_text.text()
        self.ui.input_text.setText(f"{current_text}1")
    
    def push(self, text:str):
        current_text:str = self.ui.input_text.text()
        self.ui.input_text.setText(f"{current_text}{text}")
    
    def push_equal(self):
        print("Calculate")
        lexer = MyLexer()
        parser = MyParser()
        memory = Memory()
        input_text = self.ui.input_text.text()
        result = parser.parse(lexer.tokenize(input_text))
        print(type(result))
        self.ui.output_lcd.display(result)
        # for debug
        print(memory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())