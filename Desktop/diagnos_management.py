import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QPlainTextEdit
from database_connection import connect_db



class diagn_manager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список диагнозов')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()

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
        accept_button.move(280, 30)
        accept_button.setFixedWidth(150)
        accept_button.clicked.connect(self.add_data)

    def add_data(self):
        db_connection = connect_db()

        if db_connection:
            cursor = db_connection.cursor()
            diagnos_input_text = self.diagnos_input.text()
            diagnos_description_input_text = self.diagnos_description_input.text()

            query = "INSERT INTO diagnosis (name, discription) VALUES (%s, %s)"

            data = (diagnos_input_text, diagnos_description_input_text)
            cursor.execute(query, data)

            db_connection.commit()
            cursor.close()
            db_connection.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = diagn_manager()
    window.show()
    sys.exit(app.exec_())
