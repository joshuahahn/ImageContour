import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

display_lookup = {
    # Class 1: No contour lines
    tuple([0,0,0,0]) : 1,
    tuple([1,1,1,1]) : 2,
    # Class 2: Re-classify; ambiguous
    tuple([1,0,0,0]) : 3,
    tuple([0,1,0,0]) : 4,
    tuple([0,0,1,0]) : 5,
    tuple([0,0,0,1]) : 6,
    tuple([1,1,1,0]) : 7,
    tuple([1,1,0,1]) : 8,
    tuple([1,0,1,1]) : 9,
    tuple([0,1,1,1]) : 10,
    # Class 3: One contour line
    tuple([1,1,0,0]) : 6,
    tuple([1,0,1,0]) : 7,
    tuple([1,0,0,1]) : 8,
    tuple([0,1,1,0]) : 9,
    tuple([0,1,0,1]) : 10,
    tuple([0,0,1,1]) : 11,
    
}
    
def marchingSquares(img, k, ax):
    height, width = img.shape

    # Define a 2x2 cell that inspects all spaces in the image.
    for row in range(10):
        for col in range(10):
            binIndex = np.zeros(4)
            if (abs(img[row, col] - img[row, col+1]) > k): binIndex[0] = 1
            if (abs(img[row, col+1] - img[row+1, col+1]) > k): binIndex[1] = 1
            if (abs(img[row+1, col+1] - img[row+1, col]) > k): binIndex[2] = 1
            if (abs(img[row+1, col] - img[row, col]) > k): binIndex[3] = 1
            renderContour(display_lookup[tuple(binIndex)], row, col, ax)
        
def renderContour(contourIdx, row, col, ax):
    if (contourIdx == 1 or contourIdx == 16):
        # Class 1; do nothing
        pass
    elif (contourIdx == 2):
        # Class 2: 
        pass

    X = [row+0.5, row+0.5]
    Y = [col,col+1]
    ax.plot(X,Y,color='k')


def main():
    RGBImage = Image.open('panda.jpeg')
    grayImage = ImageOps.grayscale(RGBImage)
    imageArray = np.asarray(grayImage)

    #plt.imshow(imageArray, cmap='gray') # cmap is used to display image as gs
    #plt.show()
    imageArray = imageArray.astype('int')

    fig, ax = plt.subplots()
    marchingSquares(imageArray, 0.5, ax)

    plt.show()

if __name__ == "__main__":
    main()



"""
k = 7

0 - 15
  x
5    9

Draw a vertical line from middle of top to center






"""