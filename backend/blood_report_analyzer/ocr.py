import cv2
import pytesseract

# from backend.config import get

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# tessdata_dir_config = get('tesseract', 'dir')
# pytesseract.pytesseract.tesseract_cmd = get('tesseract', 'cmd')


def ocr(img_path) -> str:
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.lower()
