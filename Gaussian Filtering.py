# Gaussian Filtering
# 중심에 있는 픽셀에 높은 가중치를 부여하여 계산한 값을 결과 이미지의 픽셀값으로 설정
# 이미지 내 전체적으로 밀도가 동일한 노이즈(백색노이즈)를 제거하는 데 가장 효과적

import cv2
import numpy as np

img = cv2.imread('IMAGE1.jpg')
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

# Median Filtering
blur = cv2.GaussianBlur(img,(9,9),0)

# 결과 출력
merged = np.hstack((img, blur))
cv2.imshow('Gaussian Filtering', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()