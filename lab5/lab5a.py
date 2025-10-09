from math import pi, e
import cv2
import numpy
from cvlib import rgblist_to_cvimg

image = cv2.imread("plane.jpg")


def cvimg_to_list(img: numpy.ndarray) -> list[tuple[int, int, int]]:
    """Convert an OpenCV image array into a flat list of BGR pixel tuples.

    Args:
        img (numpy.ndarray): The image array in BGR color order.
            Shape is (rows, cols), where each element contains integer values
            (0-255).

    Returns:
        list[tuple[int, int, int]]: A flat list of length rows*cols,
            where each element is a pixel represented as (B, G, R).
            Pixels are ordered row by row: top-to-bottom, left-to-right.
    """
    img_list = []

    for row in img:
        for pixel in row:
            img_list.append((int(pixel[0]), int(pixel[1]), int(pixel[2])))

    return img_list


def unsharp_mask(n: int) -> list:
    """Generate a 2D unsharp mask kernel of size n x n.

    The kernel is centered at (0, 0), where it's set to 1.5, and uses a
    negative Gaussian function to define all others values except the center.

    Args:
        n (int): A number to serve as a parameter to the size of the matrix
            that the function will return.

    Returns:
        list: A matrix to serve as a unsharping mask. Each element was
            determined with help of Negative Gaussian Blur formula.
    """

    # Creates an extern list to be returned further.
    matrix = []

    # Determines a range of numbers based on the parameter integer n
    if n % 2 == 0:
        coord_values = range(-(n // 2), n // 2)
    else:
        coord_values = range(-(n // 2), (n // 2) + 1)

    # inner list representing one image row
    row = []
    for v1 in coord_values:
        for v2 in coord_values:
            # pixel in position (0,0) will always be 1.5
            if v1 == v2 == 0:
                row.append(1.5)
            else:
                # constant that can easily be changed
                S = 4.5

                # divides the formula in parts to be easily readable
                constant = -(1 / (2 * pi * S**2))
                exp_part = e ** (-(v1**2 + v2**2) / (2 * S**2))
                gauss_value = constant * exp_part

                row.append(gauss_value)

        # append the current row to the matrix and start a new row
        matrix.append(row)
        row = []

    return matrix


if __name__ == "__main__":
    image_list = cvimg_to_list(image)
    converted_img = rgblist_to_cvimg(
        image_list, image.shape[0], image.shape[1]
    )
    cv2.imshow("converted", converted_img)
    cv2.waitKey(0)

    image = cv2.imread("plane.jpg")
    kernel = numpy.array(unsharp_mask(11))
    filtered_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow("filtered", filtered_image)
    cv2.waitKey(0)
