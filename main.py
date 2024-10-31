import tkinter as tk
from lab1 import Program1
from lab2 import *
from lab3 import *
import cv2

# Funkcja uruchamiająca program
def start_program_lab1():
    app.withdraw()  # Ukryj menu Tkinter
    program = Program1()
    program.uruchom()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    app.deiconify()  # Ponownie pokaż menu po zamknięciu okna OpenCV

def start_program_lab2():
    app.withdraw()  # Ukryj menu Tkinter
    open_lab2_window()  # Otwórz nowe okno dla laboratorium 2

def open_lab2_window():
    # Utworzenie nowego okna dla lab2
    lab2_window = tk.Toplevel(app)  # Użyj Toplevel dla nowego okna
    lab2_window.title("Wybór funkcji filtrowania obrazu")
    lab2_window.geometry("400x200")

    # Przycisk do wyboru funkcji dla lab2_1
    btn_lab2_1 = tk.Button(lab2_window, text="Filtry dla lab2_1.jpg", command=lambda: wybierz_funkcje('lab2_1'))
    btn_lab2_1.pack(pady=10)

    # Przycisk do wyboru funkcji dla lab2_2
    btn_lab2_2 = tk.Button(lab2_window, text="Filtry dla lab2_2.png", command=lambda: wybierz_funkcje('lab2_2'))
    btn_lab2_2.pack(pady=10)

    # Przycisk do wyboru funkcji z kamery
    btn_kamera = tk.Button(lab2_window, text="Filtry obrazu z kamery", command=lambda: wybierz_funkcje('kamera'))
    btn_kamera.pack(pady=10)

    # Dodaj możliwość zamknięcia okna
    lab2_window.protocol("WM_DELETE_WINDOW", lambda: close_lab2_window(lab2_window))

def close_lab2_window(window):
    window.destroy()  # Zamknij okno
    app.deiconify()   # Pokaż ponownie główne okno

# Funkcja uruchamiająca podprogram
def start_subprogram():
    app.withdraw()  # Ukryj menu główne
    open_subprogram_window()  # Uruchom okno podprogramu

def open_subprogram_window():
    # Tworzenie GUI dla podprogramu
    subprogram_window = tk.Toplevel(app)
    subprogram_window.title("Wybierz program")
    subprogram_window.geometry("300x450")

    label = tk.Label(subprogram_window, text="Wybierz funkcję detekcji:")
    label.pack(pady=10)

    # Przycisk dla wykrywania twarzy
    btn1 = tk.Button(subprogram_window, text="Wykrywanie Twarzy", command=detect_faces)
    btn1.pack(pady=5)

    # Przycisk dla wykrywania oczu
    btn2 = tk.Button(subprogram_window, text="Wykrywanie Oczu", command=detect_eyes)
    btn2.pack(pady=5)

    # Przycisk dla rozmywania twarzy
    btn3 = tk.Button(subprogram_window, text="Rozmywanie Twarzy", command=blur_faces)
    btn3.pack(pady=5)

    # Suwak do ustawiania intensywności rozmycia
    blur_scale = tk.Scale(subprogram_window, from_=1, to=100, orient=tk.HORIZONTAL, label="Poziom rozmycia")
    blur_scale.set(30)  # wartość początkowa
    blur_scale.pack(pady=5)

    # Przycisk dla zakrywania oczu
    btn4 = tk.Button(subprogram_window, text="Zakrywanie Oczu", command=cover_eyes)
    btn4.pack(pady=5)

    # Suwak do ustawiania wysokości i szerokości paska na oczy
    eye_cover_height_scale = tk.Scale(subprogram_window, from_=1, to=50, orient=tk.HORIZONTAL, label="Wysokość paska na oczy")
    eye_cover_height_scale.set(10)  # wartość początkowa
    eye_cover_height_scale.pack(pady=5)

    eye_cover_width_scale = tk.Scale(subprogram_window, from_=1, to=100, orient=tk.HORIZONTAL, label="Szerokość paska na oczy")
    eye_cover_width_scale.set(30)  # wartość początkowa
    eye_cover_width_scale.pack(pady=5)

    # Dodaj możliwość zamknięcia okna
    subprogram_window.protocol("WM_DELETE_WINDOW", lambda: close_subprogram_window(subprogram_window))

def close_subprogram_window(window):
    window.destroy()  # Zamknij okno
    app.deiconify()  # Pokaż ponownie główne okno

# Tworzenie menu Tkinter
app = tk.Tk()
app.title("Menu Programu")
app.geometry("300x400")

# Dodanie przycisków do laboratorium i podprogramu
frame1 = tk.Frame(app)
frame1.pack(pady=10)
start_button = tk.Button(frame1, text="Laboratoria 1", command=start_program_lab1, width=20, height=2)
start_button.pack(side=tk.LEFT)
info_label1 = tk.Label(frame1, text="Przycisk S zapisuje obraz")
info_label1.pack(side=tk.LEFT, padx=(10, 0))

frame2 = tk.Frame(app)
frame2.pack(pady=10)
start_button = tk.Button(frame2, text="Laboratoria 2", command=start_program_lab2, width=20, height=2)
start_button.pack(side=tk.LEFT)
info_label2 = tk.Label(frame2, text="Filtry na obrazy")
info_label2.pack(side=tk.LEFT, padx=(10, 0))

# Przycisk uruchomienia podprogramu
frame3 = tk.Frame(app)
frame3.pack(pady=10)
subprogram_button = tk.Button(frame3, text="Laboratoria 3", command=start_subprogram, width=20, height=2)
subprogram_button.pack(side=tk.LEFT)
info_label3 = tk.Label(frame3, text="Detekcja twarzy, oczu, blur, czarny pasek")
info_label3.pack(side=tk.LEFT, padx=(10, 0))

# Przycisk wyjścia
frameW = tk.Frame(app)
frameW.pack(pady=10)
exit_button = tk.Button(frameW, text="Wyjście", command=app.quit, width=20, height=2)
exit_button.pack(side=tk.LEFT)
info_label4 = tk.Label(frameW, text="Zamyka program")
info_label4.pack(side=tk.LEFT, padx=(10, 0))

# Uruchomienie menu
app.mainloop()
