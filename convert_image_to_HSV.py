#!/usr/bin/env python

import cv2
import os

load_dir = 'C:\\Users\\orusx\\Documents\\ITS\\TA\\Program\\ACV_assessment\\Augmented\\'
save_dir = 'C:\\Users\\orusx\\Documents\\ITS\\TA\\Program\\ACV_assessment\\Converted color space\\'
i = 0
for file in os.listdir(load_dir):
	image = cv2.imread(load_dir + file)
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	cv2.imwrite(save_dir + file, hsv)
	i += 1

print('Done!, converting {} images to HSV'.format(i))
