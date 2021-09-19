from imgprocesser import load_images
import numpy as np

images = np.array(load_images('r/'))

print(images.shape)
print(images)


