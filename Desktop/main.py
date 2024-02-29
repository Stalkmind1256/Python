import sys

from PyQt5.QtGui import QIcon, QColor, QFont, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

from login import LoginWindow
from login_doctor import LoginDoctor
from login_admin import LoginAdmin


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.loginDoctor = None
        self.loginWindow = None
        self.loginAdmin = None
        self.setWindowTitle('Поликилнника')
        self.setGeometry(450, 400, 450, 400)
        self.setupWidgets()
        self.show()


    def setupWidgets(self):
        main_text = QLabel(self)
        main_text.setText('Поликлинника')
        main_text.move(160, 10)
        main_text.setFixedWidth(100)
        main_text.setFixedWidth(300)

        btn1 = QPushButton('Регистрация', self)
        btn1.move(160, 70)
        btn1.setFixedWidth(200)

        btn2 = QPushButton('Вход', self)
        btn2.move(160, 95)
        btn2.setFixedWidth(200)
        btn2.clicked.connect(self.openLoginWindow)

        btn3 = QPushButton('Вход для администратора', self)
        btn3.move(160, 120)
        btn3.setFixedWidth(200)
        btn3.clicked.connect(self.openLoginWindow3)

        btn4 = QPushButton('Вход для врача', self)
        btn4.move(160, 145)
        btn4.setFixedWidth(200)
        btn4.clicked.connect(self.openLoginWindow2)

    def openLoginWindow(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.show()
        self.hide()

    def openLoginWindow2(self):
        self.loginDoctor = LoginDoctor()
        self.loginDoctor.show()
        self.hide()

    def openLoginWindow3(self):
        self.loginAdmin = LoginAdmin()
        self.loginAdmin.show()
        self.hide()





    """
        font = QFont("Arial", 12, QFont.Bold)
        main_text.setFont(font)

        изменение размера текста
        font.setPointSize(12)
        main_text.setFont(font)

        изменение цвета текста
        pallet = QPalette()
        color = QColor(255, 0, 0)
        pallet.setColor(QPalette.Foreground, color)
        main_text.setPalette(pallet)
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
