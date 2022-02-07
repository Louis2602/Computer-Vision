import cv2

img = cv2.imread('./img/balloon.png')
cv2.imshow("Original image", img)
cv2.waitKey()
# ksize must be an odd number
# the bigger of ksize, the more blur img get
blur = cv2.GaussianBlur(img, ksize=(31, 31), sigmaX=0)
cv2.imshow("Blur image", blur)
cv2.waitKey()

cv2.destroyAllWindows()
