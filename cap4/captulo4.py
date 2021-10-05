import cv2

#Carregando imagem RGB e segmentando canais
imagem = cv2.imread("frutas.png")
#azul, verde, vermelho = cv2.split(imagem)
'''
#Exibindo imagens dos canais separados
cv2.imshow("Canal R", vermelho)
cv2.imshow("Canal G", verde)
cv2.imshow("Canal B", azul)

#Salvando imagens dos canais separados
cv2.imwrite("frutas-canal-vermelho.jpeg", vermelho)
cv2.imwrite("frutas-canal-verde.jpeg", verde)
cv2.imwrite("frutas-canal-azul.jpeg", azul)
'''
'''
#Combinando os 3 canais em uma única imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)
'''
#Convertendo e exibindo a imagem em tons de cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()