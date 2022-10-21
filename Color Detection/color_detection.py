import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    cv2.imshow("Frame", frame) 

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([161, 155, 84], np.uint8)
    red_upper = np.array([179, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    detected_output = cv2.bitwise_and(frame, frame, mask =  red_mask) 

    cv2.imshow("Red Color", detected_output) 
    if cv2.waitKey(5) & 0xFF == 27:
       break

cam.release()
cv2.destroyAllWindows()
