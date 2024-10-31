import tkinter as tk
from lab1 import Program1
from lab2 import *

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

# Tworzenie menu Tkinter
app = tk.Tk()
app.title("Menu Programu")
app.geometry("300x200")

# Tworzenie ramki dla przycisku "Laboratoria 1" i etykiety
frame1 = tk.Frame(app)
frame1.pack(pady=10)

# Tworzenie przycisku "Laboratoria 1"
start_button = tk.Button(frame1, text="Laboratoria 1", command=start_program_lab1, width=20, height=2)
start_button.pack(side=tk.LEFT)  # Umieszczamy przycisk po lewej stronie

# Utworzenie etykiety z informacją obok przycisku "Laboratoria 1"
info_label1 = tk.Label(frame1, text="Przycisk S zapisuje obraz")
info_label1.pack(side=tk.LEFT, padx=(10, 0))  # Dodanie odstępu po lewej stronie etykiety

# Tworzenie ramki dla przycisku "Laboratoria 2" i etykiety
frame2 = tk.Frame(app)
frame2.pack(pady=10)

# Tworzenie przycisku "Laboratoria 2"
start_button = tk.Button(frame2, text="Laboratoria 2", command=start_program_lab2, width=20, height=2)
start_button.pack(side=tk.LEFT)  # Umieszczamy przycisk po lewej stronie

# Utworzenie etykiety z informacją obok przycisku "Laboratoria 2"
info_label2 = tk.Label(frame2, text="Przycisk S zapisuje obraz")
info_label2.pack(side=tk.LEFT, padx=(10, 0))  # Dodanie odstępu po lewej stronie etykiety

# Tworzenie ramki dla przycisku "Wyjście" i etykiety
frameW = tk.Frame(app)
frameW.pack(pady=10)

# Tworzenie przycisku "Wyjście"
exit_button = tk.Button(frameW, text="Wyjście", command=app.quit, width=20, height=2)
exit_button.pack(side=tk.LEFT)  # Umieszczamy przycisk po lewej stronie

# Utworzenie etykiety z informacją obok przycisku "Wyjście"
info_label3 = tk.Label(frameW, text="Zamyka program")
info_label3.pack(side=tk.LEFT, padx=(10, 0))  # Dodanie odstępu po lewej stronie etykiety

# Uruchomienie menu
app.mainloop()
