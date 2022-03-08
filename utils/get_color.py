# source: https://stackoverflow.com/questions/56787999/python-opencv-realtime-get-rgb-values-when-mouse-is-clicked

import cv2
import numpy as np


def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]
        colors = image[y,x]
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)
        print("==================================")


cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

image_path = 'images/cat1.png'
image = cv2.imread(image_path)

scale_percent = 20 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

cv2.imshow('mouseRGB', image)
cv2.waitKey(-1)
cv2.destroyAllWindows()