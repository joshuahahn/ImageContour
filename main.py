import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import matplotlib
import math

def main():
    # Task: Given an array of floating point values, find an outline 
    # such that an outline is defined by a difference in value
    # greater than a user-defined threshold, k.

    RGBImage = Image.open('panda.jpeg')
    grayImage = ImageOps.grayscale(RGBImage)
    imageArray = np.asarray(grayImage)

    #plt.imshow(imageArray, cmap='gray')
    #plt.show()

    width = imageArray.shape[0]
    height = imageArray.shape[1]

    print(width)
    print(height)





if __name__ == "__main__":
    main()