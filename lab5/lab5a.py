import cv2
from cvlib import rgblist_to_cvimg
from math import pi , e 
import numpy

image = cv2.imread('plane.jpg')

def cvimg_to_list(image):
    """
    Function that takes an array with pixels of a picture and transforms it
    into a list with the pixle sin tuples.
    """
    image_list = []

    for row in image:
        for pixel in row:
            image_list.append((int(pixel[0]), int(pixel[1]), int(pixel[2])))

    return image_list 

list_img = cvimg_to_list(image)
converted_img = rgblist_to_cvimg(list_img, image.shape[0], image.shape[1])
cv2.imshow("converted", converted_img)
cv2.waitKey(0)



def unsharp_mask(n:int)->list:

    """
    Function that takes a integer n as a parameter to create a matrix n x n
    and with help of Negativ gaussian blur returns a list with values to be
    used to create an image mask.
    """

    #Creates an extern list to be returned further.
    #Determines a rang eof numbers based on the parameter integer n
    matrix = []
    cord_values = range(-(n//2),(n//2)+1)

    #Creates a intern list that will be used to append to the external list 
    #per loop.
    rows = []
    for v1 in cord_values:
        for v2 in cord_values:
            #pixel in position (0,0) will always be 1.5
            if v1 == v2 == 0:
                rows.append(1.5)
            else:                
                #constant that can easily be changed
                S = 4.5

                #divides the formula in parts to be easily readable
                constant = -(1/(2*pi*S**2))
                exp_part = e**(-(v1**2 + v2**2) / (2*S**2) )
                gaus_blur = constant * exp_part

                rows.append(gaus_blur)

        #appends the intern list and "resets" it to an empty list
        matrix.append(rows)
        rows = []

    return matrix

img = cv2.imread('plane.jpg')
kernel = numpy.array(unsharp_mask(11))
filtered_img = cv2.filter2D(img, -1, kernel)    
cv2.imshow("filtered", filtered_img)
cv2.waitKey(0)
