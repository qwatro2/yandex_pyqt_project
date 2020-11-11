from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from MyWidgets.MyMenuWindow import MyMenuWindow
from MyWidgets.MyViewWindow import MyViewWindow
from MyWidgets.MyAddReceptWindow import MyAddReceptWindow
import constants
import sqlite3


class MyMainWindow(QMainWindow):
    """
    Класс главного окна программы.
    Задает иконку, размер окна, название окна.
    Создает связь с базой данных.
    Создает виджеты различных окон приложения.
    """

    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(constants.ICON_PATH))

        self.setWindowTitle(constants.MAIN_WINDOW_TITLE)

        self.setGeometry(50, 50, *constants.SCREEN_SIZE)
        self.setFixedSize(*constants.SCREEN_SIZE)

        self.database_connection = sqlite3.connect(constants.DATABASE_PATH)

        self.menu_window = MyMenuWindow(self)
        self.menu_window.show()

        self.browse_by_title_window = MyViewWindow(self, 'title')
        self.browse_by_title_window.hide()

        self.browse_by_ingredients_window = MyViewWindow(self, 'ingredients')
        self.browse_by_ingredients_window.hide()

        self.browse_by_complexity_window = MyViewWindow(self, 'complexity')
        self.browse_by_complexity_window.hide()

        self.add_recept_window = MyAddReceptWindow(self)
        self.add_recept_window.hide()
