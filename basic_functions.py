import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
print("Kernel:\n", kernel)

path = "resources/cat.jpg"

img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

imgCanny = cv2.Canny(imgBlur, 100, 100)

imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)

imgEroded = cv2.erode(imgDilated, kernel, iterations=1)

cv2.imshow("Cat", img)
cv2.imshow("Gray Cat", imgGray)
cv2.imshow("Blurred Cat", imgBlur)
cv2.imshow("Canny Cat", imgCanny)
cv2.imshow("Dilated Cat", imgDilated)    
cv2.imshow("Eroded Cat", imgEroded)

cv2.waitKey(0)