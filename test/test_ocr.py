import cv2
import pytesseract
import matplotlib.pyplot as plt
import re
import nltk

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


img = cv2.imread(image_path)
