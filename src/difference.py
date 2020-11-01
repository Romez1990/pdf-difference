from typing import (
    Tuple,
    List,
)
from numpy import (
    ndarray,
    asarray,
    uint8,
)
from cv2.cv2 import (
    imdecode,
    imencode,
    cvtColor,
    threshold,
    findContours,
    rectangle,
    boundingRect,
    IMREAD_COLOR,
    COLOR_BGR2GRAY,
    THRESH_BINARY_INV,
    THRESH_OTSU,
    RETR_EXTERNAL,
    CHAIN_APPROX_SIMPLE,
)
from skimage.metrics import (
    structural_similarity,
)
from imutils import (
    grab_contours,
)


def get_difference_between_images(image_1_bytes: bytes, image_2_bytes: bytes) -> bytes:
    image_1, gray_1 = decode_image(image_1_bytes)
    image_2, gray_2 = decode_image(image_2_bytes)
    difference = get_difference_gray(gray_1, gray_2)
    contours = get_contours(difference)
    draw_contours(image_2, contours)
    return imencode('.jpg', image_2)[1].tobytes()


def decode_image(image_bytes: bytes) -> Tuple[ndarray, ndarray]:
    image_array = asarray(bytearray(image_bytes), dtype=uint8)
    image = imdecode(image_array, IMREAD_COLOR)
    gray = cvtColor(image, COLOR_BGR2GRAY)
    return image, gray


def get_difference_gray(gray_1: ndarray, gray_2: ndarray) -> ndarray:
    score, diff = structural_similarity(gray_1, gray_2, full=True)
    return (diff * 255).astype('uint8')


def get_contours(difference: ndarray) -> List[ndarray]:
    thresh = threshold(difference, 0, 255, THRESH_BINARY_INV | THRESH_OTSU)[1]
    contours = findContours(thresh.copy(), RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
    return grab_contours(contours)


def draw_contours(image: ndarray, contours: List[ndarray]) -> None:
    for c in contours:
        x, y, w, h = boundingRect(c)
        rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
