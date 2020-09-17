#!/usr/bin/python

import cv2
import numpy as np
from matplotlib import pyplot as plt
from sys import argv

# cor usada para pintar
#pintado = 5

# carregar imagem na escala cinza
def carregar_imagem(caminho):
    return cv2.imread(caminho, 0);

# pausa execucao para mostrar as imagens
def bloquear_execucao():
    cv2.waitKey();
    cv2.destroyAllWindows();

# mostra imagem na tela
def mostrar_imagem(nome, img):
    cv2.imshow(nome, img);


if __name__ == '__main__': 
    if (len(argv) == 1):
        print ('Passe o caminho da imagem a ser carregada.');
        exit(1);

    

    caminho_arquivo = argv[1];
    img = carregar_imagem(caminho_arquivo);
    
    ret, imgT = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  #  mostrar_imagem('original-binaria', imgT);
    

    mostrar_imagem('original-tons-cinza', img);
    mostrar_imagem('pintada', imgT);

    n,bins,patches = plt.hist(imgT.ravel(), 256, [1, 255])
    plt.show()

    bloquear_execucao();
