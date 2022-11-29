# USAGE
# python opencv_resizing.py -i a-10.jpg

# Import the necessary libraries
import argparse as ap
import imutils
import cv2

# Script's arguments parsing. (input image)
ap = ap.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="a-10.jpg",
	help="Path to input image")
args = vars(ap.parse_args())

# Load and display original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Resize image to 200 px wide
# Calculate target dimensions considering aspect ratio
ratio = 200 / image.shape[1]
dimensions = (200, int(image.shape[0] * ratio))
# Resize and display
resized = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized to new width", resized)
cv2.waitKey(0)

# Resize using imutils
resized = imutils.resize(image, width=400)
cv2.imshow("Resized using imutils", resized)
cv2.waitKey(0)

# Show all the interpolation methods
methods = [
	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
	("cv2.INTER_AREA", cv2.INTER_AREA),
	("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
# Loop through them, 1.5x for comparison
for (name, method) in methods:
	print("[INFO] {}".format(name))
	resized = imutils.resize(image, width=int(image.shape[1] * 1.5), inter=method)
	cv2.imshow("Method: {}".format(name), resized)
	cv2.waitKey(0)
