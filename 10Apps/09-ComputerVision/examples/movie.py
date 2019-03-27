#!/usr/bin/env python

import cv2,time

video = cv2.VideoCapture(0)

check, frame = video.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
time.sleep(3)

cv2.imshow('Capturing', gray)
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()
