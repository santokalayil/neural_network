import os
import sys
import cv2
import numpy as np

from from_scratch.create_image.np2img import CreateImage

# image creation for this project script
vertical_left = np.array([
    [255, 0, 0],
    [255, 0, 0],
    [255, 0, 0]
])
horizontal_down = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [255, 255, 255]
])
# creating 3x3 pixel images from above arrays
CreateImage(vertical_left, 'img/vertical_left.png')
CreateImage(horizontal_down, 'img/horizontal_down.png')


def preprocess_the_image(path_to_img):
    img_ = cv2.imread(path_to_img, cv2.IMREAD_GRAYSCALE)  # loading the image
    simplified_img = img_ / 255  # Simplify the image
    flat_img = simplified_img.flatten()  # Flatten the image
    return flat_img


# preprocessing
flattened_vertical = preprocess_the_image("img/vertical.png")
flattened_horizontal = preprocess_the_image("img/horizontal.png")

#  loop for getting always a good filter
count = 1
while True:
    # filtering
    filter_ = np.random.randint(-1, 2, size=flattened_vertical.size)  # random generation of filter
    # applying filter to flattered image and suming up to convolution
    convolution_vertical = (flattened_vertical * filter_).sum()
    convolution_horizontal = (flattened_horizontal * filter_).sum()

    # print(convolution_horizontal)
    # print(convolution_vertical)
    # now we need a good filter, so sometimes many random generation attempts are necessary for
    if convolution_horizontal != convolution_vertical:
        print(f"Found filter : {filter_}")
        print(f"Number of Attempts: {count}")
        break
    else:
        count += 1


# .imshow("Image Window", cv2.resize(img, (500,500), interpolation=0))
# cv2.waitKey(0)

# =======================================================================================

