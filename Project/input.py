import pytesseract
import cv2

img = cv2.imread('./test.jpg')
text = pytesseract.image_to_string(img, lang='eng')
print(text)
