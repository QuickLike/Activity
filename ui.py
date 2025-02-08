import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from config import WINDOW_NAME, SCREEN_WIDTH, SCREEN_HEIGHT


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(WINDOW_NAME)
        self.setGeometry(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 5, 1440, 900)
        self.setWindowIcon(QIcon('img/favicon.jpg'))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
