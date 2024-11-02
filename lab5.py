# from PIL import Image, ImageFilter
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg')  # Ustaw backend na TkAgg
#
# img = Image.open("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/lab5.png")
#
# imggauss = img.filter(ImageFilter.GaussianBlur(3))
#
# plt.figure(1, figsize = (15, 10))
# plt.subplot(131)
# plt.title('Obraz przed rozmyciem')
# plt.axis('off')
# plt.imshow(img)
# plt.subplot(132)
# plt.title('Obraz po rozmyciu')
# plt.axis('off')
# plt.imshow(imggauss)
# plt.show()

# from PIL import Image, ImageFilter
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
#
# # Ustawienie backendu dla Matplotlib
# matplotlib.use('TkAgg')
#
# # Wczytanie i konwersja obrazu na skalę szarości
# img = Image.open("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/lab5.png").convert('L')
#
# # Zastosowanie rozmycia Gaussa
# imggauss = img.filter(ImageFilter.GaussianBlur(3))
#
# # Wyświetlenie obrazu przed i po rozmyciu
# plt.figure(figsize=(15, 10))
# plt.subplot(131)
# plt.title('Obraz przed rozmyciem')
# plt.axis('off')
# plt.imshow(img, cmap='gray')  # Dodano cmap='gray' dla poprawnej skali szarości
# plt.subplot(132)
# plt.title('Obraz po rozmyciu')
# plt.axis('off')
# plt.imshow(imggauss, cmap='gray')
# plt.show()
#
# # Konwersja obrazu do tablicy NumPy
# imgArray = np.asarray(img)
#
# # Progowanie obrazu przy różnych wartościach progowych
# _, imgThresholded1 = cv2.threshold(imgArray, 64, 255, cv2.THRESH_BINARY)
# _, imgThresholded2 = cv2.threshold(imgArray, 127, 255, cv2.THRESH_BINARY)
# _, imgThresholded3 = cv2.threshold(imgArray, 191, 255, cv2.THRESH_BINARY)
#
# # Wyświetlenie obrazów po progowaniu
# plt.figure(figsize=(15, 10))
# plt.subplot(131)
# plt.title('Próg 64')
# plt.axis('off')
# plt.imshow(imgThresholded1, cmap='gray')
# plt.subplot(132)
# plt.title('Próg 127')
# plt.axis('off')
# plt.imshow(imgThresholded2, cmap='gray')
# plt.subplot(133)
# plt.title('Próg 191')
# plt.axis('off')
# plt.imshow(imgThresholded3, cmap='gray')
# plt.show()

# from PIL import Image, ImageFilter
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
# from PIL import Image
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Ustawienie backendu dla Matplotlib
# matplotlib.use('TkAgg')
#
# # Wczytanie i konwersja obrazu na skalę szarości
# img = Image.open("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/lab5.png").convert('L')
#
# # Zastosowanie rozmycia Gaussa
# imggauss = img.filter(ImageFilter.GaussianBlur(3))
#
# # Wyświetlenie obrazu przed i po rozmyciu
# plt.figure(figsize=(15, 10))
# plt.subplot(131)
# plt.title('Obraz przed rozmyciem')
# plt.axis('off')
# plt.imshow(img, cmap='gray')  # Dodano cmap='gray' dla poprawnej skali szarości
# plt.subplot(132)
# plt.title('Obraz po rozmyciu')
# plt.axis('off')
# plt.imshow(imggauss, cmap='gray')
# plt.show()
#
# # Konwersja obrazu do tablicy NumPy
# imgArray = np.asarray(img)
#
# # Progowanie obrazu przy różnych wartościach progowych
# _, imgThresholded1 = cv2.threshold(imgArray, 64, 255, cv2.THRESH_BINARY)
# _, imgThresholded2 = cv2.threshold(imgArray, 127, 255, cv2.THRESH_BINARY)
# _, imgThresholded3 = cv2.threshold(imgArray, 191, 255, cv2.THRESH_BINARY)
#
# # Wyświetlenie obrazów po progowaniu
# plt.figure(figsize=(15, 10))
# plt.subplot(131)
# plt.title('Próg 64')
# plt.axis('off')
# plt.imshow(imgThresholded1, cmap='gray')
# plt.subplot(132)
# plt.title('Próg 127')
# plt.axis('off')
# plt.imshow(imgThresholded2, cmap='gray')
# plt.subplot(133)
# plt.title('Próg 191')
# plt.axis('off')
# plt.imshow(imgThresholded3, cmap='gray')
# plt.show()
# imgArray = np.asarray(img)
# retOtsu, imgThresholdedOtsu = cv2.threshold(imgArray, 0, 255,
# cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# plt.figure(1, figsize = (5, 5))
# plt.imshow(imgThresholdedOtsu, cmap = 'gray')
# plt.title('Metoda Otsu')
# plt.axis('off')
# plt.show()

# from PIL import Image, ImageFilter
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib
#
# # Ustawienie backendu dla Matplotlib
# matplotlib.use('TkAgg')
#
# # Wczytanie i konwersja obrazu na skalę szarości
# img = Image.open("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/lab5.png").convert('L')
#
# # Zastosowanie rozmycia Gaussa
# imggauss = img.filter(ImageFilter.GaussianBlur(3))
#
# # Wyświetlenie obrazu przed i po rozmyciu
# plt.figure(figsize=(15, 10))
# plt.subplot(131)
# plt.title('Obraz przed rozmyciem')
# plt.axis('off')
# plt.imshow(img, cmap='gray')
# plt.subplot(132)
# plt.title('Obraz po rozmyciu')
# plt.axis('off')
# plt.imshow(imggauss, cmap='gray')
# plt.show()
#
# # Konwersja obrazu do tablicy NumPy
# imgArray = np.asarray(img)
#
# # Progowanie obrazu przy różnych wartościach progowych
# _, imgThresholded1 = cv2.threshold(imgArray, 64, 255, cv2.THRESH_BINARY)
# _, imgThresholded2 = cv2.threshold(imgArray, 127, 255, cv2.THRESH_BINARY)
# _, imgThresholded3 = cv2.threshold(imgArray, 191, 255, cv2.THRESH_BINARY)
#
# # Wyświetlenie obrazów po progowaniu
# plt.figure(figsize=(15, 10))
# plt.subplot(131)
# plt.title('Próg 64')
# plt.axis('off')
# plt.imshow(imgThresholded1, cmap='gray')
# plt.subplot(132)
# plt.title('Próg 127')
# plt.axis('off')
# plt.imshow(imgThresholded2, cmap='gray')
# plt.subplot(133)
# plt.title('Próg 191')
# plt.axis('off')
# plt.imshow(imgThresholded3, cmap='gray')
# plt.show()
#
# # Metoda Otsu
# _, imgThresholdedOtsu = cv2.threshold(imgArray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# plt.figure(figsize=(5, 5))
# plt.imshow(imgThresholdedOtsu, cmap='gray')
# plt.title('Metoda Otsu')
# plt.axis('off')
# plt.show()
#
# # Operacje morfologiczne
# kernel = np.ones((5, 5), np.uint8)
# imgErosion = cv2.erode(imgThresholdedOtsu, kernel, iterations=1)
# imgDilation = cv2.dilate(imgThresholdedOtsu, kernel, iterations=1)
# imgOpening = cv2.morphologyEx(imgThresholdedOtsu, cv2.MORPH_OPEN, kernel)
# imgClosing = cv2.morphologyEx(imgThresholdedOtsu, cv2.MORPH_CLOSE, kernel)
#
# # Wyświetlenie wyników operacji morfologicznych
# plt.figure(figsize=(15, 10))
# plt.subplot(231)
# plt.imshow(imgErosion, cmap='gray')
# plt.title('Erozja')
# plt.axis('off')
# plt.subplot(232)
# plt.imshow(imgDilation, cmap='gray')
# plt.title('Dylatacja')
# plt.axis('off')
# plt.subplot(233)
# plt.imshow(imgOpening, cmap='gray')
# plt.title('Otwarcie')
# plt.axis('off')
# plt.subplot(234)
# plt.imshow(imgClosing, cmap='gray')
# plt.title('Domknięcie')
# plt.axis('off')
# plt.show()

import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# Ustawienie backendu dla Matplotlib
matplotlib.use('TkAgg')

# Wczytaj obrazy
img1 = cv2.imread("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/lab51.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/lab52.png", cv2.IMREAD_GRAYSCALE)

# Funkcja do wyświetlania wyników filtrów
def show_images(images, titles):
    plt.figure(figsize=(20, 10))
    for i in range(len(images)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

# Filtr Gaussa z mniejszym jądrem - delikatniejsze wygładzenie szumu
gauss1 = cv2.GaussianBlur(img1, (3, 3), 0)  # mniejsze jądro
gauss2 = cv2.GaussianBlur(img2, (3, 3), 0)  # mniejsze jądro

# Filtr medianowy z mniejszym jądrem - usunięcie drobnych zakłóceń punktowych
median1 = cv2.medianBlur(gauss1, 3)  # mniejsze jądro
median2 = cv2.medianBlur(gauss2, 3)  # mniejsze jądro

# Prógowanie Otsu - wyodrębnienie tekstu
_, thresh1 = cv2.threshold(median1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, thresh2 = cv2.threshold(median2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Wyświetlenie wyników
show_images([img1, gauss1, median1, thresh1], ["LAB51 - Oryginał", "Gauss (mniejsze jądro)", "Medianowy (mniejsze jądro)", "Próg Otsu"])
show_images([img2, gauss2, median2, thresh2], ["LAB52 - Oryginał", "Gauss (mniejsze jądro)", "Medianowy (mniejsze jądro)", "Próg Otsu"])
