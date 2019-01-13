# import the necessary packages
import numpy as np
import argparse
import cv2


# load the query image, compute the ratio of the old height
# to the new height, clone it, and resize it
cap = cv2.VideoCapture(-1)
while (1):
    _, image = cap.read()
    ratio = image.shape[0] / 300.0
    orig = image.copy()
    #image = cv2.resize(image, (300, 300), interpolation=cv2.INTER_CUBIC)

    # convert the image to grayscale, blur it, and find edges
    # in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    # find contours in the edged image, keep only the largest
    # ones, and initialize our screen contour
    (a, cnts, _) = cv2.findContours(edged.copy(),
                                    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    screenCnt = None
    # loop over our contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if our approximated contour has four points, then
        # we can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break
    try:

        cv2.drawContours(image, [cnts[0]], -1, (0, 255, 0), 3)
        cv2.imshow("Janela", image)
    except:
        print("erros")

    k = cv2.waitKey(30) & 0xff
    if (k == 27):
        break

cv2.destroyAllWindows()
cap.release()
