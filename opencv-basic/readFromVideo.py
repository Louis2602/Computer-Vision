import cv2

camera_id = 0 
cap = cv2.VideoCapture('./video/traffic.mp4')
while(1):
    ret, frame = cap.read()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()