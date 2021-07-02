# importing custom made function from other file so create image from array to file save.
from from_scratch.create_image.np2img import CreateImage

# importing necessary external libraries
import numpy as np
import cv2
import os
os.makedirs(name='img', exist_ok=True)  # creating img folder for png files

# Vertical Array Creation for 3 * 3 pixel image
vertical = np.array([[0, 255, 0],
                     [0, 255, 0],
                     [0, 255, 0]])

# Horizontal Array Creation
horizontal = np.array([[0, 0, 0],
                       [255, 255, 255],
                       [0, 0, 0]])

# saving the above arrays into images in the same folder
CreateImage(vertical, 'img/vertical.png')
CreateImage(horizontal, 'img/horizontal.png')

# Loading those images
vertical = cv2.imread("img/vertical.png", cv2.IMREAD_GRAYSCALE)
horizontal = cv2.imread("img/horizontal.png", cv2.IMREAD_GRAYSCALE)

# while showing image since image is too smaller to view.. we are resizing it for viewing purpose using cv2.resize fn.
# interpolation keeps img as it is without any filters
# cv2.imshow('Vertical Image', cv2.resize(vertical, (500, 500), interpolation=0))
# cv2.imshow('Horizontal Image', cv2.resize(horizontal, (500, 500), interpolation=0))

# 1) IMAGE PREPARATION ==============================================================================================
vertical = vertical / 255  # keeps number between 0 and 1.. in this case only 0 and 1
horizontal = horizontal / 255  # 'imshow' automatically identifies it as 0 - 1 instead of 0 - 255 as earlier

# Flattening the numpy array
vertical_flattened = vertical.flatten()  # [0. 1. 0. 0. 1. 0. 0. 1. 0.]
horizontal_flattened = horizontal.flatten()  # [0. 0. 0. 1. 1. 1. 0. 0. 0.]

cv2.imshow('Vertical Flattened Image', cv2.resize(vertical_flattened, (50, 500), interpolation=0))
cv2.imshow('Horizontal Flattened Image', cv2.resize(horizontal_flattened, (50, 500), interpolation=0))

# 2) CREATE IMAGE RECOGNITION CLASSIFIER ============================================================================

# trying some operations to check whether any of them can classify these images - first, summing
vertical_sum = vertical_flattened.sum()  # 3.0 -- output
horizontal_sum = horizontal_flattened.sum()  # 3.0
# since both sums are equal, by summing them we cannot identify horizontal or vertical -- in our case here

# second, now trying out some filters -- try a random filter for myself
filter1 = [1, -1, 1, -1, 1, -1, 1, -1, 1]  # should be of same length as of the flattened array

# applying same filter to both and summing it up to see whether any difference
print(horizontal_flattened * filter1)  # [ 0. -0.  0. -1.  1. -1.  0. -0.  0.]
print((horizontal_flattened * filter1).sum())  # -1.0
print((vertical_flattened * filter1).sum())  # -1.0 # again same So we cannot use it to classify

# third, another filter trying...
filter2 = [1, -1, 1, 1, -1, 1, 1, -1, 1]  # should be of same length as of the flattened array

print((horizontal_flattened * filter2).sum())  # 1.0
print((vertical_flattened * filter2).sum())  # -3.0 # now difference. we can use this filter to classify

# therefore, we can say
flattened = [horizontal_flattened, vertical_flattened]
for num, array in enumerate(flattened, start=1):
    if (array * filter2).sum() == 1:
        print(f"The image number {num} is Horizontal Image")
    else:
        print(f"The image number {num} is Vertical Image")

cv2.waitKey(0)  # wait function keep the window in loop until manually closing the windows




