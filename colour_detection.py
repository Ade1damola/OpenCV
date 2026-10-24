import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, lambda x: None)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, lambda x: None)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, lambda x: None)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, lambda x: None)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, lambda x: None)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, lambda x: None)

while True:
    success, img = cap.read()
    
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hueMin = cv2.getTrackbarPos("HUE Min", "HSV")
    hueMax = cv2.getTrackbarPos("HUE Max", "HSV")
    satMin = cv2.getTrackbarPos("SAT Min", "HSV")
    satMax = cv2.getTrackbarPos("SAT Max", "HSV")
    valMin = cv2.getTrackbarPos("VALUE Min", "HSV")
    valMax = cv2.getTrackbarPos("VALUE Max", "HSV")

    lower = np.array([hueMin, satMin, valMin])
    upper = np.array([hueMax, satMax, valMax])
    
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    
    maskBGR = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    horizontalStack = np.hstack((img, maskBGR, result))
    
    # cv2.imshow("Video", img)
    # cv2.imshow("HSV Video", imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", result)
    cv2.imshow("Horizontal Stack", horizontalStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break