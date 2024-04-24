import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QErrorMessage, QDialog
from PyQt5.QtCore import Qt
from main_admin import AdminWindow


class LoginAdmin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вход для администратора')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()
        self.setWindowModality(Qt.WindowModal)

    def setupWidgets(self):
        login_label = QLabel('Логин', self)
        login_label.move(30, 25)

        self.login_input = QLineEdit(self)
        self.login_input.move(150, 20)

        password_label = QLabel('Пароль', self)
        password_label.move(30, 50)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.move(150, 45)

        accept_button = QPushButton('Войти', self)
        accept_button.move(160, 100)
        accept_button.setFixedWidth(100)
        accept_button.clicked.connect(self.login)

    def openAdminWindow(self):
        self.adminWindow = AdminWindow()
        self.adminWindow.exec_()
        #self.hide()

    def login(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if login == 'admin' and password == 'Password':
            messageBox = QMessageBox()
            messageBox.setWindowTitle('Успешный вход')
            messageBox.setText('Вы успешно вошли')
            messageBox.exec_()
            self.openAdminWindow()
        else:
            messageBox = QMessageBox()
            messageBox.setWindowTitle('Ошибка входа')
            messageBox.setText("Неправильный лоигин или пароль")
            messageBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginAdmin()
    window.show()
    sys.exit(app.exec_())