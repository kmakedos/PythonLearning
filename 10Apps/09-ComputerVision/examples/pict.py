#!/usr/bin/env python3
import cv2
img = cv2.imread('IMGP9048.jpg', 0)
img2 = cv2.resize(img, (160,90))
print(img[200,200])
cv2.imshow("Moon", img2)
cv2.waitKey(2000)
cv2.destroyAllWindows()
