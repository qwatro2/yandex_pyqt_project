from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QPlainTextEdit
from PyQt5.Qt import QPixmap
import config


class MyInformationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Инструкция')

        self.setGeometry(800, 50, *config.INFO_WINDOW_SIZE)
        self.setFixedSize(*config.INFO_WINDOW_SIZE)

        self.counter = 0

        self.initUI()

        self.show()

    def initUI(self):
        self.image_label = QLabel(self)
        self.image_label.resize(*config.SCREEN_SIZE)
        left_border = (self.width() - self.image_label.width()) // 2
        self.image_label.move(left_border, int(self.height() * 0.01))

        self.next_info_button = QPushButton('Далее', self)
        self.next_info_button.resize(int(self.width() * 0.3), int(self.height() * 0.05))
        self.next_info_button.move(self.width() - left_border - self.next_info_button.width(),
                                   self.height() - self.next_info_button.height() - int(self.height() * 0.01))
        self.next_info_button.clicked.connect(self.next_info)

        self.previous_info_button = QPushButton('Назад', self)
        self.previous_info_button.resize(int(self.width() * 0.3), int(self.height() * 0.05))
        self.previous_info_button.move(left_border,
                                       self.height() - self.previous_info_button.height() - int(self.height() * 0.01))
        self.previous_info_button.clicked.connect(self.previous_info)

        self.text_plain = QPlainTextEdit(self)
        self.text_plain.resize(config.SCREEN_SIZE[0], int(self.height() * 0.96) -
                               self.image_label.height() - self.next_info_button.height())
        self.text_plain.move(left_border, int(self.height() * 0.02) + self.image_label.height())
        self.text_plain.setReadOnly(True)

        self.show_info_by_counter()

    def show_info_by_counter(self):
        if self.counter == 4:
            self.next_info_button.setEnabled(False)

        if self.counter == 3:
            self.next_info_button.setEnabled(True)

        if self.counter == 0:
            self.previous_info_button.setEnabled(False)

        if self.counter == 1:
            self.previous_info_button.setEnabled(True)

        self.image_label.setPixmap(QPixmap(config.INFORMATION_DICT[self.counter][0]))
        self.text_plain.setPlainText(config.INFORMATION_DICT[self.counter][1])

    def next_info(self):
        self.counter += 1
        self.show_info_by_counter()

    def previous_info(self):
        self.counter -= 1
        self.show_info_by_counter()
