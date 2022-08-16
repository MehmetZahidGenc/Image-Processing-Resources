import cv2
import numpy as np

def main():

    img = cv2.imread('daisy.jpg')

    # 2D convolution (Image filtering)
    kernel = np.ones((5, 5), np.float) / 25 # we will try an averaging filter on image.
    output_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)


    # Image Blurring (Image Smoothing)

    # 1-) Image Blurring - Averaging
    blurred_img = cv2.blur(src=img, ksize=(3, 3))

    # 2-) Image Blurring - Gaussian Filtering
    blurred_img = cv2.GaussianBlur(src=img, ksize=(3, 3), sigmaX=0)

    # 3-) Image Blurring - Median Filtering
    blurred_img = cv2.medianBlur(src=img, ksize=3)

    # 4-) Image Blurring - Bilateral Filtering
    blurred_img = cv2.bilateralFilter(src=img, d=9, sigmaSpace=75, sigmaColor=75)


if __name__ == '__main__':
    main()