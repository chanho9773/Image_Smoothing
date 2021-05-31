# Bilateral Filtering
#경계선을 유지하면서 Gaussian Filter처리를 해 주는 방법
#필터의 처리속도가 비교적으로 느리다

import cv2
import numpy as np

img = cv2.imread('IMAGE1.jpg')
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

# Median Filtering
blur = cv2.bilateralFilter(img,9,75,75)

# 결과 출력
merged = np.hstack((img, blur))
cv2.imshow('Bilateral Filtering', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()