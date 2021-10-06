import cv2
import numpy as np
'''
#Rotação
imagemOriginal = cv2.imread("folha.jpg", 0)
totalLinhas, totalColunas = imagemOriginal.shape

matriz = cv2.getRotationMatrix2D((totalColunas/2, totalLinhas/2), 90, 1)

imagemRotacionada = cv2.warpAffine(imagemOriginal, matriz, (totalColunas, totalLinhas))

cv2.imshow("Resultado", imagemRotacionada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Translação
imagemOriginal = cv2.imread("folha.jpg")
totalLinhas, totalColunas = imagemOriginal.shape[:2]

matriz = np.float32([[1, 0, 100], [0, 1, 100]])

imagemDeslocada = cv2.warpAffine(imagemOriginal, matriz, (totalColunas, totalLinhas))

cv2.imshow("Resultado", imagemDeslocada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Ajuste de escala
imagemOriginal = cv2.imread("folha.jpg")

imagemModificada = cv2.resize(imagemOriginal, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

cv2.imshow("Resultado", imagemModificada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
imagemOriginal = cv2.imread("sudoku.jpg")

pontosIniciais = np.float32([[189, 87], [459, 84], [192, 373], [484, 372]])
pontosFinais = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])

matriz = cv2.getPerspectiveTransform(pontosIniciais, pontosFinais)
imgagemModificada = cv2.warpPerspective(imagemOriginal, matriz, (500, 500))

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Modificada", imgagemModificada)
cv2.waitKey(0)
cv2.destroyAllWindows()