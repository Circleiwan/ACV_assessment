#!/usr/bin/env python

import cv2
import numpy as np
import os
import csv
from progress.bar import Bar

load_dir = 'C:\\Users\\orusx\\Documents\\ITS\\TA\\Program\\ACV_assessment\\Converted color space\\'

H = []
S = []
V = []

def total_in_folder(path):
	a = []
	for i in os.listdir(path):
		a.append(i)
	t = len(a)
	return t

def average(data):
	mean = sum(data) / len(data)
	return mean

with open('color_extraction.csv', 'w') as f:
	writer = csv.writer(f, lineterminator='\n')
	writer.writerow(['Hue', 'Saturation', 'Value'])
	for file_image in os.listdir(load_dir):
		image = cv2.imread(load_dir + file_image)
		for pixel in image:
			for a_pixel in pixel:
				H.append(a_pixel[0])
				S.append(a_pixel[1])
				V.append(a_pixel[2])
		h = average(H)
		h = round(h, 2)
		s = average(S)
		s = round(s, 2)
		v = average(V)
		v = round(v, 2)
		writer.writerow([h,s,v])