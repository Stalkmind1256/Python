import sys
import datetime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QDateEdit, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QDialog,
                             QMessageBox)
from PyQt5.QtCore import Qt
from database_connection import connect_db


class RegistrationWindow(QDialog):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.password = None
        self.email = None
        self.password_again = None
        self.phone = None
        self.passport = None
        self.birthdate = None
        self.middlename = None
        self.firstname = None
        self.lastname = None
        self.setWindowTitle('Регистрация')
        self.setGeometry(450, 750, 800, 750)
        self.setupWidgets()

    def setupWidgets(self):
        label = QLabel('Личные данные', self)
        label.move(100, 150)

        lastname = QLabel('Фамилия', self)
        lastname.move(100, 200)
        self.lastname = QLineEdit(self)
        self.lastname.move(170, 195)

        firstname = QLabel('Имя', self)
        firstname.move(100, 235)
        self.firstname = QLineEdit(self)
        self.firstname.move(170, 230)

        middlename = QLabel('Отчество', self)
        middlename.move(100, 270)
        self.middlename = QLineEdit(self)
        self.middlename.move(170, 265)

        birthdate = QLabel('Дата рождения', self)
        birthdate.move(100, 305)
        self.birthdate = QDateEdit(self)
        self.birthdate.move(205, 301)

        passport = QLabel('Паспорт', self)
        passport.move(100, 340)
        self.passport = QLineEdit(self)
        self.passport.move(170, 335)

        phone = QLabel('Телефон', self)
        phone.move(100, 375)
        self.phone = QLineEdit(self)
        self.phone.move(170, 370)

        label1 = QLabel('Данные для идентификации', self)
        label1.move(340, 150)

        email = QLabel('Электронная почта', self)
        email.move(340, 200)
        self.email = QLineEdit(self)
        self.email.move(470, 195)

        password = QLabel('Пароль', self)
        password.move(340, 235)
        self.password = QLineEdit(self)
        self.password.move(470, 230)

        password_again = QLabel('Повторите пароль', self)
        password_again.move(340, 270)
        self.password_again = QLineEdit(self)
        self.password_again.move(470, 265)

        accept_button = QPushButton('Зарегистрироваться', self)
        accept_button.move(370, 340)
        accept_button.setFixedWidth(200)
        accept_button.clicked.connect(self.register)

        #exit_main = QPushButton('Главная', self)
        #exit_main.move(370, 370)
        #exit_main.setFixedWidth(200)
        #exit_main.clicked.connect(self.open_main)

    #def open_main(self):
        #self.mainWindow.show()
       #self.hide()

    def register(self):
        if not self.check_fields():
            QMessageBox.warning(self, 'Ошибка', "Все поля должны быть заполнены")
            return
        if self.check_password():
            self.add_data()

    def add_data(self):
        db_connect = connect_db()
        cursor = db_connect.cursor()
        lastname_text = self.lastname.text()
        firstname_text = self.firstname.text()
        middlename_text = self.middlename.text()
        birthdate_text = self.birthdate.date().toString('yyyy-MM-dd')
        passport_text = self.passport.text()
        phone_text = self.phone.text()
        email_text = self.email.text()
        password_text = self.password.text()
        # password_again_text = self.password_again.text()

        query = ("INSERT INTO patients (lastname, firstname, middlename, birthdate, passport, phone, email, "
                 "password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

        data = (lastname_text, firstname_text, middlename_text, birthdate_text, passport_text, phone_text,
                email_text, password_text)
        cursor.execute(query, data)

        db_connect.commit()
        cursor.close()
        db_connect.close()

        QMessageBox.information(self, "Успех", "Вы успешно зарегистрировались")
        self.close()

        from main import MainWindow
        self.mainWin = MainWindow()
        self.mainWin.show()

    def check_fields(self):
        if (self.lastname.text() and self.firstname.text() and self.middlename.text()
                and self.passport.text() and self.phone.text() and self.email.text() and
                self.password.text() and self.password_again.text()):
            return True
        else:
            return False

    def check_password(self):
        password = self.password.text()
        password_again = self.password_again.text()
        if password != password_again:
            QMessageBox.warning(self, 'Пароли не совпадают', 'Введенные пароли не совпадают')
            return False
        else:
            return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationWindow()
    window.show()
    sys.exit(app.exec_())
