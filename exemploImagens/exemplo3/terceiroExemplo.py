import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("frida.jpg", 0)

#Ploto o histograma da imagem
#Ravel transforma a imagem (matriz 2D) em um vetor de uma dimensão
#256 é a representação do tom de cor no ponto x (bins)
#[0, 256] de que ponto em x até que ponto em x vou representar (intervalo do histograma)
plt.hist(img.ravel(), 256, [0, 256])

#Mostra na tela a imagem e o histograma
cv2.imshow("Imagem Original", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
