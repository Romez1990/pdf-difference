from pathlib import Path
from threading import Thread
from typing import (
    Optional,
)

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

    def __browse_original(self) -> None:
        self.__original_path = self.__get_pdf_path('original')

    def __browse_copy(self) -> None:
        self.__copy_path = self.__get_pdf_path('copy')

    def __get_pdf_path(self, name: str) -> Path:
        caption = f'Open {name}'
        filter = 'Adobe PDF files (*.pdf)'
        path, _ = QFileDialog.getOpenFileName(self, caption, filter=filter)
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
