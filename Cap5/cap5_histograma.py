#Histogrma imagem binária
'''import cv2

imagem = cv2.imread("folha-binaria.bmp", 0)
totalPixelsPreto = 0
totalPixelsBranco = 0

for x in range(0, 499):
    for y in range (0, 499):
        if imagem[x,y] == 255:
            totalPixelsBranco += 1;
        else:
            totalPixelsPreto += 1;

print(totalPixelsBranco)
print(totalPixelsPreto)

import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagem = cv2.imread("folha-binaria.bmp", 0)
grafico.hist(imagem.ravel(), 256, [0, 256])
grafico.show()'''

#Histograma em uma imagem e mtons de cinza
'''import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagem = cv2.imread("folha-tonsCinza.bmp", 0)
grafico.hist(imagem.ravel(), 256, [0, 256])
grafico.show()'''

#Histograma em uma imagem colcorida
'''import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagem = cv2.imread("folha-colorida.bmp")
azul, verde, vermelho = cv2.split(imagem)

grafico.hist(azul.ravel(), 256, [0, 256])

grafico.figure();
grafico.hist(verde.ravel(), 256, [0, 256])

grafico.figure();
grafico.hist(vermelho.ravel(), 256, [0, 256])

grafico.show()'''

#Equalização do histograma
import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread("maquina.jpg", 0)
imagemEqualizada = cv2.equalizeHist(imagemOriginal)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Equalizada", imagemEqualizada)

grafico.hist(imagemOriginal.ravel(), 256, [0, 256])

grafico.figure();
grafico.hist(imagemEqualizada.ravel(), 256, [0, 256])

grafico.show()