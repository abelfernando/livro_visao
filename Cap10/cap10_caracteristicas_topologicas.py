import cv2
import numpy as np
'''
#Número de vértices
imagemRGB = cv2.imread("puzzle.bmp")
imagemTonsDeCinza = cv2.imread("puzzle.bmp", 0
                               )
tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagemTonsDeCinza, 127, 255, tipo)

#Obtendo os contornos dos objetos na imagem
modo = cv2.RETR_TREE
metodo = cv2.CHAIN_APPROX_SIMPLE;
contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)

#Obtendo os ocntornosdo primeiro objeto segmentado
objeto = contornos[0]

#Obtendo a elipse
ellipse = cv2.fitEllipse(objeto)

#Desenhando a elipse na imagem RGB
cv2.ellipse(imagemRGB, ellipse, (0,255,0), 2)

cv2.imshow("Elipse Ajustada", imagemRGB)

#Obtendo o perímetro do objeto
perimetro = cv2.arcLength(objeto, True)

#Obtendo os pontos referentes aos vértices
poligono = cv2.approxPolyDP(objeto, 0.1 * perimetro, True)

#Obtendo o total de vértices
totalVertices = len(poligono)

print(totalVertices)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Número de furos
#Carrega a imagem do objeto com dois furos
imagem = cv2.imread("circulo-perfurado-3.bmp", 0)

tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagem, 127, 255, tipo)
modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;
contornos, hierarquia = cv2.findContours(imgBinarizada, modo,metodo)

#obtém o total de contornos e subtrai um
furos = len(contornos) - 1
#cv2.imshow("Imagem Binarizada", imgBinarizada)
print(furos)

cv2.waitKey(0)
cv2.destroyAllWindows()