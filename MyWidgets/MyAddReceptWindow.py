from PyQt5.QtWidgets import QWidget, QLineEdit, QComboBox, QPlainTextEdit, QPushButton, QMessageBox, QLabel
from PyQt5.Qt import QPixmap
import config


class MyAddReceptWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, *config.SCREEN_SIZE)
        self.setFixedSize(*config.SCREEN_SIZE)

        background_label = QLabel(self)
        background_label.setPixmap(QPixmap(config.ADD_RECEPT_WINDOW_BACKGROUND_IMAGE))
        background_label.resize(*config.SCREEN_SIZE)

        self.initUI()

    def initUI(self):
        self.widgets = []

        self.recept_title = QLineEdit(self)
        self.recept_title.resize(int(self.width() * 0.8), int(self.height() * 0.05))
        self.recept_title.move(int(self.width() * 0.025), int(self.height() * 0.025))
        self.recept_title.setPlaceholderText('Введите название рецепта')
        self.widgets.append(self.recept_title)

        self.recept_compexity = QComboBox(self)
        self.recept_compexity.addItems(['1', '2', '3', '4', '5'])
        self.recept_compexity.setCurrentIndex(0)
        self.recept_compexity.resize(int(self.width() * 0.125), int(self.height() * 0.05))
        self.recept_compexity.move(int(self.width() * 0.85), int(self.height() * 0.025))
        self.widgets.append(self.recept_compexity)

        self.recept_discriptoin = QPlainTextEdit(self)
        self.recept_discriptoin.resize(int(self.width() * 0.95), int(self.height() * 0.15))
        self.recept_discriptoin.move(int(self.width() * 0.025), int(self.height() * 0.1))
        self.recept_discriptoin.setPlaceholderText('Введите краткое описание блюда')
        self.widgets.append(self.recept_discriptoin)

        self.recept_ingridients = QPlainTextEdit(self)
        self.recept_ingridients.resize(int(self.width() * 0.95), int(self.height() * 0.2625))
        self.recept_ingridients.move(int(self.width() * 0.025), int(self.height() * 0.275))
        self.recept_ingridients.setReadOnly(True)
        self.recept_ingridients.setPlaceholderText('Здесь будут отображаться используемые ингредиенты')
        self.widgets.append(self.recept_ingridients)

        self.enter_ingridient = QLineEdit(self)
        self.enter_ingridient.resize(int(self.width() * 0.5), int(self.height() * 0.05))
        self.enter_ingridient.move(int(self.width() * 0.025), int(self.height() * 0.5625))
        self.enter_ingridient.setPlaceholderText('Введите следующий ингредиент без массы')
        self.widgets.append(self.enter_ingridient)

        add_entered_ingridient_button = QPushButton('Добавить', self)
        add_entered_ingridient_button.resize(int(self.width() * 0.2), int(self.height() * 0.05))
        add_entered_ingridient_button.move(int(self.width() * 0.55), int(self.height() * 0.5625))
        add_entered_ingridient_button.clicked.connect(self.add_entered_ingridient)

        delete_last_ingridient_button = QPushButton('Удалить', self)
        delete_last_ingridient_button.resize(int(self.width() * 0.2), int(self.height() * 0.05))
        delete_last_ingridient_button.move(int(self.width() * 0.775), int(self.height() * 0.5625))
        delete_last_ingridient_button.clicked.connect(self.delete_last_ingridient)

        self.recept_steps = QPlainTextEdit(self)
        self.recept_steps.resize(int(self.width() * 0.95), int(self.height() * 0.2))
        self.recept_steps.move(int(self.width() * 0.025), int(self.height() * 0.6375))
        self.recept_steps.setReadOnly(True)
        self.recept_steps.setPlaceholderText('Здесь будут отображаться этапы приготовления')
        self.widgets.append(self.recept_steps)

        self.enter_step = QLineEdit(self)
        self.enter_step.resize(int(self.width() * 0.5), int(self.height() * 0.05))
        self.enter_step.move(int(self.width() * 0.025), int(self.height() * 0.8625))
        self.enter_step.setPlaceholderText('Введите следующий этап приготовления')
        self.widgets.append(self.enter_step)

        add_entered_step_button = QPushButton('Добавить', self)
        add_entered_step_button.resize(int(self.width() * 0.2), int(self.height() * 0.05))
        add_entered_step_button.move(int(self.width() * 0.55), int(self.height() * 0.8625))
        add_entered_step_button.clicked.connect(self.add_entered_step)

        delete_last_step_button = QPushButton('Удалить', self)
        delete_last_step_button.resize(int(self.width() * 0.2), int(self.height() * 0.05))
        delete_last_step_button.move(int(self.width() * 0.775), int(self.height() * 0.8625))
        delete_last_step_button.clicked.connect(self.delete_last_step)

        save_recept_button = QPushButton('Сохранить рецепт', self)
        save_recept_button.resize(int(self.width() * 0.30), int(self.height() * 0.05))
        save_recept_button.move(int(self.width() * 0.025), int(self.height() * 0.925))
        save_recept_button.clicked.connect(self.save_recept)

        clear_form_button = QPushButton('Очистить форму', self)
        clear_form_button.resize(int(self.width() * 0.30), int(self.height() * 0.05))
        clear_form_button.move(int(self.width() * 0.35), int(self.height() * 0.925))
        clear_form_button.clicked.connect(self.clear_form)

        return_to_menu_button = QPushButton('Вернуться в меню', self)
        return_to_menu_button.resize(int(self.width() * 0.30), int(self.height() * 0.05))
        return_to_menu_button.move(int(self.width() * 0.675), int(self.height() * 0.925))
        return_to_menu_button.clicked.connect(self.return_to_menu)

    def add_entered_ingridient(self):
        ingridient = self.enter_ingridient.text()
        if ingridient and ingridient != '\n':
            entered_ingridients = self.recept_ingridients.toPlainText().split('\n')

            if entered_ingridients == ['']:
                entered_ingridients = []

            entered_ingridients.append(ingridient)
            self.recept_ingridients.setPlainText(
                '\n'.join(entered_ingridients)
            )

        self.enter_ingridient.setText('')

    def delete_last_ingridient(self):
        old_text = self.recept_ingridients.toPlainText()

        if old_text:
            self.recept_ingridients.setPlainText(
                '\n'.join(old_text.split('\n')[:-1])
            )

    def add_entered_step(self):
        step = self.enter_step.text()

        if step:
            old_text = self.recept_steps.toPlainText().split('\n')
            if old_text in ([''], ['\n']):
                old_text = []
                last_number = 0
            else:
                last_number = int(old_text[-1].split('.')[0])
            old_text.append(str(last_number + 1) + '. ' + step)
            self.recept_steps.setPlainText(
                '\n'.join(old_text)
            )

        self.enter_step.setText('')

    def delete_last_step(self):
        old_text = self.recept_steps.toPlainText()

        if old_text:
            self.recept_steps.setPlainText(
                '\n'.join(old_text.split('\n')[:-1])
            )

    def save_recept(self):
        title = self.recept_title.text().lower()
        complexity = int(self.recept_compexity.currentText())
        description = self.recept_discriptoin.toPlainText().lower()
        ingrigients = ';'.join(self.recept_ingridients.toPlainText().split('\n')).lower()
        recept = '&'.join(self.recept_steps.toPlainText().split('\n')).lower()

        if sum(map(lambda x: 1 if x else 0, [title,
                                             complexity,
                                             description,
                                             ingrigients,
                                             recept])) != 5:
            QMessageBox.critical(self, 'Ошибка ', 'Вы заполнили не все поля', QMessageBox.Ok)
            return

        cur = self.parent().database_connection.cursor()
        cur.execute(f'INSERT INTO recepts(title, ingredients, description, recept, complexity) VALUES'
                    f'("{title}", "{ingrigients}", "{description}", "{recept}", {complexity})')
        self.parent().database_connection.commit()
        QMessageBox.information(self, 'Успех ', 'Рецепт успешно сохранен', QMessageBox.Ok)
        self.clear_form()
        self.hide()
        self.parent().menu_window.show()

    def return_to_menu(self):
        self.clear_form()
        self.hide()
        self.parent().menu_window.show()

    def clear_form(self):
        for widget in self.widgets:
            widget.clear()
        self.recept_compexity.addItems(['1', '2', '3', '4', '5'])
        self.recept_compexity.setCurrentIndex(0)
