import cv2
import numpy as np
import os
import csv
load_dir = 'path/to/augmented/directory'
H = []
S = []
V = []
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
		s = average(S)
		v = average(V)
		writer.writerow([h,s,v])
	#print(H)