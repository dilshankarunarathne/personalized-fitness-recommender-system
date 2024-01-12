import re
import cv2
import nltk
import pytesseract

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ocr(img_path) -> str:
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.lower()


def process_text(text):
    sentences = nltk.sent_tokenize(text)  # Tokenize the text into sentences
    number_regex = r'\b\d{2,3}\b'  # Define the regular expression for a number
    final_numbers = {}  # number : priority

    for sentence in sentences:  # Iterate over the sentences
        # Tokenize the sentence into words
        words = nltk.word_tokenize(sentence)
        for i in range(len(words)):
            # Check if the word is a 2 or 3 digit number
            if re.match(number_regex, words[i]):
                final_numbers[words[i]] = 1  # gives a priority as 1

    # Iterate over the keys of the final_numbers dictionary
    for number in final_numbers.keys():
        # Find all occurrences of the number in the text
        occurrences = re.findall(r'\b' + number + r'\b', text)
        # The count of the number is the length of the occurrences list
        count = len(occurrences)
        # set the priority of the number, based on the count
        p = final_numbers[number] / count
        final_numbers[number] = p

    # Define the regular expression for a range
    range_regex = r'\b\d{2,3}\.\d{2}\b - \b\d{2,3}\.\d{2}\b'
    # Define the regular expression for a number in a range
    number_in_range_regex = r'\b\d{2,3}\.\d{2}\b'
    # Find all ranges in the text
    ranges = re.findall(range_regex, text)
    # Print the ranges
    for rang in ranges:
        # Find all numbers in the range
        numbers_in_range = re.findall(number_in_range_regex, rang)
        # reassign the priority of the numbers
        for number in numbers_in_range:
            p = final_numbers[number] / 2
            final_numbers[number] = p

    # Find the number with the highest priority
    # Initialize the number with the highest priority and its priority
    highest_priority_number = None
    highest_priority = 0

    # Iterate over the final_numbers dictionary
    for number, priority in final_numbers.items():
        # If the priority of the current number is higher than the highest priority found so far
        if priority > highest_priority:
            # Update the highest priority and the number with the highest priority
            highest_priority = priority
            highest_priority_number = number

    return highest_priority_number
