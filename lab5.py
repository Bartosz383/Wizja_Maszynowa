from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Ustaw backend na TkAgg

img = Image.open("D:/Repozytoria i inne takie/Wizja_Maszynowa/Wizja_Maszynowa/lab5.png")

imggauss = img.filter(ImageFilter.GaussianBlur(3))

plt.figure(1, figsize = (15, 10))
plt.subplot(131)
plt.title('Obraz przed rozmyciem')
plt.axis('off')
plt.imshow(img)
plt.subplot(132)
plt.title('Obraz po rozmyciu')
plt.axis('off')
plt.imshow(imggauss)
plt.show()
