import cv2
import numpy as np
import pywt
import matplotlib.pyplot as plt

img1 = cv2.imread("clock1.JPG", 0)
img2 = cv2.imread("clock2.JPG", 0)
min_len = min(img1.shape)
img1 = cv2.resize(img1, (min_len, min_len))
img2 = cv2.resize(img2, (min_len, min_len))

coeff1 = pywt.dwt2(img1, 'db')
coeff2 = pywt.dwt2(img2, 'db')

ca1,(ch1,cv1,cd1) = coeff1
ca2,(ch2,cv2,cd2) = coeff2

ca = (ca1 + ca2)/2
ch = np.maximum(ch1, ch2)
cv = np.maximum(cv1, cv2)
cd = np.maximum(cd1, cd2)
coeff = ca, (ch, cv, cd)
resultImg = pywt.idwt2(coeff, 'haar').astype(np.uint8)
resultImg = np.repeat(resultImg[:, :, np.newaxis], 3, axis=2)
print(resultImg)
print(resultImg.shape)
plt.imshow(resultImg)
plt.show()
