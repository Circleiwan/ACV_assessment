from PIL import Image
import cv2
import os
import random
import numpy as np

def add_noise():
	#adding noise to the image
	pass

def convert_image_to_HSV(image):
	#convert image to HSV
	converted = cv2.cvtColor(image, cv2.COLOR_HSV)
	return image

def load_and_augementation(load_path, save_path, amount):
	#exponentially increase amount of dataset
	for _ in range(0, amount):
		list_of_rotations = [90,180,270]
		choice = random.choice(list_of_rotations)
		for image in os.listdir(load_path):
			file, extension = os.path.splitext(image)
			if extension == ".jpeg" or extension == ".jpg" or extension == ".png"
				convert_image_to_HSV(image)
				rotated_image = image.rotate(choice)
				rotated_image.save(save_path)
			else:
				continue

def main():
	load_path = 
	save_path = 
	load_and_augementation(load_path, save_path)

main()