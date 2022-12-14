# PDF Difference

В современном мире анализ документов является актуальной задачей. Во время работы с текстовыми документами часто приходится сравнивать их по содержанию. Эта необходимость возникает, если над документом работала группа людей или документ был отправлен на согласование и редактирование, нужно быстро найти все проделанные изменения. Сравнение документов вручную занимает очень много времени и влечет риск ошибок. На помощь приходят программы для анализа содержания документов на предмет ошибок или различий между макетами.

Разработанное решение может сравнивать не только текст, но и изображения. В ходе разработки были выбраны следующие технологии:

OpenCV – библиотека, предназначенная для решения проблем компьютерного зрения. Предоставляет различные алгоритмы для обработки графических изображений.

Qt – кроссплатформенный фреймворк для дизайна и разработки графического интерфейса. Предоставляет графическую среду для создания окон приложения.

pdf2image и img2pdf – библиотеки для конвертирования PDF файлов.

Разработанное решение состоит из нескольких модулей, осуществляющих свой функционал. Модуль чтения/записи PDF файлов – читает, а также распознаёт PDF файлы с диска. Модуль нахождения отличий, определяющий разницу в двух документах. Сравнивая их, он создаёт новый документ, в котором выделены отличающиеся объекты. Выделение показывается с помощью красный прямоугольников. Затем передаёт его в модуль файлов, который сохраняет его на диск и отображает пользователю, добавляя при этом в историю отсканированных файлов. Все обработанные документы сохраняются на диск и отображаются в программе.

Весь функционал подключен к графическому интерфейсу, с которым пользователь взаимодействует при помощи окна и элементов управления. Интерфейс предельно прост. Пользователю необходимо выбрать два файла и нажать кнопку сравнения, затем отобразится результат.

Таким образом, разработано решение, позволяющее сравнивать два документа и находить в них отличия. Поддерживается возможно сравнения, как текста, так и отсканированных файлов в виде картинки. Также сохраняется вся история и файлы с отличиями.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

What things you need to have globally installed:
- Python 3.9

Versions of Python higher than 3.9 are not tested with this project. The project might not start with Python 3.10 or higher

### Installing

Install project dependencies

```shell
pip install -r requirements.txt
```

or if this does not work you can try to install libraries manually

```shell
pip install pillow opencv-python scikit-image imutils pdf2image img2pdf numpy pyqt5
```

Run the program

```shell
python main.py
```
