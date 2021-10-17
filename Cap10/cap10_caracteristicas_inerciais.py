import cv2
import numpy as np
'''
#momento
imagem = cv2.imread("quadrado.bmp", 0)
momentos = cv2.moments(imagem)

print(momentos)
'''
'''
#Momentos invariantes de Hu
imagem = cv2.imread("engrenagem-3.bmp", 0)
momentos = cv2.moments(imagem)
momentosDeHu = cv2.HuMoments(momentos)

print (momentosDeHu)

#Aplicando a transformação logaritmica
print(-np.sign(momentosDeHu) * np.log10(np.abs(momentosDeHu)))
'''
'''
#Centro geométrico
imagem = cv2.imread("quadrado.bmp", 0)
momentos = cv2.moments(imagem)

cx = int(momentos['m10']/momentos['m00'])
cy = int(momentos['m01']/momentos['m00'])

print(cx, cy)
'''
'''
#Retangulo Envolvente
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

#Obtendo os vértices do retangulo
x, y, w, h = cv2.boundingRect(objeto)

#Desenhando o retângulo na imagem RGB
cv2.rectangle(imagemRGB, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow("Retangulo Envolvente", imagemRGB)
print(x, y, w, h)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Circunferência envolvente
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

#Obtendo o ponto central e o raio da circunferência
(x, y), raio = cv2.minEnclosingCircle(objeto)

centro = (int(x), int(y))
raio = int(raio)

#Desenhando a circunferência na imagem RGB
cv2.circle(imagemRGB, centro, raio, (0,255,0), 2)

cv2.imshow("Cirrcunferência Envolvente", imagemRGB)
print(x, y, raio)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Elipse Ajustada
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
print(ellipse)

cv2.waitKey(0)
cv2.destroyAllWindows()