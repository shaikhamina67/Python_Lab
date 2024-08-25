#Lab1: Using a sobel filter, filter the image and then display it.

import scipy.ndimage
from scipy import misc
import matplotlib.pyplot as plt

# reads a dog face
image = misc.face()
image = plt.imread(r'C:/Users/shaik/Downloads/dog.jpg')

# Apply Sobel Filter
sobel_filtered_image = scipy.ndimage.filters.sobel(image)

# Create a figure and axes array
fig, axis = plt.subplots(1, 2, figsize=(10, 5))

# The Original image
axis[0].imshow(image)
axis[0].set_title("The Original Picture")
axis[0].axis('off')
# The Sobel Filter
axis[1].imshow(sobel_filtered_image)
axis[1].set_title("The Sobel Filtered Picture")
axis[1].axis('off')

plt.show()

