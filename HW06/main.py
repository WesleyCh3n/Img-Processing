import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('IP_dog.bmp')
rows, cols, dims = img.shape
print(rows,cols, dims)
transImg = np.zeros((rows, cols, 3), np.uint8)
### Trapezoidal Transformation
# for y in range(rows):
#     for x in range(cols):
#         transImg[int(3*y/4+x*y/(rows*cols))][int(x+y/4-x*y/(2*rows))] = img[y][x]

### Wavy Transformation
# for y in range(rows):
#     for x in range(cols):
#         x_mod = x+60*np.sin(np.pi/100*y)
#         if x_mod >= rows: x_mod = rows-1
#         elif x_mod < 0: x_mod = 0
#         transImg[int(x_mod)][y] = img[x][y]
# 
# transImg2 = np.zeros((rows, cols, 3), np.uint8)
# for y in range(rows):
#     for x in range(cols):
#         y_mod = y+60*np.sin(np.pi/100*x)
#         if y_mod >= rows: y_mod =  cols-1
#         elif y_mod < 0: y_mod = 0
#         transImg2[x][int(y_mod)] = transImg[x][y]
# plt.subplot(1,2,1), plt.imshow(transImg[:,:,::-1])
# plt.subplot(1,2,2), plt.imshow(transImg2[:,:,::-1])

### Circular Transformation
#xR = rows/2.0
#yR = cols/2.0
#for y in range(cols):
#    for x in range(rows):
#        x_ratio = (x - xR)/xR
#        y_ratio = (y - yR)/yR
#        x_mod = x_ratio * np.sqrt(1 - y_ratio**2/2) * xR + xR
#        y_mod = y_ratio * np.sqrt(1 - x_ratio**2/2) * yR + yR
#        transImg[int(x_mod)][int(y_mod)] = img[x][y]
#plt.imshow(transImg[:,:,::-1])

# plt.savefig('saveImg.png')
plt.show()
