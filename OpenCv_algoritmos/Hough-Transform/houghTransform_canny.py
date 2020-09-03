# import libraries we'll need
import cv2
import numpy as np

# read in your image
img = cv2.imread('img_canny.jpg')

# convert to grayscale so we can detect edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# use Canny edge detector to find edges in the image.  The thresholds determine how
# weak or strong an edge will be detected.  These can be tweaked.
lower_threshold = 80
upper_threshold = 200

edges = cv2.Canny(gray, lower_threshold, upper_threshold)

# detect lines in the image.  This is where the real work is done.  Higher threshold
# means a line needs to be stronger to be detected, so again, this can be tweaked.
threshold = 300
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold, minLineLength=160, maxLineGap=1)

for line in lines:
   x1, y1, x2, y2 = line[0]
   cv2.line(img, (x1 + 2000, y1), (x2 - 5000, y2), (255, 0, 0), 1)

cv2.imwrite('linesDetected_Canny.jpg', img)

