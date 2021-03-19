from keras.preprocessing.image import ImageDataGenerator
from skimage import io
import numpy as np
import os
from PIL import Image

load_dir = 'path/to/folder'
save_dir = 'path/to/folder'

datagen = ImageDataGenerator(
            rotation_range = 360,
            width_shift_range = 0.2,
            height_shift_range = 0.2,
            shear_range = 0.2,
            zoom_range = 0.2,
            horizontal_flip = True,
            fill_mode = 'reflect')

dataset = []
SIZE = 128

images = os.listdir(load_dir)
for i, image_name in enumerate(images):
    if image_name.split('.')[1] == 'jpg' or image_name.split('.')[1] == 'png':
        image = io.imread(load_dir + image_name)
        image = Image.fromarray(image, 'RGB')
        image = image.resize((SIZE,SIZE))
        dataset.append(np.array(image))

image_array = np.array(dataset)

i = 0
for batch in datagen.flow(image_array, batch_size = 16,
                            save_to_dir = save_dir,
                            save_prefix = 'aug',
                            save_format = 'png'):
    i += 1
    if i > 20:
        break

print("Augmentation is done, Resulting {} images".format(i))
