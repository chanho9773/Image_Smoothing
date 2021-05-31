# Average Filtering
# 모든 필터에 똑같은 가중치를 부여하여 이웃 픽셀의 평균을 결과 이미지의 픽셀값으로 설정

import cv2
import numpy as np

img = cv2.imread('IMAGE1.jpg')
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

# Average Filtering
blur = cv2.blur(img, (9,9))

# 결과 출력
merged = np.hstack((img, blur))
cv2.imshow('Average Filtering', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()