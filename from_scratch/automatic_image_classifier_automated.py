import cv2
import numpy as np
import glob
import pickle


def preprocess_the_image(path_to_img):
    img_ = cv2.imread(path_to_img, cv2.IMREAD_GRAYSCALE)  # loading the image
    simplified_img = img_ / 255  # Simplify the image
    flat_img = simplified_img.flatten()  # Flatten the image
    return flat_img


def convolve_img(flat_img, filter__):
    convolution_ = (flat_img * filter__).sum()  # convolution
    return convolution_


squares = glob.glob("img/square*.png")  # selects all the images with square as start
crosses = glob.glob("img/cross*.png")  # selects all the images with square as start

# img_url = squares[0]
#
# flattened_img = preprocess_the_image(img_url)  # load, simplify and flatten
# convolution = convolve_img(flattened_img)  # filter and convolution


size_of_image = (7, 7)
flat_size = size_of_image[0] * size_of_image[1]

bad_filter = True
attempts = 0
while bad_filter:
    attempts += 1
    print(f'Attempt number: {attempts}', end='\r')
    filter_ = np.random.randint(-1, 2, size=flat_size)  # filter
    for i in range(1, 6):
        convolution1 = convolve_img(preprocess_the_image(squares[i]), filter_)
        if convolution1 < 0:  # Now, 0 is for time-being our distinction line
            break

        convolution2 = convolve_img(preprocess_the_image(crosses[i]), filter_)
        if convolution2 >= 0:  # Now, 0 is for time-being our distinction line
            break

        if i == 5:
            good_filter = filter_ # which one reaches here only becomes good filter
            bad_filter = False

print("attempts:", attempts)
print("The Good filter: ", good_filter)

# saving the above found filter to a text file so that we can run classfication from other files
with open('good.filter','wb') as filter_file:
    pickle.dump(good_filter, filter_file)

# this has to be put into separate folder with preprocess and convolve functions
with open('good.filter','rb') as filter_file:
    good_filter = pickle.load(filter_file)


def classify_img(img_url):
    convolution = convolve_img(preprocess_the_image(img_url), good_filter)
    if convolution >= 0:
        return 'Square'
    else:
        return 'Cross'

for url in crosses:
    result = classify_img(url)
    print(f'File {url} \t: {result}')
# everything is cross for learned images for crosses

for url in squares:
    result = classify_img(url)
    print(f'File {url} \t: {result}')

# WE NEED ALSO TO CHECK WHETHER OUR MODEL WORKS ON UNKNOWN IMAGES AS WELL

