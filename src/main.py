from pathlib import Path

from .difference import get_difference
from .paths import (
    project_path,
    document_samples_path,
)


def main() -> None:
    difference = get_difference(document_samples_path / 'original.pdf',
                                document_samples_path / 'copy.pdf')
    save(difference, project_path / 'output' / f'difference.jpg')


def save(image: bytes, file_path: Path) -> None:
    directory = file_path.parent
    directory.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(image)


main()
