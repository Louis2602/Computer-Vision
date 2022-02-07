import cv2 as cv
import imutils

img = cv.imread('../img/group_people.png')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(
    gray, 1.3, 10, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print("Number of Faces found = " + str(len(faces)))

cv.imshow('Image', img)
cv.waitKey()
cv.destroyAllWindows(
