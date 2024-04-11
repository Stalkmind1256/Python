import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem,
                             QMessageBox)

from database_connection import connect_db


class personal_management_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.middlename = None
        self.lastname = None
        self.firstname = None
        self.table = None
        self.phone = None
        self.password = None
        self.number_cab = None
        self.specialization = None
        self.setWindowTitle('Список персонала')
        self.setGeometry(450, 750, 800, 750)
        self.setupWidgets()
        self.display()

    def setupWidgets(self):
        lastname = QLabel('Фамилия', self)
        lastname.move(25, 25)
        self.lastname = QLineEdit(self)
        self.lastname.move(130, 20)

        firstname = QLabel('Имя', self)
        firstname.move(25, 50)
        self.firstname = QLineEdit(self)
        self.firstname.move(130, 45)

        middlename = QLabel('Отчество', self)
        middlename.move(25, 75)
        self.middlename = QLineEdit(self)
        self.middlename.move(130, 70)

        specialization = QLabel('Специализация', self)
        specialization.move(25, 100)
        self.specialization = QLineEdit(self)
        self.specialization.move(130, 95)

        phone = QLabel('Телефон', self)
        phone.move(25, 125)
        self.phone = QLineEdit(self)
        self.phone.move(130, 120)

        number_cab = QLabel('Номер кабинета', self)
        number_cab.move(25, 150)
        self.number_cab = QLineEdit(self)
        self.number_cab.move(130, 145)

        password = QLabel('Пароль', self)
        password.move(25, 175)
        self.password = QLineEdit(self)
        self.password.move(130, 170)

        accept_button = QPushButton('Добавить врача', self)
        accept_button.move(270, 20)
        accept_button.setFixedWidth(150)
        accept_button.clicked.connect(self.add_data)
        
        #exit_button = QPushButton('Главная',self)
        #exit_button.move(270, 45)
        #exit_button.setFixedWidth(150)
        #exit_button.clicked.connect(self.goto_main)

        self.table = QTableWidget(self)
        self.table.setGeometry(25, 200, 750, 550)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(['Фамилия', 'Имя', 'Отчество', 'Специализация', 'Телефон', 'Номер кабинета', 'Пароль', 'Удалить'])

    def add_data(self):
        db_connect = connect_db()
        cursor = db_connect.cursor()
        lastname_text = self.lastname.text()
        firstname_text = self.firstname.text()
        middlename_text = self.middlename.text()
        specialization_text = self.specialization.text()
        phone_text = self.phone.text()
        number_cab_text = self.number_cab.text()
        password_text = self.password.text()

        query = ("INSERT INTO doctors (lastname, firstname, middlename, specializations, phone, number_of_cabinet, "
                 "password) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data = (lastname_text, firstname_text, middlename_text, specialization_text, phone_text, number_cab_text, password_text)
        cursor.execute(query, data)

        db_connect.commit()
        cursor.close()
        db_connect.close()
        self.display()

    def display(self):
        db_connect = connect_db()
        if db_connect:
            cursor = db_connect.cursor()
            cursor.execute("SELECT lastname, firstname, middlename, specializations, phone, number_of_cabinet, "
                           "password FROM doctors")
            data = cursor.fetchall()

            self.table.setRowCount(len(data))
            for row, row_data in enumerate(data):
                for column, column_data in enumerate(row_data):
                    item = QTableWidgetItem(str(column_data))
                    self.table.setItem(row, column, item)
                delete_btn = QPushButton("Удалить")
                delete_btn.clicked.connect(self.delete_data)
                self.table.setCellWidget(row, 7, delete_btn)

            cursor.close()
            db_connect.close()

    def delete_data(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            db_connect = connect_db()
            if db_connect:
                cursor = db_connect.cursor()
                name = self.table.item(row, 0).text()
                query = "DELETE FROM doctors WHERE lastname = %s"
                cursor.execute(query, (name,))
                db_connect.commit()
                cursor.close()
                db_connect.close()

                self.display()
                QMessageBox.warning(self, 'Успех', 'Данные удалены')
	
	

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = personal_management_Window()
    window.show()
    sys.exit(app.exec_())
