import cv2
import numpy as np
import math
import random
import os

drawMode = False
eraseMode = False
mx, my = 0, 0
radius = 10
delta_radius = 2
current_color = [0, 0, 0]
circles = []

def update_r(val):
    global current_color
    current_color[2] = val

def update_g(val):
    global current_color
    current_color[1] = val

def update_b(val):
    global current_color
    current_color[0] = val

def mscbkfunc(event, x, y, flags, param):
    global drawMode, mx, my, radius, delta_radius, eraseMode

    if event == cv2.EVENT_MOUSEMOVE:
        mx, my = x, y

    if event == cv2.EVENT_LBUTTONDOWN:
        drawMode = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawMode = False

    if event == cv2.EVENT_RBUTTONDOWN:
        eraseMode = True
    elif event == cv2.EVENT_RBUTTONUP:
        eraseMode = False

    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:   # Mouse Wheel Up
            radius += delta_radius
        else:           # Mouse Wheel Down
            radius -= delta_radius
            if radius < 4:
                radius = 4

def main():
    global drawMode, mx, my, current_color, circles
    w, h = 800, 600
    image = 255 * np.ones((h, w, 3), np.uint8)
    helper_window = np.zeros((500, 400, 3), np.uint8)
    cv2.namedWindow("Helper")
    cv2.createTrackbar("R: ", "Helper", 0, 255, update_r)
    cv2.createTrackbar("G: ", "Helper", 0, 255, update_g)
    cv2.createTrackbar("B: ", "Helper", 0, 255, update_b)



    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", mscbkfunc)

    while True:
        cv2.imshow("Image", image)
        cv2.imshow("Helper", helper_window)

        if drawMode:
            if (mx, my, radius, current_color) not in circles:
                circles.append((mx, my, radius, current_color.copy()))
                image = cv2.circle(image, (mx, my), radius, current_color, -1)
        if eraseMode:
            for i in range(len(circles) - 1, -1, -1): # n-1, n-2, ..., 3, 2, 1, 0
                c = circles[i]
                distance = math.hypot(c[0] - mx, c[1] - my)
                if distance <= c[2]:
                    circles.pop(i)
                    image = 255 * np.ones((h, w, 3), np.uint8)
                    for c1 in circles:
                        image = cv2.circle(image, (c1[0], c1[1]), c1[2], c1[3], -1)
                    break

        key = cv2.waitKey(5)
        if key == 27 or key == ord('q'):
            break
        elif key == 8:  # backspace key
            circles.clear()
            image = 255 * np.ones((h, w, 3), np.uint8)
        elif key == ord('s'):
            filename = f'image_{random.randint(1, 9999999)}.png'
            while os.path.isfile(filename):
                filename = f'image_{random.randint(1, 9999999)}.png'
            cv2.imwrite(filename, image)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
