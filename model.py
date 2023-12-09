import cv2
import numpy as np

def convert_to_pencil_sketch(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Blend the grayscale image with the blurred inverted image using color dodge
    pencil_sketch = cv2.divide(gray_image, 255 - blurred_image, scale=256.0)

    return pencil_sketch

# Load the image
image_path = 'SuriyaPrakash.jpg'
image = cv2.imread(image_path)

# Convert the image to pencil sketch
pencil_sketch = convert_to_pencil_sketch(image)

# Display the original image and the pencil sketch
cv2.imshow('Original Image', image)
cv2.imshow('Pencil Sketch', pencil_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
