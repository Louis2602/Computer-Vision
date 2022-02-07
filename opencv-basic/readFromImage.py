import cv2

filepath = './img/balloon.png'

# image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filepath)

cv2.imshow("Colored Image", image)
dimensions = image.shape
print(dimensions)

# cv2.imwrite("./img/sample_gray.jpg", image) # save image

# cv2.imshow("Image", image)

cv2.waitKey()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", image_gray)
dimensions = image_gray.shape
print(dimensions)
cv2.waitKey()

cv2.destroyAllWindows()
