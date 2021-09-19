
# load and show an image with Pillow
from PIL import Image
import numpy as np
from os import listdir

SIZE = 256
OUTPUT_METRICS_SIZE = SIZE * SIZE


def load_images (img_dir):
    imageOutput = []
    outputMetrics = np.empty((OUTPUT_METRICS_SIZE,SIZE))
    print('load_images .. ')
    ## load images from dir
    for filename in listdir(img_dir):		
        # extract image id
        image_path=img_dir+filename
        print(image_path)
        # load and resize image to 256 x 256 
        print('gray scaled')
        image = Image.open(image_path).resize((256,256)).convert('L')
        image.load()
        image.show()
        image_data = np.asarray(image, dtype="int32")
        
        print('calculate metrics')
        for i in range(SIZE):
            for j in range(SIZE):
                # calculate metric
                outputMetrics[i][0] = 0

        # convert to 2d to 1D image
        image_data = image_data.flatten()
        print('flatten image')
        print(image_data.shape)
        print(image_data[0:10])
        imageOutput.append(image_data)




    return imageOutput, outputMetrics


    # resize image



    # append them to output array

    imageOutput = [] # each row is an image  1D array


# Open the image form working directory
# image = Image.open('1.jpg')

# summarize some details about the image

# print(image.format)
# print(image.size)
# print(image.mode)

# print(np.array(image).shape)

# r_image = image.resize((256,256))

# c_image = r_image.convert('L')
# load_img_cv = np.array(c_image)
# Image.fromarray(load_img_cv).save('c/g1.jpg')
# print("After :",load_img_cv[0])

# c_image.show()

# gr_im= Image.fromarray(im)
