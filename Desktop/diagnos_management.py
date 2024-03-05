import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QTableWidget, QTableWidgetItem,
                             QMessageBox)

from database_connection import connect_db


class diagn_manager(QWidget):
    def __init__(self):
        super().__init__()
        self.table = None
        self.diagnos_input = None
        self.diagnos_description_input = None
        self.setWindowTitle('Список диагнозов')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()
        self.display()

    def setupWidgets(self):
        diagnos = QLabel('Название диагноза', self)
        diagnos.move(25, 25)

        self.diagnos_input = QLineEdit(self)
        self.diagnos_input.move(150, 20)

        diagnos_description = QLabel('Описание диагноза', self)
        diagnos_description.move(25, 50)

        self.diagnos_description_input = QLineEdit(self)
        self.diagnos_description_input.move(150, 45)

        accept_button = QPushButton('Добавить диагноз', self)
        accept_button.move(280, 20)
        accept_button.setFixedWidth(150)
        accept_button.clicked.connect(self.add_data)


        self.table = QTableWidget(self)
        self.table.setGeometry(25, 90, 400, 280)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Название', 'Описание', 'Удалить'])



    def add_data(self):
        db_connect = connect_db()

        if db_connect:
            cursor = db_connect.cursor()
            diagnos_input_text = self.diagnos_input.text()
            diagnos_description_input_text = self.diagnos_description_input.text()

            query = "INSERT INTO diagnosis (name, discription) VALUES (%s, %s)"

            data = (diagnos_input_text, diagnos_description_input_text)
            cursor.execute(query, data)

            db_connect.commit()
            cursor.close()
            db_connect.close()
            self.display()

    def display(self):
        db_connect = connect_db()
        if db_connect:
            cursor = db_connect.cursor()
            cursor.execute("SELECT name, discription FROM diagnosis")
            data = cursor.fetchall()

            self.table.setRowCount(len(data))
            for row, row_data in enumerate(data):
                for column, column_data in enumerate(row_data):
                    item = QTableWidgetItem(str(column_data))
                    self.table.setItem(row, column, item)
                delete_btn = QPushButton("Удалить")
                delete_btn.clicked.connect(self.delete_data)
                self.table.setCellWidget(row, 2, delete_btn)
            cursor.close()
            db_connect.close()

    def delete_data(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            db_connect = connect_db()
            if db_connect:
                cursor = db_connect.cursor()
                name = self.table.item(row,0).text()
                query = "DELETE FROM diagnosis WHERE name = %s"
                cursor.execute(query, (name,))
                db_connect.commit()
                cursor.close()
                db_connect.close()

                self.display()
                QMessageBox.warning(self, 'Успех', 'Данные удалены')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = diagn_manager()
    window.show()
    sys.exit(app.exec_())
