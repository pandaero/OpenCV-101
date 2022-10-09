# USAGE
# python opencv_load_image.py -i aeroplane.jpg

# Import necessary libraries
import argparse
import cv2

# Function's arguments parses, one for input, one for output
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input image")
ap.add_argument("-o", "--out", required=False, help="Name for output image")
args = vars(ap.parse_args())

# Load the image, and get its dimensions and no. of channels.
image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

# Write out the image dimensions, and number of channels.
print("width: {} px".format(w))
print("height: {}  px".format(h))
print("channels: {}".format(c))

# Show the image and wait for a keypress or window close.
cv2.imshow("Image", image)
cv2.waitKey(0)

# Determine the name of the output image, and save it.
if args["out"]:
	name = args["out"]+".jpg"
else:
	name = "savedimage.jpg"
cv2.imwrite(name, image)
