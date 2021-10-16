import cv2
import numpy as np
'''
#Binarização
imgOriginal = cv2.imread("graos-de-cafe.jpg", 0)

metodo = cv2.THRESH_BINARY_INV
ret, imgBinarizada = cv2.threshold(imgOriginal, 135, 255, metodo)

cv2.imshow("Imagem Original", imgOriginal)
cv2.imshow("Imagem Tratada", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Binarização adaptativa
imgOriginal = cv2.imread("comprimidos.jpg", 0)
imgTratada = cv2.medianBlur(imgOriginal, 7)

imgBinarizada = cv2.adaptiveThreshold(imgTratada, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 11, 5)

cv2.imshow("Imagem Original", imgOriginal)
cv2.imshow("Imagem Tratada", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Binarização de Nobuyuki Otsu
imgOriginal = cv2.imread("graos-de-cafe.jpg", 0)

tipo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
limiar, imgBinarizada = cv2.threshold(imgOriginal, 0, 255, tipo)

print(limiar)

cv2.imshow("Imagem Original", imgOriginal)
cv2.imshow("Imagem Tratada", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()