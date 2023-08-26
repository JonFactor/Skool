import cv2
cap = cv2.VideoCapture(0)
ret, freams = cap.read()

print(ret)