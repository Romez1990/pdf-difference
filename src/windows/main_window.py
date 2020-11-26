from pathlib import Path
from threading import Thread
from typing import (
    Optional,
)
import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from ..difference import get_difference
from ..recent_files import (
    save_file,
    open_file,
)
from .main_window_ui import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.__init_ui()
        self.__original_path: Optional[Path] = None
        self.__copy_path: Optional[Path] = None

    def __init_ui(self) -> None:
        self.pushButton_1.clicked.connect(self.__browse_original)
        self.pushButton_3.clicked.connect(self.__browse_copy)
        self.pushButton_2.clicked.connect(self.__compare)
        self.progressBar_2.hide()
        self.textEdit_2.hide()
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.verticalScrollBar().hide()
        self.textEdit_2.setFrameStyle(0)
        self.textEdit_1.hide()
        self.textEdit_1.setReadOnly(True)
        self.textEdit_1.verticalScrollBar().hide()
        self.textEdit_1.setFrameStyle(0)

    def __browse_original(self) -> None:
        self.__original_path = self.__get_pdf_path('original')
        self.__show_file_name(self.textEdit_2, self.__original_path)
    def __browse_copy(self) -> None:
        self.__copy_path = self.__get_pdf_path('copy')
        self.__show_file_name(self.textEdit_1, self.__copy_path)

    def __get_pdf_path(self, name: str) -> Path:
        caption = f'Open {name}'
        filter = 'Adobe PDF files (*.pdf)'
        path, _ = QFileDialog.getOpenFileName(self, caption, filter=filter)
        if len(path) == 0:      #если при выборе жмакнуть отмену
            path = None         #то все равно берется какой-то путь
        else:                   #вот за этим тут if else :^)
            return Path(path)

    def __compare(self):
        if self.__original_path is None or self.__copy_path is None:
            self.__show_error()
            return

        Thread(target=self.__compare_and_show).start()

    def __compare_and_show(self) -> None:
        result = get_difference(self.__original_path, self.__copy_path)
        result_path = save_file(result)
        open_file(result_path)

    def __show_error(self) -> None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('One of files is not selected')
        msg.setWindowTitle('Error')
        msg.exec()

    def __show_file_name(self, textEdit, file):
        if file is None:
            textEdit.hide()
        else:        #ну тут просто берем название файла, а не фул путь
            textEdit.setText(os.path.basename(str(file)))
            textEdit.show()
    #гифку я пока не докрутил, время спать уже :^(
