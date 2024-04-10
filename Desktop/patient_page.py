import sys

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
                             QTableWidgetItem, QComboBox, QTimeEdit, QDateEdit,
                             QMessageBox)

from database_connection import connect_db


class PatientPage(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.data = None
        self.time = None
        self.doctor = None
        self.patient = None
        self.setWindowTitle('Записаться на прием')
        self.setGeometry(450, 450, 450, 450)
        self.setupWidgets()
        self.fillCombobox()

    def setupWidgets(self):
        patient = QLabel('Пациент:', self)
        patient.move(27, 50)
        self.patient = QComboBox(self)
        self.patient.move(90, 45)

        doctor = QLabel('Врач:', self)
        doctor.move(27, 75)
        self.doctor = QComboBox(self)
        self.doctor.move(90, 70)

        time = QLabel('Время:', self)
        time.move(27, 100)
        self.time = QTimeEdit(self)
        self.time.move(90, 95)

        data = QLabel('Дата:', self)
        data.move(27, 125)
        self.data = QDateEdit(self)
        self.data.move(90, 120)

        # self.patient_model = {}

        button_accept = QPushButton('Записаться на прием', self)
        button_accept.move(27, 150)
        button_accept.setFixedWidth(150)
        button_accept.clicked.connect(self.add_data)

    def fillCombobox(self):
        db_connect = connect_db()
        cursor = db_connect.cursor()
        patient_query = "SELECT * FROM patients"
        doctor_query = "SELECT * FROM doctors"

        cursor.execute(patient_query)
        patients = cursor.fetchall()
        for patient in patients:
            patient_name = f"{patient[1]} {patient[2]} {patient[3]}"
            patient_id = patient[0]
            self.patient.addItem(patient_name, userData=patient_id)

        cursor.execute(doctor_query)
        cursor.execute(doctor_query)
        doctors = cursor.fetchall()
        for doctor in doctors:
            doctor_name = f"{doctor[1]} {doctor[2]} {doctor[3]}"
            doctor_id = doctor[0]
            self.doctor.addItem(doctor_name, userData=doctor_id)

        cursor.close()
        db_connect.close()

    def add_data(self):
        db_connect = connect_db()
        cursor = db_connect.cursor()
        patient_id = self.patient.currentData()
        doctor_id = self.doctor.currentData()
        data_text = self.data.text()
        time_text = self.time.text()

        query = ("INSERT INTO appointment(id_patients, id_doctors, date, time)  VALUES (%s, %s, %s, %s)")
        data = (patient_id, doctor_id, data_text, time_text)
        cursor.execute(query, data)

        db_connect.commit()
        cursor.close()
        db_connect.close()

        QMessageBox.information(self, "Успех", "Вы успешно записались на прием!")
        self.close()

        # Локальный импорт интерфеса, musthave, чтобы   бороться с циклическим импортом
        from main import MainWindow
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PatientPage()
    window.show()
    sys.exit(app.exec_())
