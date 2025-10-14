import cv2
from lab5a import cvimg_to_list
from cvlib import greyscale_list_to_cvimg


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):

    def is_in_interval(pixel):
        (h,s,v) = pixel
        if hlow<= h <= hhigh and slow<= s <= shigh and vlow<= v <= vhigh:
            return 1
        else:
            return 0
    
    return is_in_interval

if __name__ == "__main__":
    hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
    plane_list = cvimg_to_list(hsv_plane)
    
    is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))
    
    cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
    cv2.waitKey(0)

