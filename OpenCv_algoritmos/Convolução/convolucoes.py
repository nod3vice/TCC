#-*- coding:utf-8 -*-

from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

# Argumentos necessários para inicialização
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagem", required=True,
                help="Caminho até a imagem de referencia")
args = vars(ap.parse_args())

# Matriz Laplaciana
laplacian = np.array((
    [1, 1, 1],
    [1, 8, 1],
    [1, 1, 1]), dtype="int")
# Matriz Sobel X
sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")


kernelBank = (
    ("sobel_y", sobelY),
    ("sobel_x", sobelX),
    ("laplacian", laplacian)

)

# Carregamento da imagem
image = cv2.imread(args["image"])
# Conversão para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for (kernelName, kernel) in kernelBank:
    print("Aplicando {} kernel".format(kernelName))
    opencvOutput = cv2.filter2D(gray, -1, kernel)
    
    # show the output images
    cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
    cv2.imwrite('img_' + kernelName + '.jpg', opencvOutput)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
