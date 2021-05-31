import cv2
import numpy as np

src = cv2.imread('IMAGE1.jpg', cv2.IMREAD_COLOR)
src = cv2.pyrDown(src)
src = cv2.pyrDown(src)

dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bin = cv2.threshold(dst, 100, 255, cv2.THRESH_BINARY)

#merged1 = np.hstack([src, dst])
#merged2 = np.hstack([src, bin])

cv2.imshow('Original', src)
cv2.imshow('Grayscale', dst)
cv2.imshow('Binary', bin)
cv2.waitKey(0)
cv2.destroyAllWindows()