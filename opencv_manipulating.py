# USAGE
# python opencv_manipulating.py -i a-10.jpg

# Import necessary libraries
import argparse
import cv2

# Function's argument parsing
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
	default="a-10.jpg", help="Path to input image")
args = vars(ap.parse_args())

# Load image and display dimensions
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
print("Width: {}".format(w))
print("Height: {}".format(h))

# Display image
cv2.imshow("Original", image)

# Access some pixel, top left, and display values
(b, g, r) = image[0, 0]
print("Pixel (0,0): R {}, G {}, B {}".format(r, g, b))

# Access some pixel, and display values.
(b, g, r) = image[250, 250]
print("Pixel (250,250): R {}, G {}, B {}".format(r, g, b))

# Change a pixel value, and fetch it to confirm.
image[250, 250] = (255, 255, 255)
(b, g, r) = image[250, 250]
print("Pixel (250,250): R {}, G {}, B {}".format(r, g, b))

# Get the centre of the image to split into quadrants
(cx, cy) = (w // 2, h // 2)

# Get top-left quadrant and display
tlq = image[0:cy, 0:cx]
cv2.imshow("Quadrant", tlq)

# Set top-left quadrant to red and display with key hook
image[0:cy, 0:cx] = (0, 0, 255)
cv2.imshow("Red Quadrant", image)
cv2.waitKey(0)
