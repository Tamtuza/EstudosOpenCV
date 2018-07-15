import cv2
import numpy as np

imagemJogador = cv2.imread("marta.jpg")

#Exibe altura, largura e quantidade de canais de cor da imagem respectivamente
#(y,x,n)
print imagemJogador.shape

#Exibe o canal BGR (similar RGB) de um determinado pixel (y,x)
print imagemJogador.item(0,0,0), imagemJogador.item(0,0,1), imagemJogador.item(0,0,2) 

#Modifica a cor de um pixel. Nesse caso troco o pixel (0,0) para vermelho.
imagemJogador.itemset((0,0,2), 255)
imagemJogador.itemset((0,0,0), 0)
imagemJogador.itemset((0,0,1), 0)

cv2.imwrite("marta2.jpg", imagemJogador)

#Extrair informação da bola passando pixels correspondentes [yi:yf,xi:xf]
bola = imagemJogador[347:405, 500:563]
cv2.imwrite("bola.jpg", bola)

#Inserir a bola em um outro ponto da imagem passando pixels iniciais e finais
imagemJogador[334:392, 39:102] = bola
cv2.imwrite("marta3.jpg", imagemJogador)
