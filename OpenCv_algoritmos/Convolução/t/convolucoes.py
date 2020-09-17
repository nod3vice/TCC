#-*- coding:utf-8 -*-

from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to the input image")
args = vars(ap.parse_args())

# construct the Laplacian kernel used to detect edge-li
# regions of an image
laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")
# construct the Sobel x-axis kernel
sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")
# construct the Sobel y-axis kernel
sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

# construct the kernel bank, a list of kernels we're going
# to apply using both our custom `convole` function and
# OpenCV's `filter2D` function
kernelBank = (
    ("sobel_y", sobelY),
    ("sobel_x", sobelX),
    ("laplacian", laplacian)

)

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# loop over the kernels
for (kernelName, kernel) in kernelBank:
    # apply the kernel to the grayscale image using OpenCV's `filter2D`
    print("[INFO] applying {} kernel".format(kernelName))
    opencvOutput = cv2.filter2D(gray, -1, kernel)
    
    # show the output images
    cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
    cv2.imwrite('img_' + kernelName + '.jpg', opencvOutput)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
