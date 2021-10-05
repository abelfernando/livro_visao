'''import cv2
imagem =cv2.imread("frutas.png")
valorPixel = imagem[150, 150]
print(valorPixel)'''

'''import cv2
imagem =cv2.imread("frutas.png")
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
valorPixel = imagem[150, 150]
print(valorPixel)'''

'''import cv2
imagem =cv2.imread("frutas.png")
valorPixel = imagem[150, 150, 0]
print(valorPixel)'''

import cv2
imagem =cv2.imread("frutas.png")
imagem[150, 150] = [255, 255, 255]
print(imagem[150, 150])