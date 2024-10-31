# import pyrealsense2 as rs
# import numpy as np
# import cv2
# pipe = rs.pipeline()
# cfg = rs.config()
# cfg.enable_stream(rs.stream.color, 640,480, rs.format.bgr8, 30)
# cfg.enable_stream(rs.stream.depth, 640,480, rs.format.z16, 30)
# pipe.start(cfg)
# img = cv2.imread("11.png")
# rotate_matrix = cv2.getRotationMatrix2D(center=(1000,140),angle=30, scale=1)
# rotate_matrix2 = cv2.getRotationMatrix2D(center=(320,240),angle=330, scale=1)
# rotated = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(1200,1000))
# rotated2 = cv2.warpAffine(src=img, M=rotate_matrix2, dsize=(640,480))
# cv2.imshow('rot', rotated)
# cv2.imshow('rot2', rotated2)
# print (img.shape)
# print(img[50, 50])
# resized = cv2.resize(img, (320, 240))
# cv2.imshow('resized', resized)
# cv2.rectangle(img, )
# cv2.imshow('rgb', img)
# #img2 = img[20:200, 400:600]
# #cv2.imshow('obraz2', img2)
# #while True:
#     #frame = pipe.wait_for_frames()
#     #color_frame = frame.get_color_frame()
#     #color_image = np.asanyarray(color_frame.get_data())
#
#
#     #cv2.imshow('rgb', color_image)
#     #if cv2.waitKey(25) & 0xFF == ord('q'):
#         #cv2.imwrite('obraz.jpg', color_image)
#         #break
#
# pipe.stop()


import cv2
import numpy as np


# Klasa do obsługi kamery
class Kamera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def otworz_kamere(self):
        if not self.cap.isOpened():
            print("Nie można otworzyć kamery")
            return False
        return True

    def zamknij_kamere(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def detekcja_twarzy(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Nie można odczytać obrazu z kamery")
                break

            # Wykrywanie twarzy
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

            # Rysowanie prostokątów wokół twarzy
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.imshow("Kamera - twarze", frame)

            # Zapisz obraz przy nacisnięciu "s"
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite("obraz_z_kamery.jpg", frame)
                print("Zapisano obraz jako 'obraz_z_kamery.jpg'")
                break

            # Zatrzymaj kamerę przy nacisnięciu "q"
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


# Klasa do operacji na obrazie
class Obraz:
    def __init__(self, path):
        self.img = cv2.imread(path)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def parametry_obrazu(self):
        if self.img is not None:
            print("Parametry obrazu:", self.img.shape)
            cv2.imshow("Wczytany obraz", self.img)
        else:
            print("Błąd: Nie udało się wczytać obrazu")

    def kolor_piksela(self, x, y):
        if self.img is not None:
            print(f"Kolor piksela ({x}, {y}):", self.img[y, x])

    def wytnij_twarz(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            face_crop = self.img[y:y + h, x:x + w]
            cv2.imshow("Wycięta twarz", face_crop)
            cv2.imwrite("wycieta_twarz.jpg", face_crop)
            print("Wycięto twarz i zapisano jako 'wycieta_twarz.jpg'")
        else:
            print("Nie znaleziono twarzy do wycięcia")

    def zmniejsz_obraz(self):
        new_x, new_y = int(self.img.shape[1] * 0.5), int(self.img.shape[0] * 0.5)
        resized_img = cv2.resize(self.img, (new_x, new_y))
        cv2.imshow("Zmniejszony obraz", resized_img)

    def obroc_obraz(self):
        (h, w) = self.img.shape[:2]
        center = (w // 2, h // 2)
        rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=30, scale=1)

        # Rozszerzanie rozmiaru wyjściowego obrazu, aby zapobiec przycięciu
        cos = np.abs(rotate_matrix[0, 0])
        sin = np.abs(rotate_matrix[0, 1])
        new_w = int((h * sin) + (w * cos))
        new_h = int((h * cos) + (w * sin))
        rotate_matrix[0, 2] += (new_w / 2) - center[0]
        rotate_matrix[1, 2] += (new_h / 2) - center[1]

        rotated_img = cv2.warpAffine(self.img, rotate_matrix, (new_w, new_h))
        cv2.imshow("Obrócony obraz", rotated_img)
        cv2.imwrite("obrocony_obraz.jpg", rotated_img)
        print("Obrócony obraz zapisano jako 'obrocony_obraz.jpg'")

    def oznacz_twarz(self, imie_nazwisko):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(self.img, imie_nazwisko, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.imshow("Oznaczona twarz", self.img)


# Klasa główna programu
class Program:
    def __init__(self):
        self.kamera = Kamera()
        self.obraz = None

    def uruchom(self):
        if self.kamera.otworz_kamere():
            self.kamera.detekcja_twarzy()
            self.kamera.zamknij_kamere()

        self.obraz = Obraz("obraz_z_kamery.jpg")
        self.obraz.parametry_obrazu()
        self.obraz.kolor_piksela(50, 50)
        self.obraz.wytnij_twarz()
        self.obraz.zmniejsz_obraz()
        self.obraz.obroc_obraz()
        self.obraz.oznacz_twarz("Bartosz Kruszynski")


# Inicjalizacja programu
if __name__ == "__main__":
    program = Program()
    program.uruchom()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
