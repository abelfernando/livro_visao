##Carregando imagens a partir de arquivos
'''import cv2

imagem = cv2.imread("imagem.jpg")
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

##Carregando imagens a partir de vídeos
'''import cv2

captura = cv2.VideoCapture("video.mov")

while True:
    ret, frame = captura.read()
    cv2.imshow("Imagem", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

captura.release()
cv2.destroyAllWindows()'''

##Capturando imagens a partit de uma webcam
import cv2

captura = cv2.VideoCapture(0)

while True:
    ret, frame = captura.read()
    cv2.imshow("Imagem", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

captura.release()
cv2.destroyAllWindows()