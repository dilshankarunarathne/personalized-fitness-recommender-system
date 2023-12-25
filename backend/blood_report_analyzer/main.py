from backend.blood_report_analyzer.analyzer import process_sugar_report_text
from backend.blood_report_analyzer.ocr import ocr_img_base64


def analyze_blood_sugar_report(report_img_data):
    # TODO read base64 str image data
    # convert to text using ocr module
    img_txt = ocr_img_base64(report_img_data)

    # process text using analyzer module
    blood_sugar_level = process_sugar_report_text(img_txt)

    return blood_sugar_level
