# import libraries we'll need
import cv2
import numpy as np

# read in your image
img = cv2.imread('img_laplacian.jpg')

# convert to grayscale so we can detect edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# use Canny edge detector to find edges in the image.  The thresholds determine how
# weak or strong an edge will be detected.  These can be tweaked.
lower_threshold = 112
upper_threshold = 215
edges = cv2.Canny(gray, lower_threshold, upper_threshold)

# detect lines in the image.  This is where the real work is done.  Higher threshold
# means a line needs to be stronger to be detected, so again, this can be tweaked.
threshold = 257
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold)

# convert each line to coordinates back in the original image
for line in lines:
    for rho, theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * -b)
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 5000 * -b)
        y2 = int(y0 - 1000 * a)

        # draw each line on the image
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

# write the image to disk
cv2.imwrite('houghlines.jpg', img)
