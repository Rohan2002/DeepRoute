import numpy as np
import cv2

# https://stackoverflow.com/a/38982869/10016132
def sharpen_image(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    im = cv2.filter2D(img, -1, kernel)
    return im
