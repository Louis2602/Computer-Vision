import enum
import cv2
import imutils
from imutils.perspective import four_point_transform
import numpy as np
from imutils import contours


ANSWER_KEY = {0: 1, 1: 4, 2: 3, 3: 2, 4: 1}

input = input('Enter an image: ')
img = cv2.imread(f'./img/{input}.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

# find contours in the edge map, then initialize
# the contour that corresponds to the document
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None
# ensure that at least one contour was found
if len(cnts) > 0:
    # sort the contours according to their size in
    # descending order
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    # loop over the sorted contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points,
        # then we can assume we have found the paper
        if len(approx) == 4:
            docCnt = approx
            break

# apply a four point perspective transform to both the
# original image and grayscale image to obtain a top-down
# birds eye view of the paper
paper = four_point_transform(img, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))
# Threshold
thresh = cv2.threshold(
    warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Find contours
cnts = cv2.findContours(
    thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

questionCnts = []

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)

    ar = w / float(h)

    if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
        questionCnts.append(c)

questionCnts = contours.sort_contours(
    questionCnts, method="top-to-bottom")[0]

correct = 0

for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
    cnts = contours.sort_contours(questionCnts[i: i + 5])[0]
    bubbled = None

    for (j, c) in enumerate(cnts):
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)

        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)

        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j)
    color = (0, 0, 255)
    k = ANSWER_KEY[q]

    if k == bubbled[1]:
        color = (0, 255, 0)
        correct += 1

    cv2.drawContours(paper, [cnts[k]], -1, color, 3)

score = (correct / 5.0) * 100
print("[INFO] score: %.2f" % score + "%")
cv2.putText(paper, "%.2f" % score + "%", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

cv2.imshow("Thres", thresh)
cv2.imshow("Original", img)
cv2.imshow("Exam", paper)
cv2.waitKey(0)
cv2.destroyAllWindows()