import cv2
import numpy as np
import tkinter as tk
from tkinter import messagebox

# Definicja funkcji filtrowania obrazu z pliku bez wykrywania okręgów
def filtrowanie_obrazu_z_pliku(image_path):
    frame = cv2.imread(image_path)
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian_edges = cv2.Laplacian(gray_image, cv2.CV_64F)

    minVal = 50
    maxVal = 100
    edges_canny = cv2.Canny(gray_image, minVal, maxVal)

    gaussian_blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges_canny_blurred = cv2.Canny(gaussian_blurred, minVal, maxVal)

    # Wyświetlenie wyników
    cv2.imshow('Oryginalny obraz', gray_image)
    cv2.imshow('Wykrywanie krawędzi Laplace', laplacian_edges)
    cv2.imshow('Wykrywanie krawędzi Canny', edges_canny)
    cv2.imshow('Obraz po filtrze gaussowskim', gaussian_blurred)
    cv2.imshow('Wykrywanie krawędzi Canny po filtrze', edges_canny_blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Definicja funkcji filtrowania obrazu z pliku z wykrywaniem okręgów
def filtrowanie_obrazu_z_pliku_z_okregami(image_path):
    frame = cv2.imread(image_path)
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian_edges = cv2.Laplacian(gray_image, cv2.CV_64F)

    minVal = 50
    maxVal = 100
    edges_canny = cv2.Canny(gray_image, minVal, maxVal)

    gaussian_blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges_canny_blurred = cv2.Canny(gaussian_blurred, minVal, maxVal)

    # Wykrywanie okręgów metodą Hougha
    circles = cv2.HoughCircles(edges_canny_blurred,
                               cv2.HOUGH_GRADIENT,
                               dp=2,
                               minDist=200,
                               param1=150,
                               param2=85,
                               minRadius=150,
                               maxRadius=200)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Okrąg
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)  # Środek okręgu

    # Wyświetlenie wyników
    cv2.imshow('Wykryte okręgi', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Definicja funkcji filtrowania obrazu z kamery
def filtrowanie_obrazu_z_kamery():
    cap = cv2.VideoCapture(0)  # 0 oznacza pierwszą kamerę
    ret, frame = cap.read()
    cap.release()  # Zwolnienie kamery
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    laplacian_edges = cv2.Laplacian(gray_image, cv2.CV_64F)
    minVal = 50
    maxVal = 100
    edges_canny = cv2.Canny(gray_image, minVal, maxVal)

    gaussian_blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edges_canny_blurred = cv2.Canny(gaussian_blurred, minVal, maxVal)

    # Wykrywanie okręgów metodą Hougha
    circles = cv2.HoughCircles(edges_canny_blurred,
                               cv2.HOUGH_GRADIENT,
                               dp=2,
                               minDist=200,
                               param1=150,
                               param2=85,
                               minRadius=150,
                               maxRadius=200)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Okrąg
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)  # Środek okręgu

    # Wyświetlenie wyników
    cv2.imshow('Oryginalny obraz', gray_image)
    cv2.imshow('Wykrywanie krawędzi Laplace', laplacian_edges)
    cv2.imshow('Wykrywanie krawędzi Canny', edges_canny)
    cv2.imshow('Obraz po filtrze gaussowskim', gaussian_blurred)
    cv2.imshow('Wykrywanie krawędzi Canny po filtrze', edges_canny_blurred)
    cv2.imshow('Wykryte okręgi', frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Funkcja do obsługi przycisków
def wybierz_funkcje(funkcja):
    if funkcja == 'lab2_1':
        filtrowanie_obrazu_z_pliku('lab2_1.jpg')
    elif funkcja == 'lab2_2':
        filtrowanie_obrazu_z_pliku_z_okregami('lab2_2.png')
    elif funkcja == 'kamera':
        filtrowanie_obrazu_z_kamery()
    else:
        messagebox.showerror("Błąd", "Nieznana funkcja")
