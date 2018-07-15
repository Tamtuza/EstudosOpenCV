import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("alanis.jpg")

#Cria uma lista contendo os canais de cores para construir
#o histograma dos três canais
color = ('b', 'g', 'r')

#Itera entre os canais BGR
for i, col in enumerate(color):
    
    #print (i, col)

    #Gera o histograma usando: a imagem, o identificador do canal,
    #a máscara (caso queira calcular apenas uma região), o bin e o intervalo
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])

    #Constrói o histograma para o canal de cor específico
    plt.plot(histr, color = col)

    #Define os limites do histograma em relação a x (igual ao intervalo acima)
    plt.xlim([0, 256])

cv2.imshow("ImagemOriginal", img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
