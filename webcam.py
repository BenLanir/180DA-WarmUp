"""
Most of this code is based on the following tutorial to create a mask for one color: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
The other source I used was this tutorial for bounding boxes: https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

I changed the colors from HSV to BGR because it worked better for me and found a range in BGR


"""
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    #hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])

    lower_blue = np.array([150,0,0])
    upper_blue = np.array([255,100,100])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(frame, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    res_gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)

    x, y, w, h = cv.boundingRect(res_gray)

    cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()