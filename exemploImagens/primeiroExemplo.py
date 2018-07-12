import cv2

#Fun��o 1: recebe nome do arquivo do arquivo de imagem e 1 = cor ou 0 = p&b
imagemCarregada = cv2.imread("exemplo.jpg", 0)

#Fun��o 2: recebe o t�tulo da janela e a vari�vel contendo a imagem
cv2.imshow("ImagemCarregada", imagemCarregada)

#Fun��o 3: espera usu�rio digitar algo e recebe tempo em milisegundos
cv2.waitKey(0)

#Fun��o 4: encerra a aplica��o fechando todas as janelas criadas
cv2.destroyAllWindows()

#Fun��o 5: salva uma imagem e recebe o nome a ser salvo e vari�vel contendo imagem
cv2.imwrite("imagemSalva.jpg", imagemCarregada)
