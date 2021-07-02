import cv2
import os

images = ['img/'+img for img in os.listdir('img/') if img in ['horizontal_down.png','horizontal.png', 'vertical_left.png', 'vertical.png']]
print(images)


def classify_image(image_url):
    img = cv2.imread(image_url, cv2.IMREAD_GRAYSCALE)  # load image
    img_simplified = img / 255  # SIMPLIFY IMAGE (0 - 1 conversion)
    img_flattened = img_simplified.flatten()  # FLATTEN
    filter_selected = [1, -1, 1, 1, -1, 1, 1, -1, 1]  # FILTER
    convolution = img_flattened * filter_selected  # multiplying flattened image and filter is called CONVOLUTION
    convolution_sum = convolution.sum()  # SUM OF CONVOLUTION
    if convolution_sum == 1:  # CONDITION
        print(f'{image_url} is Horizontal')
        cv2.imshow('This Image is a Horizontal Image', cv2.resize(img, (500, 500), interpolation=0))
    else:
        cv2.imshow('This Image is a Vertical Image', cv2.resize(img, (500, 500), interpolation=0))
        print(f'{image_url} is Vertical')
    return 0


for image in images:
    classify_image(image)

cv2.waitKey(0)
