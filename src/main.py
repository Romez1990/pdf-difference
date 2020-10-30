from pathlib import Path

from .convert_pdf import convert_pdf_to_images
from .paths import (
    project_path,
    document_samples_path,
)


def main() -> None:
    pages = convert_pdf_to_images(document_samples_path / 'original.pdf')
    for number, page in enumerate(pages, 1):
        save(page, project_path / 'output' / f'page {number}.jpg')


def save(image: bytes, file_path: Path) -> None:
    directory = file_path.parent
    directory.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(image)


main()
