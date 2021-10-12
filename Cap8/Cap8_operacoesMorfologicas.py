import cv2
import numpy as np
'''
#Operação de erosão
imagemOriginal = cv2.imread("rolamento.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
imagemProcessada = cv2.erode(imagemOriginal, elementoEstruturante, iterations = 2)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Operação de dilatação
imagemOriginal = cv2.imread("rolamento.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
imagemProcessada = cv2.dilate(imagemOriginal, elementoEstruturante, iterations = 2)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Operação de abertura
imagemOriginal = cv2.imread("rolamento-ruido-externo.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_OPEN, elementoEstruturante)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Operação de fechamento
imagemOriginal = cv2.imread("rolamento-ruido-interno.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_CLOSE, elementoEstruturante)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Abertura e fechamento em tons de cinza
imagemOriginal = cv2.imread("arroz.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_CROSS, (100,100))
imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_OPEN, elementoEstruturante)

imagemSubtraida = cv2.subtract(imagemOriginal, imagemProcessada)

#Ajusta o contraste da imagem
imagemTratada = cv2.add(imagemSubtraida, imagemSubtraida)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)
cv2.imshow("Subtraida", imagemSubtraida)
cv2.imshow("Tratada", imagemTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Gradiente Morfológico
imagemOriginal = cv2.imread("rolamento.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_GRADIENT, elementoEstruturante)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Top Hat
imagemOriginal = cv2.imread("arroz.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_TOPHAT, elementoEstruturante)

#Ajuste de contraste
imagemTratada = cv2.add(imagemProcessada, imagemProcessada)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)
cv2.imshow("Final", imagemTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Remoção de ruído
imagemOriginal = cv2.imread("engrenagem-binaria.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
imagemProcessada = cv2.erode(imagemOriginal, elementoEstruturante, iterations = 1)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()