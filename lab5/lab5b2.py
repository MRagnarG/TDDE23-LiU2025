import cv2
from cvlib import rgblist_to_cvimg
from lab5a import cvimg_to_list


def generator_from_image(img: cv2.AsyncArray):
    """Function that given an array with pixels in it, will use a intern
    function to return a specified pixel color in hsv format.

    Args:
        img (cv2.AsyncArray): image pixels organized as an array.
    """

    def pixel_color(index: int):
        """Function that given a previous array and now a index, returns
        the color or that pixel.

        Args:
            index (int): index from the pixels on the array

        Returns:
            int or tuple: if there's no pixel on that index, returns 0,
            otherwise, returns pixels color.
        """
        if index >= len(img):
            return 0

        else:
            return img[index]

    return pixel_color


if __name__ == "__main__":
    orig_img = cv2.imread("plane.jpg")

    orig_list = cvimg_to_list(orig_img)

    generator = generator_from_image(orig_list)

    new_list = [generator(i) for i in range(len(orig_list))]

    cv2.imshow("original", orig_img)
    cv2.imshow(
        "new", rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1])
    )
    cv2.waitKey(0)
