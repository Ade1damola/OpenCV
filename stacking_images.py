import cv2
import numpy as np

import myutilis

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    # cv2.imshow("Video", img)
    

    kernel = np.ones((5, 5), np.uint8)
    print("Kernel:\n", kernel)

    # path = "resources/cat.jpg"

    # img = cv2.imread(path)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (9, 9), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 100)
    imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)
    imgEroded = cv2.erode(imgDilated, kernel, iterations=1)

    imgBlank = np.zeros((200, 200), np.uint8)

    StackedImages = myutilis.stackImages(0.4, ([img, imgGray, imgBlur, img, imgGray, imgBlur], 
                                      [imgCanny, imgDilated, imgEroded, imgCanny, imgDilated, imgEroded],
                                      [img, imgGray, imgBlur, img, imgGray, imgBlur], 
                                      [imgCanny, imgDilated, imgEroded, imgCanny, imgDilated, imgEroded]))

    cv2.imshow("Stacked Images", StackedImages)
    # cv2.imshow("Cat", img)
    # cv2.imshow("Gray Cat", imgGray)
    # cv2.imshow("Blurred Cat", imgBlur)
    # cv2.imshow("Canny Cat", imgCanny)
    # cv2.imshow("Dilated Cat", imgDilated)    
    # cv2.imshow("Eroded Cat", imgEroded)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break