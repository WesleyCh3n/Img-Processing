import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('rects.bmp', 0)
edgesImg = cv2.Canny(img ,50,150,apertureSize = 3) 
lines = cv2.HoughLinesP(edgesImg, 1,np.pi/360, 50,  None , 50, 10)
numbers, dummy, points = lines.shape
for x1, y1, x2, y2 in lines.reshape((numbers,points)):
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),5)
    print(x1, y1, x2, y2)
    cv2.putText(img, f"{np.sqrt((x1-x2)**2+(y1-y2)**2):.2f}", (int(round((x2+x1)/2)), int(round((y1+y2)/2))), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255,255,255), 1, cv2.LINE_AA)
plt.imshow(img)
plt.show()
