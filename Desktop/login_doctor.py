import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDialog
from database_connection import connect_db
from PyQt5.QtCore import Qt



class LoginDoctor(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вход')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()

    def setupWidgets(self):
        phone_label = QLabel('Телефон', self)
        phone_label.move(30, 25)

        self.phone_input = QLineEdit(self)
        self.phone_input.move(150, 20)

        password_label = QLabel('Пароль', self)
        password_label.move(30, 50)

        self.password_input = QLineEdit(self)
        self.password_input.move(150, 45)

        accept_button = QPushButton('Войти', self)
        accept_button.move(160, 100)
        accept_button.setFixedWidth(100)
        accept_button.clicked.connect(self.login)


    def login(self):
        phone = self.phone_input.text()
        password = self.password_input.text()

        db_connect = connect_db()
        cursor = db_connect.cursor()

        query = "SELECT phone, password FROM doctors WHERE phone = %s and password = %s"
        cursor.execute(query, (phone, password))

        result = cursor.fetchone()
        if result is not None and result[1] == password:
            self.openDoctorPage()
        else:
            QMessageBox.information(self, "", 'Ошибка входа, проверьте правильность телефона или пароля')

        cursor.close()
        db_connect.close()

    def openDoctorPage(self):
        from doctor_page import DoctorWindow
        #self.hide()
        self.doctorWindow = DoctorWindow()
        self.doctorWindow.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginDoctor()
    window.show()
    sys.exit(app.exec_())