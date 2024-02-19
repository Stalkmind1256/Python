import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вход')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()

    def setupWidgets(self):
        email_label = QLabel('Email', self)
        email_label.move(30, 25)

        email_input = QLineEdit(self)
        email_input.move(150, 20)

        password_label = QLabel('Пароль', self)
        password_label.move(30, 50)

        password_input = QLineEdit(self)
        password_input.move(150, 45)

        accept_button = QPushButton('Войти', self)
        accept_button.move(160, 100)
        accept_button.setFixedWidth(100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
