from pathlib import Path
from os import startfile
from os.path import getctime
from datetime import datetime
from typing import (
    List,
)

from .paths import (
    recent_files_path,
)


def save_file(file_bytes: bytes) -> Path:
    current_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    filename = f'{current_datetime}.pdf'
    path = recent_files_path / filename
    recent_files_path.mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as file:
        file.write(file_bytes)
    add_to_recent(path)
    return path


def read_recent_files() -> List[Path]:
    if not recent_files_path.exists():
        return []
    files: List[Path] = []
    for file in recent_files_path.iterdir():
        if file.suffix == '.pdf':
            files.append(file)
    files.sort(key=get_creation_datetime, reverse=True)
    return files


def get_creation_datetime(file: Path) -> datetime:
    timestamp = getctime(file)
    return datetime.fromtimestamp(timestamp)


recent_files = read_recent_files()


def add_to_recent(path: Path) -> None:
    recent_files.insert(0, path)


def open_file(path: Path) -> None:
    startfile(path)
