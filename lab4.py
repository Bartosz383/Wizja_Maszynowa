import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

img = cv2.imread("lab4_1.png")
cv2.imwrite("new_lab4_1.png", img)  # zapisuje obraz jako nowy plik
imgArray = np.asarray(cv2.imread("new_lab4_1.png"))

print('Wynik:', imgArray )