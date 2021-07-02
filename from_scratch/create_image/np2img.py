import numpy as np
from PIL import Image

def CreateImage(array, output='img.png'):
    """ CreateImage(array, output='img.png')
    """
    img_arr = np.array(array)
    image = Image.fromarray(img_arr.astype(np.uint8))
    image.save(output)
    return 0

if __name__ == '__main__':
    CreateImage([1,2,3])