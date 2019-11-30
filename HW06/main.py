import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('IP_dog.bmp')
plt.imshow(img[:,:,::-1])
plt.show()