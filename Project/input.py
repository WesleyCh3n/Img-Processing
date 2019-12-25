import pytesseract
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./test.jpg')
text = pytesseract.image_to_string(img, lang='eng')
print(text)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
