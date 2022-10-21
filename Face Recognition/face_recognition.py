import cv2
import numpy as np

cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier()
face_cascade.load(cv2.samples.findFile("haarcascade.xml"))


while True:
    _, frame = cam.read()
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)

    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,0), 3)

    cv2.imshow("All around me are familiar faces", frame)

    if cv2.waitKey(5) & 0xFF == 27:
       break

cam.release()
cv2.destroyAllWindows()