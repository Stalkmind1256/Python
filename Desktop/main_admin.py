import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Админская страница')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()

    def setupWidgets(self):
        accept_button = QPushButton('Управление диагнозов', self)
        accept_button.move(160, 100)
        accept_button.setFixedWidth(200)

        accept_button = QPushButton('Управление персоналом', self)
        accept_button.move(160, 130)
        accept_button.setFixedWidth(200)

        accept_button = QPushButton('Список диагнозов', self)
        accept_button.move(160, 160)
        accept_button.setFixedWidth(200)

        accept_button = QPushButton('Список персонала', self)
        accept_button.move(160, 190)
        accept_button.setFixedWidth(200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())