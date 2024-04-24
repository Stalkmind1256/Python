import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QDialog
from diagnos_management import diagn_manager
from personal_management import personal_management_Window


class AdminWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.diagnos_manager = None
        self.setWindowTitle('Админская страница')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()

    def setupWidgets(self):
        accept_button1 = QPushButton('Управление диагнозов', self)
        accept_button1.move(140, 100)
        accept_button1.setFixedWidth(200)
        accept_button1.clicked.connect(self.manage_diagnos)

        accept_button2 = QPushButton('Управление персоналом', self)
        accept_button2.move(140, 130)
        accept_button2.setFixedWidth(200)
        accept_button2.clicked.connect(self.personal_manager)

        accept_button = QPushButton('Список диагнозов', self)
        accept_button.move(140, 160)
        accept_button.setFixedWidth(200)

        accept_button = QPushButton('Список персонала', self)
        accept_button.move(140, 190)
        accept_button.setFixedWidth(200)

        #exit_button = QPushButton('Выход', self)
        #exit_button.move(160, 220)
        #exit_button.setFixedWidth(200)
        #exit_button.clicked.connect(self.goto_main)

    #def goto_main(self):
        #from main import MainWindow
       #self.hide()
        #self.main = MainWindow()
        #self.main.show()


    def manage_diagnos(self):
        self.diagnos_manager = diagn_manager()
        self.diagnos_manager.exec_()
        #self.hide()

    def personal_manager(self):
        self.personal_manager = personal_management_Window()
        self.personal_manager.exec_()
        #self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())