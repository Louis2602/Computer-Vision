# Contours là tập hợp các điểm liên tục tạo thành 1 đường cong (curve)(boundary)
# và không có khoảng hở trong đường cong đó

# Trong opencv, việc tìm 1 contour là đi tìm một đối tượng có màu trắng trên nền đen

import cv2

filepath = './img/balloon.png'
img = cv2.imread(filepath)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh_binary = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(
    thresh_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow('Image with contours', img)
cv2.waitKey()
cv2.destroyAllWindows()
