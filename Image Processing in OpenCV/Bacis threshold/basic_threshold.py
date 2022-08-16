import cv2

def main():
    img = cv2.imread('daisy.jpg', 0)

    # threshold types:
    # THRESH_BINARY, THRESH_BINARY_INV, THRESH_MASK, THRESH_OTSU, THRESH_TOZERO
    # THRESH_TOZERO_INV, THRESH_TRIANGLE, THRESH_TRUNC

    ret, thresh = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

    # Also you can use adaptivethresold
    # types: ADAPTIVE_THRESH_MEAN_C, ADAPTIVE_THRESH_GAUSSIAN_C
    thresh = cv2.adaptiveThreshold(src=img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=11, C=2)


    # Otsu binarization
    ret, thresh = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)

if __name__ == '__main__':
    main()