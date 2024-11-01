# import cv2
# import pytesseract
# import numpy as np
#
# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
#
# img = cv2.imread("lab4_1.png")
# cv2.imwrite("new_lab4_1.png", img)  # zapisuje obraz jako nowy plik
# imgArray = np.asarray(cv2.imread("new_lab4_1.png"))
#
# print('Wynik:', imgArray )

import cv2
import pytesseract
import numpy as np
import qrcode

# Ścieżka do Tesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

# Inicjalizacja kamery
cap = cv2.VideoCapture(0)  # 0 oznacza domyślną kamerę

# Sprawdź, czy kamera została poprawnie otwarta
if not cap.isOpened():
    print("Nie można otworzyć kamery")
    exit()

# Przechwycenie jednej klatki z kamery
ret, frame = cap.read()

if ret:
    # Zapisz przechwycony obraz jako nowy plik
    cv2.imwrite("new_lab4_camera.png", frame)

    # Przekształć obraz na tablicę numpy
    imgArray = np.asarray(frame)

    # Wyświetl wynik
    print('Wynik:', imgArray)

    # Pokaż obraz z kamery
    cv2.imshow("Obraz z kamery", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/Nie udało się przechwycić obrazu")

img=qrcode.make('Mój kod QR')
img.save('moj_qr.png')
# Zwolnij zasoby kamery
cap.release()
