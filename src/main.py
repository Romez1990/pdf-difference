from sys import argv, exit
from PyQt5.QtWidgets import QApplication

from .windows import MainWindow


def main() -> None:
    app = QApplication(argv)
    main_window = MainWindow()
    main_window.show()
    exit_code = app.exec()
    exit(exit_code)


main()
