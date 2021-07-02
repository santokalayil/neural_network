import cv2
import numpy as np
import os

def sigmoid(x):
    return 1/(1 + np.exp(-x))


# 1 INPUT
# input preprocessing
img = cv2.imread(os.path.join("img", "vertical.png"),
                 cv2.IMREAD_GRAYSCALE)
img_total_pixels = img_size = np.multiply(img.shape[0], img.shape[1])
img = img / 255  # simplifying
img_flattened = img.flatten()  # flattening


print(img_flattened)

# 2 WEIGHTS -- earlier we called it filter
weights = np.ones(img_size) * 0.5  # [0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5]
print(weights)
convolution = np.sum(img_flattened * weights)
print(convolution)

# 3. ACTIVATION FUNCTION - here we use sigmoid
result = sigmoid(convolution)
print("Sigmoid of x after convolution: ", result)

# 4. OUTPUT
if result < 0.5:  # 0.5 is the threshold; Vertical is 0 for now
    print("Therefore, prediction is vertical")
elif result > 0.5:  # Horizontal is 1 for now
    print('Therefore, prediction is horizontal')
# here it prints horizontal which is wrong.. we will use this error to train


# 5. ERROR - How far we have lost track
error = result - 0
print("Error: ", error)
