# Canny algorithm

import cv2
filepath = './img/balloon.png'
gray_img = cv2.imread(filepath, 0)
cv2.imshow('Original Image', gray_img)
cv2.waitKey()

edges = cv2.Canny(gray_img, threshold1=100, threshold2=200)
cv2.imshow('Image with edges', edges)

cv2.waitKey()
cv2.destroyAllWindows()
