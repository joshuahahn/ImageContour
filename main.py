import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps, ImageEnhance

display_lookup = {
    # Class 1: No contour lines
    tuple([0,0,0,0]) : 1,
    tuple([1,1,1,1]) : 2,
    # Class 2: 1/2 contour lines
    tuple([1,0,0,0]) : 3,
    tuple([0,1,0,0]) : 4,
    tuple([0,0,1,0]) : 5,
    tuple([0,0,0,1]) : 6,
    # Class 3: V contour lines
    tuple([1,1,1,0]) : 7,
    tuple([1,1,0,1]) : 8,
    tuple([1,0,1,1]) : 9,
    tuple([0,1,1,1]) : 10,
    # Class 3: One contour line
    tuple([1,1,0,0]) : 11,
    tuple([1,0,1,0]) : 12,
    tuple([1,0,0,1]) : 13,
    tuple([0,1,1,0]) : 14,
    tuple([0,1,0,1]) : 15,
    tuple([0,0,1,1]) : 16
}
    
def marchingSquares(img, k, ax):
    height, width = img.shape

    # Define a 2x2 cell that inspects all spaces in the image.
    for row in range(height-1):
        for col in range(width-1):
            binIndex = np.zeros(4)
            if (abs(img[row, col] - img[row, col+1]) > k): binIndex[0] = 1
            if (abs(img[row, col+1] - img[row+1, col+1]) > k): binIndex[1] = 1
            if (abs(img[row+1, col+1] - img[row+1, col]) > k): binIndex[2] = 1
            if (abs(img[row+1, col] - img[row, col]) > k): binIndex[3] = 1
            renderContour(display_lookup[tuple(binIndex)], row, col, ax)
        
def renderContour(contourIdx, row, col, ax):
    # Class 1: No contour lines
    if (contourIdx == 1 or contourIdx == 2):
        pass
    # Class 2: Half contour lines
    elif (contourIdx >= 3 and contourIdx <= 6):
        if contourIdx == 3:
            X = [row+0.5,row+0.5]
            Y = [col,col+0.5]
        elif contourIdx == 4:
            X = [row+0.5,row+1]
            Y = [col+0.5,col+0.5]
        elif contourIdx == 5:
            X = [row+0.5,row+0.5]
            Y = [col+0.5,col+1]
        elif contourIdx == 6:
            X = [row,row+0.5]
            Y = [col+0.5,col+0.5]
        X[0] = 100 - X[0]
        X[1] = 100 - X[1]
        ax.plot(Y,X,color='k')
    # Class 3: V contour lines
    elif (contourIdx >= 7 and contourIdx <= 10):
        if contourIdx == 7:
            X = [row+0.5,row+1,row+0.5]
            Y = [col,col+0.5,col+1]
        elif contourIdx == 8:
            X = [row,row+0.5,row+1]
            Y = [col+0.5,col,col+0.5]
        elif contourIdx == 9:
            X = [row+0.5,row,row+0.5]
            Y = [col,col+0.5,col+1]
        elif contourIdx == 10:
            X = [row,row+0.5,row+1]
            Y = [col+0.5,col+1,col+0.5]
        X[0] = 100 - X[0]
        X[1] = 100 - X[1]
        X[2] = 100 - X[2]
        ax.plot(Y,X,color='k')
    # Class 4: One contour line
    else:
        if contourIdx == 11:
            X = [row+0.5,row+1]
            Y = [col,col+0.5]
        elif contourIdx == 12:
            X = [row+0.5,row+0.5]
            Y = [col,col+1]
        elif contourIdx == 13:
            X = [row,row+0.5]
            Y = [col+0.5,col]
        elif contourIdx == 14:
            X = [row+0.5,row+1]
            Y = [col+1,col+0.5]
        elif contourIdx == 15:
            X = [row,row+1]
            Y = [col+0.5,col+0.5]
        elif contourIdx == 16:
            X = [row,row+0.5]
            Y = [col+0.5,col+1]
        X[0] = 100 - X[0]
        X[1] = 100 - X[1]
        ax.plot(Y,X,color='k')

    


def main():
    #RGBImage = Image.open('panda.jpeg')
    RGBImage = Image.open('images/seyoandme.jpg')
    RGBResized = RGBImage.resize((100,100), Image.ANTIALIAS)
    enhancer = ImageEnhance.Contrast(RGBResized)
    RGBContrast = enhancer.enhance(2)
    grayImage = ImageOps.grayscale(RGBContrast)
    imageArray = np.asarray(grayImage)
    imageArray = imageArray.astype('int')
    plt.imshow(RGBImage)
    plt.title("Original Image")
    #plt.imshow(imageArray, cmap='gray')# cmap is used to display image as gs

    threshold = 40

    fig,ax = plt.subplots()
    fig.suptitle("Contour generation, threshold: " + str(threshold))
    
    marchingSquares(imageArray, threshold, ax)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()