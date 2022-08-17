import cv2
import numpy as np
from matplotlib import pyplot as plt

"""

Fourier Transform   ---  Created by Mehmet Zahid Genç

"""

# Low-pass Filters

def lowpass_filter(fourier_spectrogram, ksize):
    h, w = fourier_spectrogram.shape[:2]

    center_h, center_w = int(h/2), int(w/2)

    mask_img = np.zeros((h, w), np.uint8)
    mask_img[center_h-int(ksize / 2):center_h+int(ksize / 2), center_w-int(ksize / 2):center_w+int(ksize / 2)] = 1

    result = mask_img * fourier_spectrogram

    return result

# High-pass Filters

def highpass_filter(fourier_spectrogram, ksize):
    h, w = fourier_spectrogram.shape[:2]

    center_h, center_w = int(h / 2), int(w / 2)

    fourier_spectrogram[center_h-int(ksize / 2):center_h+int(ksize / 2), center_w-int(ksize / 2):center_w+int(ksize / 2)] = 0

    return fourier_spectrogram


# Fourier Transform

def fourier_transform(image, Ftype, ksize=250):
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        pass

    # fourier transform
    img_dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(img_dft)

    if Ftype == 'lowpass':
        # low pass filter
        dft_shift = lowpass_filter(dft_shift, ksize)

    if Ftype == 'highpass':
        # high pass filter
        dft_shift = highpass_filter(dft_shift, ksize)

    # Inverse fourier transform
    inverse_dft_shift = np.fft.ifftshift(dft_shift)
    inverse_fimg = np.fft.ifft2(inverse_dft_shift)
    inverse_fimg = np.abs(inverse_fimg)

    return np.int8(inverse_fimg)


def main():
    image = cv2.imread('daisy.jpg')

    result_image = fourier_transform(image, ksize=50, Ftype='highpass') # You can change ksize as you want. Ftype = highpass and lowpass

    plt.title('result')
    plt.imshow(result_image, cmap='gray')
    plt.show()

if __name__ == '__main__':
    main()