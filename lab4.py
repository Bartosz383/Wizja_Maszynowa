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

# import cv2
# import pytesseract
# import numpy as np
# import qrcode
#
# # Ścieżka do Tesseract
# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
#
# # Inicjalizacja kamery
# cap = cv2.VideoCapture(0)  # 0 oznacza domyślną kamerę
#
# # Sprawdź, czy kamera została poprawnie otwarta
# if not cap.isOpened():
#     print("Nie można otworzyć kamery")
#     exit()
#
# # Przechwycenie jednej klatki z kamery
# ret, frame = cap.read()
#
# if ret:
#     # Zapisz przechwycony obraz jako nowy plik
#     cv2.imwrite("new_lab4_camera.png", frame)
#
#     # Przekształć obraz na tablicę numpy
#     imgArray = np.asarray(frame)
#
#     # Wyświetl wynik
#     print('Wynik tablicy obrazu:', imgArray)
#
#     # Pokaż obraz z kamery
#     cv2.imshow("Obraz z kamery", frame)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Nie udało się przechwycić obrazu")
#
# # Generowanie kodu QR
# qr_content = "Mój kod QR"
# qr_img = qrcode.make(qr_content)
# qr_img_path = "moj_qr.png"
# qr_img.save(qr_img_path)
# print(f"Zapisano kod QR pod ścieżką: {qr_img_path}")
#
# # Wczytanie i dekodowanie kodu QR
# img = cv2.imread(qr_img_path)
# det = cv2.QRCodeDetector()
# val, pts, st_code = det.detectAndDecode(img)
#
# # Sprawdzenie wartości kodu QR
# if val:
#     print("Wartość kodu QR:", val)
# else:
#     print("Nie udało się odczytać kodu QR")
#
# # Zwolnij zasoby kamery
# cap.release()

import cv2
import pytesseract
import numpy as np
import qrcode

def handle_qr_codes():
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Nie można otworzyć kamery")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite("new_lab4_camera.png", frame)
        imgArray = np.asarray(frame)
        print('Wynik tablicy obrazu:', imgArray)
        cv2.imshow("Obraz z kamery", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Nie udało się przechwycić obrazu")

    qr_content = "Mój kod QR"
    qr_img = qrcode.make(qr_content)
    qr_img_path = "moj_qr.png"
    qr_img.save(qr_img_path)
    print(f"Zapisano kod QR pod ścieżką: {qr_img_path}")

    img = cv2.imread(qr_img_path)
    det = cv2.QRCodeDetector()
    val, pts, st_code = det.detectAndDecode(img)
    if val:
        print("Wartość kodu QR:", val)
    else:
        print("Nie udało się odczytać kodu QR")

    cap.release()

def handle_aruco_codes():
    # Szablon funkcji do pracy z kodami ArUco
    print("Funkcja do przetwarzania kodów ArUco jeszcze nie zaimplementowana.")


