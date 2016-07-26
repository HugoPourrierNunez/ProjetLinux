#!/usr/bin/python
# Import Pillow:
from PIL import Image

# Load the original image:
img = Image.open("test.jpg")

img.rotate(45).save("test.jpg")
