# USAGE
# python opencv_transformations.py -i a-10.jpg

# Import necessary libraries
import numpy as np
import argparse
import imutils
import cv2

# Script's arguments parsing. (input image)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="a-10.jpg",
	help="Path to input image")
args = vars(ap.parse_args())

# Load the image and display it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# TRANSLATION - move 50px right, 100px down
# Prepare transformation affine matrix [[1 0 t_x], [0 1 t_y]]
aM = np.float32([[1, 0, 50], [0, 1, 100]])
# Assign translated image
translated = cv2.warpAffine(image, aM, (image.shape[1], image.shape[0]))
# Show translated image
cv2.imshow("Translated with affine matrix", translated)
cv2.waitKey(0)

# TRANSLATION - move 100px right, 50px down
translated = imutils.translate(image, 100, 50)
# Show the translated image
cv2.imshow("Translated with imutils", translated)
cv2.waitKey(0)

# ROTATION
# Get the centre of the image
(h, w) = image.shape[:2]
(cx, cy) = (w // 2, h // 2)
# Prepare the rotation  transformation affine matrix about the centre. 45 deg.
aM = cv2.getRotationMatrix2D((cx, cy), 45, 1)
rotated = cv2.warpAffine(image, aM, (w, h))
# Show the rotated image
cv2.imshow("Rotated with affine matrix", rotated)
cv2.waitKey(0)

# ROTATION - about another point
aM = cv2.getRotationMatrix2D((100, 100), -45, 1)
rotated = cv2.warpAffine(image, aM, (w, h))
# Show the rotated image
cv2.imshow("Rotated about point with affine matrix", rotated)
cv2.waitKey(0)

# ROTATION - using imutils
rotated = imutils.rotate(image, 270)
cv2.imshow("Rotated about centre with imutils", rotated)
cv2.waitKey(0)

# ROTATION - using imutils to preserve whole image within dimensions
rotated = imutils.rotate_bound(image, 30)
cv2.imshow("Rotated about centre with imutils bound", rotated)
cv2.waitKey(0)
