# %%
import cv2 
from cvlib import rgblist_to_cvimg

# 5A1
image = cv2.imread('image.jpeg')

def cvimg_to_list(image):
    image_list = []

    for row in image:
        for pixel in row:
            image_list.append((int(pixel[0]), int(pixel[1]), int(pixel[2])))

    return image_list 

list_img = cvimg_to_list(image)

converted_img = rgblist_to_cvimg(list_img, image.shape[0], image.shape[1])

cv2.imshow("converted", converted_img)

cv2.waitKey(0)

#%%
# 5A2
from math import pi as pi, e as e
import cv2
import numpy

def unsharp_mask(n:int):

    #m_pos = n**2

    list_values = []
    length_height = range(-(n//2),(n//2)+1)

    list_per_row = []
    for v1 in length_height:
        for v2 in length_height:
            if v1 == v2 == 0:
                list_per_row.append(1.5)
            else:                
                s = 4.5
                constant = -(1/(2*pi*s**2))
                exp_part = e**(-(v1**2 + v2**2) / 2*s**2 )
                gaus_blur = constant * exp_part
                list_per_row.append(gaus_blur)

        list_values.append(list_per_row)
        list_per_row = []

    return list_values

img = cv2.imread('image.jpeg')
kernel = numpy.array(unsharp_mask(11))
filtered_img = cv2.filter2D(img, -1, kernel)    
cv2.imshow("filtered", filtered_img)
cv2.waitKey(0)

# %%

print(5//2)
print(3//2)
print(1//2)