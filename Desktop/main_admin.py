import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from diagnos_management import diagn_manager


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

        accept_button = QPushButton('Управление персоналом', self)
        accept_button.move(160, 130)
        accept_button.setFixedWidth(200)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())