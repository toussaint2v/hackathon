# Import required packages
import cv2
import pytesseract
import sys
def decompose_img(img, imgOrigin):
    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

    # Read image from which text needs to be extracted

    # img = cv2.imread("image/testblanc.png")

    # Preprocessing the image starts

    # Convert the image to gray scale
    gray = img
    cv2.imshow('tzt',gray)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    # imgOrigin = img.copy()



    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    croppedTab = []
    i =0
    for cnt in contours:

        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(imgOrigin, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = imgOrigin[ y:y + h, x:x + w ]

        if (len(pytesseract.image_to_string(cropped)) > 4):
            i += 1
            croppedTab.append(cropped)

    return croppedTab


    """ print(len(croppedTab))
    i = 0
    for e in croppedTab:
        i += 1
        cv2.imshow('test' + str(i), e)

    cv2.waitKey() """

