import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(100, 100, 300, 400)
        self.setFixedSize(300, 400)
        self.setWindowTitle("Calculator")

        # Display
        self.display = QLineEdit(self)
        self.display.setGeometry(20, 20, 260, 40)

        # Buttons layout
        buttons = [
            ('7', 20, 80), ('8', 90, 80), ('9', 160, 80), ('/', 230, 80),
            ('4', 20, 140), ('5', 90, 140), ('6', 160, 140), ('*', 230, 140),
            ('1', 20, 200), ('2', 90, 200), ('3', 160, 200), ('-', 230, 200),
            ('0', 20, 260), ('C', 90, 260), ('=', 160, 260), ('+', 230, 260),
        ]

        for text, x, y in buttons:
            btn = QPushButton(text, self)
            btn.setGeometry(x, y, 60, 50)
            btn.clicked.connect(self.on_click)

    def on_click(self):
        sender = self.sender()
        text = sender.text()

        if text == "C":
            self.display.clear()

        elif text == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except:
                self.display.setText("Error")

        else:
            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())
