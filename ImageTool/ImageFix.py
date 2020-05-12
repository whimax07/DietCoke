import numpy as np
from PIL import Image
import sys
from dietcoke import colourbox


image = Image.open(
    r'C:\Users\Max\Documents\GitHub\DietCoke\ImageTool\TestImage.jpg')
print(image.size)

data = np.asarray(image)

print(data[480, 640, :])
