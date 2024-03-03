import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from diagnos_management import diagn_manager
from personal_management import personal_management_Window


class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.diagnos_manager = None
        self.setWindowTitle('Админская страница')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()

    def setupWidgets(self):
        accept_button1 = QPushButton('Управление диагнозов', self)
        accept_button1.move(160, 100)
        accept_button1.setFixedWidth(200)
        accept_button1.clicked.connect(self.manage_diagnos)

        accept_button2 = QPushButton('Управление персоналом', self)
        accept_button2.move(160, 130)
        accept_button2.setFixedWidth(200)
        accept_button2.clicked.connect(self.personal_manager)

        accept_button = QPushButton('Список диагнозов', self)
        accept_button.move(160, 160)
        accept_button.setFixedWidth(200)

        accept_button = QPushButton('Список персонала', self)
        accept_button.move(160, 190)
        accept_button.setFixedWidth(200)

    def manage_diagnos(self):
        self.diagnos_manager = diagn_manager()
        self.diagnos_manager.show()
        self.hide()

    def personal_manager(self):
        self.personal_manager = personal_management_Window()
        self.personal_manager.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())
