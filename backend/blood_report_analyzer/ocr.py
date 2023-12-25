import cv2
import pytesseract
import numpy as np
import base64

# from backend.config import get

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# tessdata_dir_config = get('tesseract', 'dir')
# pytesseract.pytesseract.tesseract_cmd = get('tesseract', 'cmd')


def ocr_img(img_path) -> str:
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.lower()


def ocr_img_base64(img_data: str) -> str:
    # Decode the base64 string into bytes
    img_bytes = base64.b64decode(img_data)

    # Convert the bytes to a numpy array
    nparr = np.frombuffer(img_bytes, np.uint8)

    # Convert numpy array to image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale image
    text = pytesseract.image_to_string(gray)

    return text.lower()
