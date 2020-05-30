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

# Define the scaling factor
scaleFactor = (5, 5)

# Get a slice of the image.
image2 = data
simg2 = np.shape(image2)
image3 = np.zeros([simg2[0] * scaleFactor[0], simg2[1] * scaleFactor[1],
                  simg2[2]], dtype='uint8')

# Make image3 scaleFactor as big as image2.
for i in range(simg2[0]):
    for j in range(simg2[1]):
        Ith = scaleFactor[0] * i
        Jth = scaleFactor[1] * j
        if np.sum(image2[(i, j)]) < 105:
            image3[Ith:Ith + scaleFactor[0], Jth:Jth + scaleFactor[1], :] = \
                (0, 0, 0)
        else:
            image3[Ith:Ith + scaleFactor[0], Jth:Jth + scaleFactor[1], :] = \
                image2[i, j, :]


# Show the images.
# image2 = Image.fromarray(image2)
# image2.show()
# image2.save('Image2.png')
image3 = Image.fromarray(image3)
image3.show()
# image3.save('Image6.png')

# --- Display the colour of a pixel of the image.
# cb.ColourSwob(cb.rgb2Hex(data[580, 430, :]))
