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

# b) Ustawienie kamery i inicjalizacja detektora twarzy
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if not cap.isOpened():
    print("Nie można otworzyć kamery")
    exit()

# Zatrzymanie pętli po wykryciu twarzy i zapisaniu obrazu
while True:
    ret, frame = cap.read()
    if not ret:
        print("Nie można odczytać obrazu z kamery")
        break

    # Detekcja twarzy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Rysowanie prostokątów wokół twarzy
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Kamera - twarze", frame)

    # Zapisz obraz z kamerki do pliku przy nacisnięciu "s"
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("obraz_z_kamery.jpg", frame)
        print("Zapisano obraz jako 'obraz_z_kamery.jpg'")
        break

cap.release()
cv2.destroyAllWindows()

# c) Wczytaj zapisany obraz i sprawdź jego parametry
img = cv2.imread("obraz_z_kamery.jpg")
print("Parametry obrazu:", img.shape)

# d) Wyświetl obraz
cv2.imshow("Wczytany obraz", img)
cv2.waitKey(0)

# e) Podejrzyj zawartość dowolnego piksela (np. 50, 50)
print("Kolor piksela (50, 50):", img[50, 50])

# f) Wytnij z obrazu jedną z twarzy (jeśli wykryto)
faces = face_cascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.1, 4)
if len(faces) > 0:
    (x, y, w, h) = faces[0]
    face_crop = img[y:y + h, x:x + w]
    cv2.imshow("Wycięta twarz", face_crop)
    cv2.imwrite("wycieta_twarz.jpg", face_crop)
    print("Wycięto twarz i zapisano jako 'wycieta_twarz.jpg'")
else:
    print("Nie znaleziono twarzy do wycięcia")

# g) Zmniejszenie obrazu o 50% z zachowaniem proporcji
new_x, new_y = int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)
resized_img = cv2.resize(img, (new_x, new_y))
cv2.imshow("Zmniejszony obraz", resized_img)

# h) Obróć pierwotny obraz o 30 stopni przeciwnie do ruchu wskazówek zegara
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=30, scale=1)

# i) Rozwiązanie problemu wychodzenia poza krawędzie: rozszerzenie rozmiaru wyjściowego obrazu
cos = np.abs(rotate_matrix[0, 0])
sin = np.abs(rotate_matrix[0, 1])
new_w = int((h * sin) + (w * cos))
new_h = int((h * cos) + (w * sin))
rotate_matrix[0, 2] += (new_w / 2) - center[0]
rotate_matrix[1, 2] += (new_h / 2) - center[1]

rotated_img = cv2.warpAffine(img, rotate_matrix, (new_w, new_h))
cv2.imshow("Obrócony obraz", rotated_img)

# j) Oznaczenie twarzy czerwonym prostokątem i podpisanie imieniem
if len(faces) > 0:
    (x, y, w, h) = faces[0]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(img, "Bartosz Kruszynski", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Oznaczona twarz", img)

# k) Zapisz obrócony obraz do pliku
cv2.imwrite("obrocony_obraz.jpg", rotated_img)
print("Obrócony obraz zapisano jako 'obrocony_obraz.jpg'")

cv2.waitKey(0)
cv2.destroyAllWindows()
