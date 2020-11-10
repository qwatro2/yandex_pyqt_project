from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.Qt import QPixmap
from MyWidgets.MyViewReceptWindow import MyViewReceptWindow
import config


class MyViewWindow(QWidget):
    def __init__(self, parent, key):
        super().__init__(parent)

        self.key = key

        self.setGeometry(0, 0, *config.SCREEN_SIZE)
        self.setFixedSize(*config.SCREEN_SIZE)

        background_label = QLabel(self)
        background_label.setPixmap(QPixmap(config.VIEW_WINDOW_BACKGROUND_IMAGE))
        background_label.resize(*config.SCREEN_SIZE)

        self.initUI()

        self.load_table()

    def initUI(self):
        self.filter_lineedit = QLineEdit(self)
        self.filter_lineedit.resize(int(self.width() * 0.7), int(self.height() * 0.05))
        self.filter_lineedit.move(int(self.width() * 0.05), int(self.height() * 0.05))

        if self.key == 'title':
            placeholder = 'Введите название'
        elif self.key == 'complexity':
            placeholder = 'Введите число от 1 до 5 включительно'
        else:
            placeholder = 'Введите ингредиенты через ; без дополнительных пробелов'

        self.filter_lineedit.setPlaceholderText(placeholder)

        apply_filter_button = QPushButton('Найти', self)
        apply_filter_button.resize(int(self.width() * 0.15), int(self.height() * 0.05))
        apply_filter_button.move(int(self.width() * 0.8), int(self.height() * 0.05))
        apply_filter_button.clicked.connect(self.load_table)

        self.table = QTableWidget(self)
        self.table.resize(int(self.width() * 0.9), int(self.height() * 0.7))
        self.table.move(int(self.width() * 0.05), int(self.height() * 0.15))

        self.view_current_recept_button = QPushButton('Посмотреть', self)
        self.view_current_recept_button.resize(int(self.table.width() * 0.45), int(self.height() * 0.05))
        self.view_current_recept_button.move(int(self.width() * 0.05), int(self.height() * 0.9))
        self.view_current_recept_button.clicked.connect(self.open_current_recept)

        return_to_menu_button = QPushButton('Вернуться в меню', self)
        return_to_menu_button.resize(int(self.table.width() * 0.45), int(self.height() * 0.05))
        return_to_menu_button.move(int(self.width() * 0.545), int(self.height() * 0.9))
        return_to_menu_button.clicked.connect(self.return_to_menu)

    def load_table(self):
        cur = self.parent().database_connection.cursor()

        filter = self.filter_lineedit.text().lower()

        if self.key == 'title':
            query_result = cur.execute(f'SELECT title, description, complexity FROM recepts WHERE title LIKE'
                                       f' "%{filter}%" OR description LIKE "%{filter}%"').fetchall()
        elif self.key == 'complexity':
            if filter:
                if filter in ('1', '2', '3', '4', '5'):
                    query_result = cur.execute(f'SELECT title, description, complexity FROM recepts WHERE '
                                               f'complexity = {filter}').fetchall()
                else:
                    query_result = []
            else:
                query_result = cur.execute('SELECT title, description, complexity FROM recepts').fetchall()
        else:
            if filter:
                query_result = cur.execute('SELECT title, description,'
                                           ' ingredients, complexity FROM recepts').fetchall()
                template_result = []
                for i in query_result:
                    if {*filter.split(';')}.issubset({*i[2].split(';')}):
                        template_result.append(i)
                query_result = template_result[:]
            else:
                query_result = cur.execute('SELECT title, description,'
                                           ' ingredients, complexity FROM recepts').fetchall()

        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(len(query_result[0]) if query_result else 0)

        for i, content in enumerate(query_result):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, element in enumerate(content):
                table_widget_item = QTableWidgetItem(str(element))
                table_widget_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.table.setItem(i, j, table_widget_item)

        if not self.table.rowCount():
            self.table.setRowCount(1)
            self.table.setColumnCount(1)
            table_widget_item = QTableWidgetItem('Ничего не найдено')
            table_widget_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table.setItem(0, 0, table_widget_item)
            self.view_current_recept_button.setEnabled(False)
        else:
            if self.key == 'title':
                header_labels = ['Название блюда', 'Краткое описание', 'Сложность']
            elif self.key == 'complexity':
                header_labels = ['Название блюда', 'Краткое описание', 'Сложность']
            else:
                header_labels = ['Название блюда', 'Краткое описание', 'Ингредиенты', 'Сложность']

            self.table.setHorizontalHeaderLabels(header_labels)
            self.table.setCurrentCell(0, 0)
            self.view_current_recept_button.setEnabled(True)

        self.table.resizeColumnsToContents()

    def return_to_menu(self):
        self.hide()
        self.parent().menu_window.show()

    def open_current_recept(self):
        current_row = self.table.currentItem().row()
        choosen_title = self.table.item(current_row, 0).text()
        cur = self.parent().database_connection.cursor()
        self.view_recept_window = MyViewReceptWindow(cur.execute('''SELECT * FROM recepts 
        WHERE title = ?''', (choosen_title,)).fetchall())
