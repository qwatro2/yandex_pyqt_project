from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox
import sys
import config


class MyMenuWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, *config.SCREEN_SIZE)
        self.setFixedSize(*config.SCREEN_SIZE)

        self.initUI()

    def initUI(self):
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

        info_button = QPushButton('Информация', self)
        info_button.resize(int(self.width() * 0.6), int(self.height() * 0.12))
        info_button.move(int(self.width() * 0.2), int(self.height() * 0.68))
        info_button.clicked.connect(self.show_information)

        exit_button = QPushButton('Выход', self)
        exit_button.resize(int(self.width() * 0.6), int(self.height() * 0.12))
        exit_button.move(int(self.width() * 0.2), int(self.height() * 0.84))
        exit_button.clicked.connect(sys.exit)

    def open_view_window(self):
        key = config.BUTTON_TEXT_TO_KEYS[self.sender().text()]
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
        QMessageBox.question(self, 'Удалить', 'В форме добавления рецептов кнопка '
                                              '"Удалить" удаляет только последнюю '
                                              'строку, а не очищает соответствующее поле полностью', QMessageBox.Ok)
