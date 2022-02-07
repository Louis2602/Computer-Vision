import cv2
import matplotlib.pyplot as plt

filepath = './img/sudoku.jpg'
# Using 0 to read image in grayscale mode
img = cv2.imread(filepath, 0)
ret, thresh_binary_1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Apply adaptive threshold
thresh_binary_2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh_binary_3 = cv2.adaptivethreshold(img, 255, cv2.adaptive_thresh_gaussian_c,
                                        cv2.thresh_binary, 11, 2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, thresh_binary_1, thresh_binary_2, thresh_binary_3]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
