# Median Filtering
# 커널 내의 픽셀을 크기순으로 정렬한 후 중간값을 픽셀값으로 설정
# 무작위 노이즈를 제거하는데 효과적
# 에지가 있는 이미지의 경우 결과 이미지에서 에지가 사라질 수 있음

import cv2
import numpy as np

img = cv2.imread('IMAGE1.jpg')
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

# Median Filtering
median = cv2.medianBlur(img, 9)

# 결과 출력
merged = np.hstack((img, median))
cv2.imshow('Median Filtering', median)
cv2.waitKey(0)
cv2.destroyAllWindows()