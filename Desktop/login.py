import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from database_connection import connect_db
from patient_page import PatientPage


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.patient_page = None
        self.setWindowTitle('Вход')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()

    def setupWidgets(self):
        email_label = QLabel('Email', self)
        email_label.move(30, 25)
        self.email_input = QLineEdit(self)
        self.email_input.move(150, 20)

        password_label = QLabel('Пароль', self)
        password_label.move(30, 50)
        self.password_input = QLineEdit(self)
        self.password_input.move(150, 45)

        accept_button = QPushButton('Войти', self)
        accept_button.move(160, 100)
        accept_button.setFixedWidth(100)
        accept_button.clicked.connect(self.login)

    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()

        db_connect = connect_db()
        cursor = db_connect.cursor()

        query = "SELECT email, password FROM patients WHERE email = %s"
        cursor.execute(query, (email,))

        result = cursor.fetchone()
        if result is not None and result[1] == password:
            self.openPatientPage()
        else:
            QMessageBox.information(self, "", 'Ошибка входа, проверьте правильность логина или пароля')

        cursor.close()
        db_connect.close()

    def openPatientPage(self):
        self.patient_page = PatientPage()
        self.patient_page.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
