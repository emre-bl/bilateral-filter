import numpy as np
import cv2 as cv

def G_x(x,sigma):
    import math
    return math.exp(-(x**2)/(2*(sigma**2)))/(sigma*((2*math.pi)**0.5))

def kernel_calculation(part,sigma_r,sigma_s):
    sum = 0.0
    normalization = 0.0
    pi = part.shape[0]//2
    for i in range(part.shape[0]):
        for j in range(part.shape[1]):
            distance = ((i-pi)**2 + (j-pi)**2)**0.5
            intensity_difference = abs(part[i][j] - part[pi][pi])
            normalization+=(G_x(distance,sigma_s)*G_x(intensity_difference,sigma_r))
            sum += G_x(distance,sigma_s)*G_x(intensity_difference,sigma_r)*part[i,j]
    return sum/normalization

def bilateral_filter(image,kernel_size,sigma_s,sigma_r):
    border = kernel_size//2
    img = image.copy()
    return_img = np.zeros(img.shape)
    img = cv.copyMakeBorder(img, border, border, border,border, cv.BORDER_REPLICATE, None)

    for x in range(return_img.shape[0]):
        for y in range(return_img.shape[1]):
            part = img[x:x+2*border+1, y:y+2*border+1]
            return_img[x,y] = kernel_calculation(part,sigma_s,sigma_r)

    return return_img
