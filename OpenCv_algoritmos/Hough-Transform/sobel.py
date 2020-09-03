
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img_laplacian.jpg', cv2.IMREAD_GRAYSCALE)
sobel = cv2.Sobel(img, cv2.CV_32F, 1, 0)

cst = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

lines = cv2.HoughLinesP(sobel,1,np.pi/180,100,100,30)
for line in lines:    
    for x1,y1,x2,y2 in line:
         cv2.line(cst,(x1 + 1000,y1),(x2 - 5000,y2),(0,255,0),1)

cv2.imwrite('linesDetected_laplacian.jpg',cst)