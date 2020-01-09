import pytesseract
from pytesseract import Output
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

img = cv2.imread('./test.jpeg')
print(img.shape)
# text = pytesseract.image_to_string(img, lang='eng')
# print(text)

df = pytesseract.image_to_data(img, output_type=Output.DATAFRAME)
# d.to_csv('./word.csv', index=False)

'''Bounding box'''
# df = pd.read_csv('./word.csv')
df['text'].replace('', np.nan, inplace=True)
print(df)
df.dropna(subset=['text'], inplace=True)
print(df['level'].iloc[1])
for i in range(len(df['level'])):
    (x, y, w, h) = (df['left'].iloc[i], df['top'].iloc[i], df['width'].iloc[i], df['height'].iloc[i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

'''Bounding box'''
# pdf = pytesseract.image_to_pdf_or_hocr(img, lang='eng')
# f = open("demofile.pdf", "w+b")
# f.write(bytearray(pdf))
# f.close()

'''Put text on new image'''
# df = pd.read_csv('./word.csv')
# df['text'].replace('', np.nan, inplace=True)
# df.dropna(subset=['text'], inplace=True)

# newImg = np.ones(img.shape, np.uint8) * 255
# for i in range(len(df['level'])):
#     (x, y, w, h) = (df['left'].iloc[i], df['top'].iloc[i], df['width'].iloc[i], df['height'].iloc[i])
#     cv2.putText(newImg, str(df['text'].iloc[i]), (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,0,0), 1, cv2.LINE_AA)

# plt.imshow(cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB))
# plt.show()

'''PDF output'''
# df = pd.read_csv('./word.csv')
# df = pytesseract.image_to_data(img, output_type=Output.DATAFRAME)
# df['text'].replace('', np.nan, inplace=True)
# df.dropna(subset=['text'], inplace=True)
# print(df)
# for i in range(len(df['level'])):
#     (x, y, w, h) = (df['left'].iloc[i], df['top'].iloc[i], df['width'].iloc[i], df['height'].iloc[i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

# from fpdf import FPDF
# pdf = FPDF('P','pt','A4')
# pdf.add_page()
# pdf.add_font('Times', '', './times-new-roman.ttf', uni=True)
# pdf.set_font('Times', '', 10)
# for i in range(len(df['level'])):
#     (x, y, w, h) = (df['left'].iloc[i], df['top'].iloc[i], df['width'].iloc[i], df['height'].iloc[i])
#     pdf.set_xy(x*(595/2479), y*(842/3580))
#     pdf.cell(0, 0, df['text'].iloc[i])
# pdf.output('tes2.pdf')
