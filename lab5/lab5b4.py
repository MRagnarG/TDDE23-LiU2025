# %%
import cv2
from cvlib import rgblist_to_cvimg
from lab5a import cvimg_to_list
from lab5b2 import generator_from_image


def gradient_condition(pixel):
    """Function that given a pixel in BGR format, will return a value(float)
        to serve as weight in a image blender.  """
    return pixel[2] / 255


def pixel_blend(p1: tuple, p2: tuple, weight:float)-> tuple:
    """Returns a new pixel (tuple) with new values based on a weight.

    Args:
        p1 (tuple): Pixel from Image 1
        p2 (tuple): Pixel from Image 2
        weight (float): Value to determine how much from each image to choose

    Returns:
        tuple: New pixel (tuple) with values from pixel blendning.
    """
    new_pix = []
    for v1, v2 in zip(
        p1,
        p2,
    ):
        result = v1 * weight + v2 * (1 - weight)
        new_pix.append(result)

    return tuple(new_pix)


def combine_images2(
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
        list: a flat list of BGR pixel tuples, length rows x cols
    """
    comb_img = []

    for index in range(len(list_hsv_pixels)):
        mask_pixel = list_hsv_pixels[index]
        weight = mask_function(mask_pixel)
        final_pixel = pixel_blend(gen1(index), gen2(index), weight)

        comb_img.append(final_pixel)

    return comb_img


if __name__ == "__main__":
    plane_img = cv2.imread("plane.jpg")
    flowers_img = cv2.imread("flowers.jpg")
    gradient_img = cv2.imread("gradient.jpg")

    condition = gradient_condition

    hsv_list = cvimg_to_list(cv2.cvtColor(gradient_img, cv2.COLOR_BGR2HSV))
    plane_img_list = cvimg_to_list(plane_img)
    flowers_img_list = cvimg_to_list(flowers_img)

    generator1 = generator_from_image(flowers_img_list)
    generator2 = generator_from_image(plane_img_list)

    result = combine_images2(hsv_list, condition, generator1, generator2)

    new_img = rgblist_to_cvimg(
        result, gradient_img.shape[0], gradient_img.shape[1]
    )
    cv2.imshow("Final image", new_img)
    cv2.waitKey(0)
