#  using opencv-python package
import cv2

#  store gray version of image in variable, gray denoted by "0" argument
color = cv2.imread('pic.png', 0)

# write to new file, with the product stored in "color variable"
cv2.imwrite('gray-pic.png', color)