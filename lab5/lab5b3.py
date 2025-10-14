import random

import cv2
from cvlib import rgblist_to_cvimg
from lab5a import cvimg_to_list
from lab5b1 import pixel_constraint
from lab5b2 import generator_from_image


def combine_images(
    list_hsv_pixels: list,
    mask_function, 
    gen1,
    gen2,
) -> list:
    """Function that takes a list, and three other functions - a mask function
    that decides how to interpret the elements of the list, a first image
    function that returns pixels of that image and a second image function
    that returns pixels of that image - and combine the two images.

    Args:
        list_hsv_pixels (list): list with pixels in it.
        mask_function (function): function that has an array as a mask.
        gen1 (function): Function from image1
        gen2 (function): Function from image2

    Returns:
        list: final list with two image combined
    """
    comb_img = []

    for index in range(len(list_hsv_pixels)):
        mask_pixel = list_hsv_pixels[index]
        weight = mask_function(mask_pixel)

        if weight == 1:
            comb_img.append(gen1(index))
        else:
            comb_img.append(gen2(index))

    return comb_img

if __name__ == "__main__":


    # Läs in en bild
    plane_img = cv2.imread("plane.jpg")
    
    # Skapa ett filter som identifierar himlen
    condition = pixel_constraint(100, 150, 50, 200, 100, 255)
    
    # Omvandla originalbilden till en lista med HSV-färger
    hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
    plane_img_list = cvimg_to_list(plane_img)
    
    
    # Skapa en generator som gör en stjärnhimmel
    def generator1(index):
        val = random.random() * 255 if random.random() > 0.99 else 0
        return (val, val, val)
    
    
    # Skapa en generator för den inlästa bilden
    generator2 = generator_from_image(plane_img_list)
    
    # Kombinera de två bilderna till en, alltså använd himmelsfiltret som mask
    result = combine_images(hsv_list, condition, generator1, generator2)
    
    # Omvandla resultatet till en riktig bild och visa upp den
    new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
    cv2.imshow("Final image", new_img)
    cv2.waitKey(0)
