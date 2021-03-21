import cv2
import numpy as np
import os

load_dir = '/path/to/image/directory/'

def color_extraction(input_image):
	image = cv2.imread(input_image)
	H = []
	S = []
	V = []
	for pixel in image:
		for a_pixel in pixel:
			H.append(a_pixel[0])
			S.append(a_pixel[1])
			V.append(a_pixel[2])
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return H, S, V

def generate_csv(input1, input2, input3, name1, name2, name3):
	with open('color_extraction.csv', 'w') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerow([str(name1), str(name2), str(name3)])
		for color in list(zip(input1, input2, input3)):
			writer.writerow([color[0], color[1], color[2]])

def main():
	for image in os.listdir(directory):