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
'''
'''
#Segmentação por Cor
imgRGB = cv2.imread("cubo-magico.jpg")
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

tomClaro = np.array([160, 100, 100])
tomEscuro = np.array([200, 255, 255])

imgSegmentada = cv2.inRange(imgHSV, tomClaro, tomEscuro)

cv2.imshow("Original", imgRGB)
cv2.imshow("Segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Segmentação por bordas
imgOriginal = cv2.imread("graos-de-cafe.jpg", 0)

metodo = cv2.THRESH_BINARY_INV
ret, imgBinarizada = cv2.threshold(imgOriginal, 135, 255, metodo)

e = np.ones((3, 3), np.uint8)
imgTratada = cv2.morphologyEx(imgBinarizada, cv2.MORPH_CLOSE, e)
imgTratada = cv2.erode(imgTratada, e, iterations = 2)

imgSegmentada = cv2.Canny(imgTratada, 100, 200)

cv2.imshow("Binarizada", imgBinarizada)
cv2.imshow("Tratada", imgTratada)
cv2.imshow("Segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Segmentação por movimento
cap1 = cv2.imread("captura-1.jpg")
cap2 = cv2.imread("captura-2.jpg")

imgRGB = cv2.subtract(cap1, cap2)
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)

tomClaro = np.array([0, 120, 120])
tomEscuro = np.array([180, 255, 255])

imgSegmentada = cv2.inRange(imgHSV, tomClaro, tomEscuro)
cv2.imshow("segmentada", imgSegmentada)

cv2.waitKey(0)
cv2.destroyAllWindows()