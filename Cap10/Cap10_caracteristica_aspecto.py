import cv2
import statistics

#Cor binaria

imgBinaria = cv2.imread("tampa-binaria.bmp", 0)
imgTonsDeCinza = cv2.imread("tampa-tons-de-cinza.jpg", 0)

rolBinaria = imgBinaria.ravel()
rolTonsDeCinza = imgTonsDeCinza.ravel()

print(statistics.mode(rolBinaria))
print(statistics.mode(rolTonsDeCinza))

#Cor RGB

imgRGB = cv2.imread("tampa-rgb.jpg")
imgTonsDeCinza = cv2.imread("tampa-tons-de-cinza.jpg", 0)

valorMedioRGB = cv2.mean(imgRGB)
valorMedioCinza = cv2.mean(imgTonsDeCinza)

print(valorMedioRGB)
print(valorMedioCinza)