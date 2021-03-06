from MyWidgets.MyMainWindow import MyMainWindow
from PyQt5.QtWidgets import QApplication
import sys


def main():
    """
    Главная функция программы.
    Создает окно приложения и главный виджет.
    """
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
