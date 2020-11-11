from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.Qt import QPixmap
from MyWidgets.MyExitMessageBox import MyExitMessageBox
from MyWidgets.MyInformationWindow import MyInformationWindow
import sys
import constants


class MyMenuWindow(QWidget):
    """
    Класс окна меню приложения.
    Имеет кнопки навигации по окнам приложения и соответсвующие методы.
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, *constants.SCREEN_SIZE)
        self.setFixedSize(*constants.SCREEN_SIZE)

        self.initUI()

    def initUI(self):
        """
        Метод инициализации UI.
        Создает на виджете фоновую картинку и кнопки, их соединение с методами.
        """

        background_label = QLabel(self)
        background_label.setPixmap(QPixmap(constants.MAIN_WINDOW_BACKGROUND_IMAGE))
        background_label.resize(*constants.SCREEN_SIZE)

        browse_by_title_button = QPushButton('Поиск рецептов по названию', self)
        browse_by_title_button.resize(int(self.width() * 0.6), int(self.height() * 0.12))
        browse_by_title_button.move(int(self.width() * 0.2), int(self.height() * 0.04))
        browse_by_title_button.clicked.connect(self.open_view_window)

        browse_by_ingredients_button = QPushButton('Поиск рецептов по ингредиентам', self)
        browse_by_ingredients_button.resize(int(self.width() * 0.6), int(self.height() * 0.12))
        browse_by_ingredients_button.move(int(self.width() * 0.2), int(self.height() * 0.2))
        browse_by_ingredients_button.clicked.connect(self.open_view_window)

        browse_by_complexity_button = QPushButton('Поиск рецептов по сложности', self)
        browse_by_complexity_button.resize(int(self.width() * 0.6), int(self.height() * 0.12))
        browse_by_complexity_button.move(int(self.width() * 0.2), int(self.height() * 0.36))
        browse_by_complexity_button.clicked.connect(self.open_view_window)

        add_button = QPushButton('Добавить рецепт', self)
        add_button.resize(int(self.width() * 0.6), int(self.height() * 0.12))
        add_button.move(int(self.width() * 0.2), int(self.height() * 0.52))
        add_button.clicked.connect(self.open_add_window)

        info_button = QPushButton('Инструкция', self)
        info_button.resize(int(self.width() * 0.6), int(self.height() * 0.12))
        info_button.move(int(self.width() * 0.2), int(self.height() * 0.68))
        info_button.clicked.connect(self.show_information)

        exit_button = QPushButton('Выход', self)
        exit_button.resize(int(self.width() * 0.6), int(self.height() * 0.12))
        exit_button.move(int(self.width() * 0.2), int(self.height() * 0.84))
        exit_button.clicked.connect(self.my_exit)

    def open_view_window(self):
        """
        Метод открытия окна просмотра базы данных.
        С помощью получаемого ключа вызывает показ нужного виджета.
        """

        key = constants.BUTTON_TEXT_TO_KEYS[self.sender().text()]
        self.parent().menu_window.hide()
        if key == 'title':
            self.parent().browse_by_title_window.filter_lineedit.clear()
            self.parent().browse_by_title_window.load_table()
            self.parent().browse_by_title_window.show()
        elif key == 'complexity':
            self.parent().browse_by_complexity_window.filter_lineedit.clear()
            self.parent().browse_by_complexity_window.load_table()
            self.parent().browse_by_complexity_window.show()
        else:
            self.parent().browse_by_ingredients_window.filter_lineedit.clear()
            self.parent().browse_by_ingredients_window.load_table()
            self.parent().browse_by_ingredients_window.show()

    def open_add_window(self):
        self.parent().menu_window.hide()
        self.parent().add_recept_window.show()

    def show_information(self):
        """
        Метод открытия окна инструкции.
        """

        self.information_window = MyInformationWindow()

    def my_exit(self):
        """
        Метод закрытия приложения.
        Вызывает окно подтверждения действия.
        """

        exit_message_box = MyExitMessageBox('menu')
        user_answer = exit_message_box.exec()

        if user_answer == 0:
            sys.exit()
