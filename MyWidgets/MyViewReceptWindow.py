from PyQt5.QtWidgets import QMainWindow, QLabel, QPlainTextEdit
from PyQt5.Qt import QPixmap
from PyQt5.QtGui import QIcon
import constants


class MyViewReceptWindow(QMainWindow):
    """
    Класс отображения рецепта.
    Показывает всю информацию о рецепте пользователю.
    """

    def __init__(self, data):
        """
        data - отображаемая пользователю информация
        """

        super().__init__()

        self.setWindowIcon(QIcon(constants.ICON_PATH))

        self.data = data[0]

        self.setWindowTitle('Рецепт: ' + self.data[1] + ' Сложность: ' + str(self.data[5]))

        background_label = QLabel(self)
        background_label.setPixmap(QPixmap(constants.VIEW_WINDOW_BACKGROUND_IMAGE))
        background_label.resize(*constants.VIEW_RECEPT_WINDOW_SIZE)

        self.setGeometry(800, 50, *constants.VIEW_RECEPT_WINDOW_SIZE)
        self.setFixedSize(*constants.VIEW_RECEPT_WINDOW_SIZE)

        self.initUI()

        self.show()

    def initUI(self):
        """
        Метод инициализации UI.
        Создает поля для текста и записывает их информацию.
        """

        meal_description = QPlainTextEdit(self)
        meal_description.resize(int(self.width() * 0.92), int(self.height() * 0.28))
        meal_description.move(int(self.width() * 0.04), int(self.height() * 0.04))
        meal_description.setPlainText('Краткое описание:\n\n' + self.data[3])
        meal_description.setReadOnly(True)

        meal_ingredients = QPlainTextEdit(self)
        meal_ingredients.resize(int(self.width() * 0.92), int(self.height() * 0.28))
        meal_ingredients.move(int(self.width() * 0.04), int(self.height() * 0.36))
        meal_ingredients.setPlainText('Ингредиенты:\n\n' + '\n'.join(self.data[2].split(';')))
        meal_ingredients.setReadOnly(True)

        meal_recept = QPlainTextEdit(self)
        meal_recept.resize(int(self.width() * 0.92), int(self.height() * 0.28))
        meal_recept.move(int(self.width() * 0.04), int(self.height() * 0.68))
        meal_recept.setPlainText('Рецепт:\n\n' + '\n'.join(self.data[4].split('&')))
        meal_recept.setReadOnly(True)
