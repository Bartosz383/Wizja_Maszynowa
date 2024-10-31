import tkinter as tk
from lab1 import Program

# Funkcja uruchamiająca program
def start_program():
    app.withdraw()  # Ukryj menu Tkinter
    program = Program()
    program.uruchom()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    app.deiconify()  # Ponownie pokaż menu po zamknięciu okna OpenCV

# Tworzenie menu Tkinter
app = tk.Tk()
app.title("Menu Programu")
app.geometry("300x200")

# Tworzenie przycisków
start_button = tk.Button(app, text="Laboratoria 1", command=start_program, width=20, height=2)
start_button.pack(pady=10)

exit_button = tk.Button(app, text="Wyjście", command=app.quit, width=20, height=2)
exit_button.pack(pady=10)

# Uruchomienie menu
app.mainloop()
