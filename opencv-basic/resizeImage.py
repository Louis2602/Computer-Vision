import cv2

filepath = './img/balloon.png'

image = cv2.imread(filepath)

cv2.imshow("Original Image", image)
cv2.waitKey()

# image_resize = cv2.resize(image, dsize=(800,600)) # resize absolute with actual values
image_resize = cv2.resize(image, dsize=None, fx=0.5,
                          fy=0.5)  # resize relative with ratio
cv2.imshow("Resized Image", image_resize)
cv2.waitKey()

cv2.destroyAllWindows()
