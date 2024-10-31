import numpy as np
import cv2
import tkinter as tk
from tkinter import Scale, HORIZONTAL

# Inicjalizacja klasyfikatorów Haar do wykrywania twarzy i oczu
face_cascade = cv2.CascadeClassifier("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/haarcascade_eye.xml")

# Funkcja do wykrywania twarzy
def detect_faces():
    cap = cv2.VideoCapture(0)
    while True:
        ret, color_image = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=15)
        for (x, y, w, h) in faces:
            cv2.rectangle(color_image, (x, y), (x + w, y + h), (190, 0, 0), 2)
        cv2.imshow('Face Detection', color_image)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Funkcja do wykrywania oczu
def detect_eyes():
    cap = cv2.VideoCapture(0)
    while True:
        ret, color_image = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=15)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(color_image, (ex, ey), (ex + ew, ey + eh), (0, 190, 0), 2)
        cv2.imshow('Eye Detection', color_image)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Funkcja do rozmywania wykrytych twarzy
def blur_faces():
    cap = cv2.VideoCapture(0)
    while True:
        ret, color_image = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=15)
        for (x, y, w, h) in faces:
            face = color_image[y:y+h, x:x+w]
            blur_value = blur_scale.get()
            face = cv2.blur(face, (blur_value, blur_value))
            color_image[y:y+h, x:x+w] = face
        cv2.imshow('Blurred Faces', color_image)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Funkcja do zakrywania oczu paskiem
def cover_eyes():
    cap = cv2.VideoCapture(0)
    while True:
        ret, color_image = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=15)
        for (ex, ey, ew, eh) in eyes:
            bar_height = eye_cover_height_scale.get()
            bar_width = eye_cover_width_scale.get()
            cv2.rectangle(color_image,
                          (ex + ew // 2 - bar_width // 2, ey + eh // 2 - bar_height // 2),
                          (ex + ew // 2 + bar_width // 2, ey + eh // 2 + bar_height // 2),
                          (0, 0, 0), -1)
        cv2.imshow('Covered Eyes', color_image)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# # Tworzenie GUI z tkinter
# root = tk.Tk()
# root.title("Wybierz program")
# root.geometry("300x450")
#
# # Nagłówek
# label = tk.Label(root, text="Wybierz funkcję detekcji:")
# label.pack(pady=10)
#
# # Przycisk dla wykrywania twarzy
# btn1 = tk.Button(root, text="Wykrywanie Twarzy", command=detect_faces)
# btn1.pack(pady=5)
#
# # Przycisk dla wykrywania oczu
# btn2 = tk.Button(root, text="Wykrywanie Oczu", command=detect_eyes)
# btn2.pack(pady=5)
#
# # Przycisk dla rozmywania twarzy
# btn3 = tk.Button(root, text="Rozmywanie Twarzy", command=blur_faces)
# btn3.pack(pady=5)
#
# # Suwak do ustawiania intensywności rozmycia
# blur_scale = Scale(root, from_=1, to=100, orient=HORIZONTAL, label="Poziom rozmycia")
# blur_scale.set(30)  # wartość początkowa
# blur_scale.pack(pady=5)
#
# # Przycisk dla zakrywania oczu
# btn4 = tk.Button(root, text="Zakrywanie Oczu", command=cover_eyes)
# btn4.pack(pady=5)
#
# # Suwak do ustawiania wysokości paska na oczy
# eye_cover_height_scale = Scale(root, from_=1, to=50, orient=HORIZONTAL, label="Wysokość paska na oczy")
# eye_cover_height_scale.set(10)  # wartość początkowa
# eye_cover_height_scale.pack(pady=5)
#
# # Suwak do ustawiania szerokości paska na oczy
# eye_cover_width_scale = Scale(root, from_=1, to=100, orient=HORIZONTAL, label="Szerokość paska na oczy")
# eye_cover_width_scale.set(30)  # wartość początkowa
# eye_cover_width_scale.pack(pady=5)
#
# root.mainloop()
