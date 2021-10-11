import cv2

'''
#Operador Sobel
imagem = cv2.imread("estacionamento.jpg", 0)

sobelx = cv2.Sobel(imagem, cv2.CV_8U, 1, 0, ksize = 3)
sobely = cv2.Sobel(imagem, cv2.CV_8U, 0, 1, ksize = 3)

cv2.imshow("Original", imagem)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Operador Laplaciano
imgOriginal = cv2.imread("estacionamento.jpg", 0)
imgTratada = cv2.Laplacian(imgOriginal, cv2.CV_8U)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Aguçamento de Bordas
imgOriginal = cv2.imread("lua.jpg", 0)
imgFiltrada = cv2.Laplacian(imgOriginal, cv2.CV_8U)
imgRealcada = cv2.subtract(imgOriginal, imgFiltrada)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Filtrada", imgFiltrada)
cv2.imshow("Realçada", imgRealcada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
#Máscara de desaguçamento
imgOriginal = cv2.imread("radiografia.jpg", 0)
imgSuavizada = cv2.GaussianBlur(imgOriginal, (13, 13), 3)
imgDetalhes = 3 * cv2.subtract(imgOriginal, imgSuavizada)
imgRealcada = cv2.add(imgOriginal, imgDetalhes)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgSuavizada)
cv2.imshow("Bordas", imgDetalhes)
cv2.imshow("Realcada", imgRealcada)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#Detector de bordas de Canny
imgOriginal = cv2.imread("estacionamento.jpg", 0)
imgTratada = cv2.Canny(imgOriginal, 100, 200)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()