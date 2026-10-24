import cv2
import numpy as np

img1 = cv2.imread("resources/cat.jpg")
img2 = cv2.imread("resources/brain.jpg")

print("Image 1 shape:", img1.shape)
print("Image 2 shape:", img2.shape)

img1_resized = cv2.resize(img1, (500, 500), None, 0.5, 0.5)
img2_resized = cv2.resize(img2, (500, 500), None, 0.5, 0.5)

horizontally_stacked = np.hstack((img1_resized, img2_resized))
vertically_stacked = np.vstack((img1_resized, img2_resized))

cv2.imshow("Horizontally Stacked", horizontally_stacked)
cv2.imshow("Vertically Stacked", vertically_stacked)

cv2.waitKey(0)