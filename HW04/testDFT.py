import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C1HW04_IMG01_2019.jpg',0)
print(f"This is input shape {img.shape}")
dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
print(f"This is dft shape {dft.shape}")
print(dft)
dft_shift = np.fft.fftshift(dft)
print(f"This is dft_shift shape {dft_shift.shape}")
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
print(f"This is magnitude_spectrum shape {magnitude_spectrum.shape}")

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()