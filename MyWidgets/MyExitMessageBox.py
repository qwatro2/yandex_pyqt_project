from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import constants


class MyExitMessageBox(QMessageBox):
    """
    Класс кастомизированного диалогового окна.
    """

    def __init__(self, key):
        super().__init__()
        self.addButton('Да', QMessageBox.YesRole)
        self.addButton('Отмена', QMessageBox.NoRole)
        self.setText(constants.MESSAGE_BOX_TEXTS[key])
        self.setWindowTitle('Уверены? ')
        self.setWindowIcon(QIcon(constants.ICON_PATH))
