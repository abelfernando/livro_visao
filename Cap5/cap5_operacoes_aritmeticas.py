import cv2
import numpy as np
from matplotlib import pyplot as grafico
'''
imagemFichasVermelhas = cv2.imread("fichas-vermelhas.bmp")
imagemFichasPretas = cv2.imread("fichas-pretas.bmp")

#Adição
imagem = cv2.add(imagemFichasVermelhas, imagemFichasPretas)
'''
'''
#Adição p/ modificar contraste
imagemOriginal = cv2.imread("conteiners.jpg", 0)
imagemClara = cv2.add(imagemOriginal, 40)
imagemEscura = cv2.add(imagemOriginal, -40)

grafico.hist(imagemOriginal.ravel(), 256, [0, 256])

grafico.figure();
grafico.hist(imagemClara.ravel(), 256, [0, 256])

grafico.figure();
grafico.hist(imagemEscura.ravel(), 256, [0, 256])

grafico.show()
'''

#mistura
imagemFichasVermelhas = cv2.imread("fichas-vermelhas.bmp")
imagemFichasPretas = cv2.imread("fichas-pretas.bmp")

imagem = cv2.addWeighted(imagemFichasPretas, 0.2, imagemFichasVermelhas, 1.0, 0)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()