import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('./img.jpg')
originalImg = np.copy(img)
print(img.shape) # 1108, 1478

cv2.circle(img, (428, 170), 10, (0, 0, 255), -1)
cv2.circle(img, (1029, 206), 10, (0, 0, 255), -1)
cv2.circle(img, (143, 1027), 10, (0, 0, 255), -1)
cv2.circle(img, (1347, 1028), 10, (0, 0, 255), -1)

pt1 = np.float32([[428, 170],[1029, 206],[143, 1027],[1347, 1028]])
pt2 = np.float32([[-1,0],[2480,0],[0,3508],[2480,3508]])
matrix = cv2.getPerspectiveTransform(pt1, pt2)
print(matrix)
result = cv2.warpPerspective(originalImg, matrix,(2480,3508))

edge = cv2.Canny(originalImg, 50, 150, apertureSize = 3)
print(edge.shape)

plt.subplot(1,2,1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.subplot(1,2,2), plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('After Wrapping')
plt.show()

