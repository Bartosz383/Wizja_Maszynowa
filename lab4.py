import pytesseract
import numpy as np
import qrcode
import cv2
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib

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
    matplotlib.use('TkAgg')  # Ustaw backend na TkAgg

    # Wybierz słownik ArUco
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

    # Ustawienia wykresu
    fig = plt.figure()
    nx = 4  # liczba kolumn
    ny = 3  # liczba wierszy

    # Generowanie markerów
    for i in range(1, nx * ny + 1):
        ax = fig.add_subplot(ny, nx, i)
        img = aruco.generateImageMarker(aruco_dict, i, 700)  # generowanie markera
        plt.imshow(img, cmap=mpl.cm.gray, interpolation="nearest")
        ax.axis("off")

    # Zapisz wykres do pliku
    plt.savefig("markers.jpg")

    # Wyświetl wykres
    plt.show()

# Funkcja do odczytu kodów ArUco ze ścieżki
def arc_uco_reading():
    path = "D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/markers.jpg"
    try:
        # Wczytaj obraz ze ścieżki
        frame = cv2.imread(path)
        if frame is None:
            print(f"Nie można wczytać obrazu ze ścieżki: {path}")
            return

        # Konwersja obrazu do skali szarości
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Wybierz słownik ArUco i utwórz detektor
        aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
        parameters = aruco.DetectorParameters()  # Poprawiony obiekt DetectorParameters
        detector = aruco.ArucoDetector(aruco_dict, parameters)

        # Wykrywanie markerów
        corners, ids, _ = detector.detectMarkers(gray)

        # Rysowanie wykrytych markerów na oryginalnym obrazie
        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)

        # Wyświetlanie obrazu z wykrytymi markerami
        cv2.imshow("Detected ArUco Markers", frame_markers)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Wypisz wykryte identyfikatory markerów
        if ids is not None:
            print("Wykryto następujące identyfikatory markerów ArUco:", ids.flatten())
        else:
            print("Nie wykryto żadnych markerów ArUco.")

    except Exception as e:
        print("Wystąpił błąd podczas odczytu kodów ArUco:", str(e))


