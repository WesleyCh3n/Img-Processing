import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('rects.bmp', 0)
print(img.shape)
edgesImg = cv2.Canny(img ,50,150,apertureSize = 3) 
lines = cv2.HoughLinesP(edgesImg, 1,np.pi/360,60, 74.46, 10)
numbers, dummy, points = lines.shape
for x1, y1, x2, y2 in lines.reshape((numbers,points)):
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),10)
print(lines.shape)
plt.imshow(img)
plt.show()
