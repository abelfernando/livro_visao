import cv2

'''
#Filtro de média
imgOriginal=cv2.imread("moedas.jpg")
imgTratada = cv2.blur(imgOriginal, (5,5))

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Filtro Gaussiano
imgOriginal=cv2.imread("moedas.jpg")
imgTratada = cv2.GaussianBlur(imgOriginal, (5,5), 0)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Filtro de mediana
imgOriginal=cv2.imread("radioatividade.jpg")
imgTratada = cv2.medianBlur(imgOriginal, 15)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#Filtro Bilateral
imgOriginal=cv2.imread("estacionamento.jpg")
imgTratada = cv2.bilateralFilter(imgOriginal, 9, 75, 75)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()