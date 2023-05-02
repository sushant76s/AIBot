from pytesseract import pytesseract
import urllib.request
import cv2
import numpy as np
import urllib.request


class Features:
    def extract(image_url):

        path_to_tesseract = r"C:/Users/Sushant/OneDrive/Documents/Bots/TelegramBot/TBot1/Tesseract-OCR/tesseract"
        req = urllib.request.urlopen(image_url)
        arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        res = text[:-1]
        return res
    
    def improve_image(image_url):
        image_path = urllib.request.urlopen(image_url)
        image_array = np.asarray(bytearray(image_path.read()), dtype=np.uint8)
        img = cv2.imdecode(image_array, -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, result = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
        adaptive_res = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 2)

        cv2.imwrite("result-image.jpg", adaptive_res)