import cv2
import imutils

filepath = './img/balloon.png'

image = cv2.imread(filepath)

cv2.imshow("Original Image", image)
cv2.waitKey()

image_rotate = imutils.rotate(image, 45)  # Nguoc chieu kim dong ho
cv2.imshow("Resized Image", image_rotate)
cv2.waitKey()

cv2.destroyAllWindows()
