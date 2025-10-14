import cv2
from lab5a import cvimg_to_list
from cvlib import greyscale_list_to_cvimg


def pixel_constraint(hlow:int, hhigh:int, slow:int, shigh:int, vlow:int, vhigh:int):
    """Function that creates a new function that, given a pixel, returns if    
    it is between desired interval.

    Args:
        hlow (int): lowest value for hue
        hhigh (int): highest value for hue
        slow (int): lowest value for saturation
        shigh (int): highest value for saturation
        vlow (int): lowest value for value
        vhigh (int): highest value for value
    """
    def is_in_interval(pixel:tuple):
        """Function that checks if a given pixel is in a pre decided interval.

        Args:
            pixel (tuple): hsv_pixel

        Returns:
            1 if the pixel is in the desired interval, 
            0 if it's not.
        """
        (h, s, v) = pixel
        if hlow <= h <= hhigh and slow <= s <= shigh and vlow <= v <= vhigh:
            return 1
        else:
            return 0

    return is_in_interval


if __name__ == "__main__":
    hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
    plane_list = cvimg_to_list(hsv_plane)

    is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

    cv2.imshow(
        "sky",
        greyscale_list_to_cvimg(
            sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]
        ),
    )
    cv2.waitKey(0)
