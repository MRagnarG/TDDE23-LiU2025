import cv2
from lab5a import cvimg_to_list
from cvlib import rgblist_to_cvimg


def generator_from_image (img):

    def pixel_color(i):

        if not img[i]:
            return 0
        
        else:
            return img[i]
        
    return pixel_color


if __name__ == "__main__":
    orig_img = cv2.imread("plane.jpg")
    
    orig_list = cvimg_to_list(orig_img)
    
    generator = generator_from_image(orig_list)
    
    new_list = [generator(i) for i in range(len(orig_list))]
    
    cv2.imshow('original', orig_img)
    cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
    cv2.waitKey(0)