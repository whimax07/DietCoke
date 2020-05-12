import sys
from os.path import abspath, dirname, join

import numpy as np
from PIL import Image

sys.path.insert(0, abspath(join(dirname(__file__), '..\\ColourPalet')))
import ColourBox as cb


# --- Import the image.
image = Image.open(
    r'C:\Users\Max\Documents\GitHub\DietCoke\ImageTool\TestImage.jpg')
# Convert it to a RGB array.
data = np.asarray(image)

# Get a slice of the image.
image2 = data[500:650, 380:490, :]
simg2 = np.shape(image2)
image3 = np.zeros([simg2[0] * 2, simg2[1] * 2, simg2[2]], dtype='uint8')

# Make image3 twice as big as image2.
for i in range(simg2[0]):
    for j in range(simg2[1]):
        image3[(2 * i, 2 * j)] = image2[(i, j)]
        image3[(2 * i + 1, 2 * j)] = image2[(i, j)]
        image3[(2 * i, 2 * j + 1)] = image2[(i, j)]
        image3[(2 * i + 1, 2 * j + 1)] = image2[(i, j)]

# Show the images.
image2 = Image.fromarray(image2)
image2.show()
image3 = Image.fromarray(image3)
image3.show()

# --- Display the colour of a pixel of the image.
# cb.ColourSwob(cb.rgb2Hex(data[580, 430, :]))
