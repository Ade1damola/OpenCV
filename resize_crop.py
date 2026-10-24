import cv2

path = "resources/brain.jpg"

img = cv2.imread(path)

print(img.shape)

width, height = 500, 500
img_resized = cv2.resize(img, (width, height))

print(img_resized.shape)

imgCropped = img[300:1120, 100:620]
imgCroppedResized = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))

cv2.imshow("Brain", img)
cv2.imshow("Brain Resized", img_resized)
cv2.imshow("Brain Cropped", imgCropped)
cv2.imshow("Brain Cropped Resized", imgCroppedResized)

cv2.waitKey(0)