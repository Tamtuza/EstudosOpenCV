import cv2

#Função 1: recebe nome do arquivo do arquivo de imagem e 1 = cor ou 0 = p&b
imagemCarregada = cv2.imread("exemplo.jpg", 0)

#Função 2: recebe o título da janela e a variável contendo a imagem
cv2.imshow("ImagemCarregada", imagemCarregada)

#Função 3: espera usuário digitar algo e recebe tempo em milisegundos
cv2.waitKey(0)

#Função 4: encerra a aplicação fechando todas as janelas criadas
cv2.destroyAllWindows()

#Função 5: salva uma imagem e recebe o nome a ser salvo e variável contendo imagem
cv2.imwrite("imagemSalva.jpg", imagemCarregada)
