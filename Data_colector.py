#!!/usr/bin/env python

import cv2
import os
import time
import RPi.GPIO as GPIO
	
cTime = 0
pTime = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

cap = cv2.VideoCapture(0)

while True:
	_, img = cap.read()

	cTime = time.time()
	try:
		fps = 1/(cTime-pTime)
		pTime = cTime
		cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 
			3, (255,0,0), 3)
		if GPIO.input(2) == 0:
			i += 1
			cv2.imwrite(path + i, img)
			print("Image {} is Captured".format(i))
		else:
			pass

		cv2.imshow('Image', img)
	except ZeroDivisionError:
		continue

	if cv2.waitKey(1) == ord('q'):
		break

cap.Release()
cv2.destroyAllWindows()