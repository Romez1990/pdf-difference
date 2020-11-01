from pathlib import Path

from .convert_pdf import convert_pdf_to_images
from .difference import get_difference_between_images
from .paths import (
    project_path,
    document_samples_path,
)


def main() -> None:
    original_pages = convert_pdf_to_images(document_samples_path / 'original.pdf')
    copy_pages = convert_pdf_to_images(document_samples_path / 'copy.pdf')
    for number, pages in enumerate(zip(original_pages, copy_pages), 1):
        original_page, copy_page = pages
        difference = get_difference_between_images(original_page, copy_page)
        save(difference, project_path / 'output' / f'page {number}.jpg')


def save(image: bytes, file_path: Path) -> None:
    directory = file_path.parent
    directory.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(image)


main()
