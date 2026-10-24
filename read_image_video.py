import cv2

# img = cv2.imread("resources/circuit_design.png")

# cv2.imshow("Circuit Design", img)

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture("resources/tower_crane.mp4")
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break