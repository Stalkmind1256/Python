import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem,
                             QMessageBox, QMainWindow)

from database_connection import connect_db


class DoctorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Страница врача')
        self.setGeometry(450, 450, 450, 450)

        self.table = QTableWidget(self)
        self.table.setGeometry(25, 200, 750, 550)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'ID Доктора', 'ID Пациента', 'Дата', 'Время', 'ID Диагноза', 'ID Добавить диагноз'])
        self.display()

    def display(self):
        db_connect = connect_db()
        cursor = db_connect.cursor()
        cursor.execute("SELECT id, id_patients, id_doctors, date, time, id_diagnos FROM appointment")
        data = cursor.fetchall()
        self.table.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for column, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.table.setItem(row, column, item)
        cursor.close()
        db_connect.close()

        self.table.resizeColumnsToContents() #настройка ширины столбцев


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DoctorWindow()
    window.show()
    sys.exit(app.exec_())
