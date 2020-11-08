from io import BytesIO
from pathlib import Path
from typing import (
    List,
)
from pdf2image import convert_from_path
from img2pdf import convert
from PIL import Image

from .paths import poppler_path


def convert_pdf_to_images(path: Path) -> List[bytes]:
    pages = convert_from_path(str(path),
                              poppler_path=poppler_path)
    pages_bytes = []
    for page in pages:
        pages_bytes.append(convert_image_to_bytes(page))
    return pages_bytes


def convert_image_to_bytes(image: Image) -> bytes:
    bytes_io = BytesIO()
    image.save(bytes_io, 'JPEG')
    return bytes_io.getvalue()


def convert_images_to_pdf(images: List[bytes]) -> bytes:
    return convert(images)
