# USAGE
# python opencv_drawing.py

# Import necessary libraries
import numpy as np
import cv2

# Create an empty image (canvas)
# 1000 x 1000, 3 channels (R, G, B) unsigned 8-bit integer
canvas = np.zeros((1000, 1000, 3), dtype="uint8")

# Draw a green line through the canvas, 5 pixels thick
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green, 5)

# Show the line drawing
cv2.imshow("Draw - line", canvas)
cv2.waitKey(0)

# Draw a red (hollow) rectangle on the canvas, 3 px thick
red = (0, 0, 255)
cv2.rectangle(canvas, (100, 200), (500, 400), red, 3)

# Show the drawing
cv2.imshow("Draw - rectangle", canvas)
cv2.waitKey(0)

# Draw a blue (filled) rectangle on the canvas
blue = (255, 0, 0)
cv2.rectangle(canvas, (500, 500), (800, 800), blue, -1)

# Show the drawing
cv2.imshow("Draw - filled rectangle", canvas)
cv2.waitKey(0)

# Draw a white circle on the canvas, 3px thick
white = (255, 255, 255)
cv2.circle(canvas, (500, 500), 100, white, 3)

# Show the drawing
cv2.imshow("Draw - filled rectangle", canvas)
cv2.waitKey(0)
