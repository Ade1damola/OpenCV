import cv2
import numpy as np

path = "resources/cards.jpg"

img = cv2.imread(path)

height, width = 350, 250

points1 = np.float32([[111, 218], 
                     [290, 187], 
                     [152, 483], 
                     [351, 441]])

points2 = np.float32([[0, 0],
                     [width, 0],
                     [0, height],
                     [width, height]])

matrix = cv2.getPerspectiveTransform(points1, points2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

for i in range(len(points1)):
    cv2.circle(img, (int(points1[i][0]), int(points1[i][1])), 5, (0, 255, 0), cv2.FILLED) 

cv2.imshow("Card", img)
cv2.imshow("Warped Card", imgOutput)

cv2.waitKey(0)