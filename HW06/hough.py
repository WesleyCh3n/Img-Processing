import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('rects.bmp', 0)
print(img.shape)
edgesImg = cv2.Canny(img ,50,150,apertureSize = 3) 
plt.imshow(edgesImg , cmap='gray')
plt.show()
