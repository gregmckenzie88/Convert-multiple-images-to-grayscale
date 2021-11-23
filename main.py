import os
import cv2

#  access directory with images
images = os.listdir('images')

# loop through each entry, saving a gray verion of each
for image in images:
  # save gray version of image
  gray = cv2.imread(f'images/{image}', 0)
  # write new grayscale file
  cv2.imwrite(f'gray-{image}', gray)