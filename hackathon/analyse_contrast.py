from skimage.exposure import is_low_contrast
from imutils.paths import list_images
import argparse
import imutils
import cv2
import numpy as np

from skimage.util.dtype import dtype_range, dtype_limits
from skimage._shared import utils
from skimage.color import rgb2gray, rgba2rgb

percent = 0
#debut de la fonction qui renvoi le contrast
def contrast(image, fraction_threshold=0.05, lower_percentile=1, upper_percentile=99, method='linear'):
    image = np.asanyarray(image)

    if image.dtype == bool:
        return not ((image.max() == 1) and (image.min() == 0))
    if image.ndim == 3:
        if image.shape[2] == 4:
            image = rgba2rgb(image)
        if image.shape[2] == 3:
            image = rgb2gray(image)

    dlimits = dtype_limits(image, clip_negative=False)
    limits = np.percentile(image, [lower_percentile, upper_percentile])
    ratio = (limits[1] - limits[0]) / (dlimits[1] - dlimits[0])
    global percent
    percent = ratio
    return ratio < fraction_threshold

#fin de la fonction qui renvoi le contrast


def pourcentage_de_contrast(image):
    ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--input", required = True)

    ap.add_argument("-t", "--thresh", type=float, default=0.35, help="threshold for low contrast" )
    args= vars(ap.parse_args())


    image = imutils.resize(image, width=450)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    contrast(gray, fraction_threshold=args["thresh"])

    return round((percent * 100),2)

    #cv2.imshow("Image", image)
    #cv2.imshow("Edge", edged)
    #cv2.waitKey(0)

    #print (round((percent100),2))

