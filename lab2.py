import cv2
import numpy as np

def filtrowanie_obrazu_z_kamery():
    # a) Wczytanie obrazu z kamery
    cap = cv2.VideoCapture(0)  # 0 oznacza pierwszą kamerę
    ret, frame = cap.read()
    cap.release()  # Zwolnienie kamery

    # b) Konwersja do skali szarości
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # c) Wykrywanie krawędzi metodą Laplace
    laplacian_edges = cv2.Laplacian(gray_image, cv2.CV_64F)

    # Parametry dla algorytmu Canny
    minVal = 50
    maxVal = 100
    edges_canny = cv2.Canny(gray_image, minVal, maxVal)

    # Wyświetlenie wyników
    cv2.imshow('Oryginalny obraz', gray_image)
    cv2.imshow('Wykrywanie krawędzi Laplace', laplacian_edges)
    cv2.imshow('Wykrywanie krawędzi Canny', edges_canny)

    # d) Filtrowanie obrazu gaussowskiego
    gaussian_blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Wykrywanie krawędzi metodą Canny po filtracji
    edges_canny_blurred = cv2.Canny(gaussian_blurred, minVal, maxVal)

    # Wyświetlenie wyników po filtracji
    cv2.imshow('Obraz po filtrze gaussowskim', gaussian_blurred)
    cv2.imshow('Wykrywanie krawędzi Canny po filtrze', edges_canny_blurred)

    # f) Wykrywanie linii metodą transformacji Hough
    lines = cv2.HoughLinesP(edges_canny_blurred, 1, np.pi / 180, threshold=50, minLineLength=30, maxLineGap=5)

    # Rysowanie linii na obrazie
    hough_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)  # Przekształcenie w kolor
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(hough_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Wyświetlenie wyniku
    cv2.imshow('Wykryte linie metodą Hough', hough_image)

    # Oczekiwanie na naciśnięcie klawisza i zamknięcie wszystkich okien
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Wywołanie funkcji
filtrowanie_obrazu_z_kamery()
