import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLCDNumber

from components.lexica import MyLexer
from components.parsers import MyParser
from components.memory import Memory

class MainWindow(QMainWindow):

    # Do this for intellisense
    button_1:QPushButton
    button_2:QPushButton
    button_plus:QPushButton
    button_equal:QPushButton
    input_text:QLineEdit
    output_lcd:QLCDNumber

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("components/main.ui", self)

        #### Binding button to function ####
        # Method 1:
        self.button_1.clicked.connect(self.push_1)
        # Method 2:
        self.button_2.clicked.connect(lambda: self.push("2"))
        self.button_plus.clicked.connect(lambda: self.push("+"))

        self.button_equal.clicked.connect(self.push_equal)

    def push_1(self):
        current_text:str = self.input_text.text()
        self.input_text.setText(f"{current_text}1")
    
    def push(self, text:str):
        current_text:str = self.input_text.text()
        self.input_text.setText(f"{current_text}{text}")
    
    def push_equal(self):
        print("Calculate")
        lexer = MyLexer()
        parser = MyParser()
        memory = Memory()
        input_text = self.input_text.text()
        result = parser.parse(lexer.tokenize(input_text))
        print(type(result))
        self.output_lcd.display(result)
        # for debug
        print(memory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()