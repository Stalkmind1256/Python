import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QComboBox,
                             QMessageBox, QMainWindow)

from database_connection import connect_db


class DoctorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Страница врача')
        self.setGeometry(450, 450, 750, 450)

        self.table = QTableWidget(self)
        self.table.setGeometry(10, 10, 725, 470)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'ID Доктора', 'ID Пациента', 'Дата', 'Время', 'ID Диагноза', 'Выбрать диагноз',
             'ID Добавить Диагноз'])
        self.display()

    def display(self):
        db_connect = connect_db()
        cursor = db_connect.cursor()
        cursor.execute("SELECT id, id_doctors, id_patients, date, time, id_diagnos FROM appointment")
        data = cursor.fetchall()
        self.table.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for column, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.table.setItem(row, column, item)
            diagnosis = self.get_diagnos()
            combobox = QComboBox()
            combobox.addItems(diagnosis)
            self.table.setCellWidget(row, 6, combobox)
            add_btn = QPushButton("Добавить")
            add_btn.clicked.connect(self.add_data)
            self.table.setCellWidget(row, 7, add_btn)

        cursor.close()
        db_connect.close()

        self.table.resizeColumnsToContents()  # настройка ширины столбцев

    def get_diagnos(self):
        db_connect = connect_db()
        cursor = db_connect.cursor()
        cursor.execute("SELECT name FROM diagnosis")
        data = cursor.fetchall()
        cursor.close()
        db_connect.close()
        return [row[0] for row in data]

    def add_data(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            db_connect = connect_db()
            if db_connect:
                cursor = db_connect.cursor()
                combobox = self.table.cellWidget(row, 6)
                selected_diagnosis = combobox.currentText()

                # Получаем ID выбранного диагноза
                cursor.execute("SELECT id FROM diagnosis WHERE name = %s", (selected_diagnosis,))
                result = cursor.fetchone()
                if result:
                    diagnosis_id = result[0]
                    cursor.execute("UPDATE appointment SET id_diagnos = %s WHERE id = %s",
                                   (diagnosis_id, self.table.item(row, 0).text()))
                    db_connect.commit()
                    cursor.close()
                    db_connect.close()

                    item = QTableWidgetItem(str(diagnosis_id))
                    self.table.setItem(row, 5, item)

                    QMessageBox.information(self, 'Успешно', 'ID выбранного диагноза был добавлен в базу данных.')
                else:
                    QMessageBox.warning(self, 'Ошибка', 'Выбранный диагноз не найден в базе данных.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DoctorWindow()
    window.show()
    sys.exit(app.exec_())
