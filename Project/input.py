import pytesseract
from pytesseract import Output
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

img = cv2.imread('./test.jpg')
# text = pytesseract.image_to_string(img, lang='eng')
# print(text)

# d = pytesseract.image_to_boxes(img, lang='eng', output_type=Output.DATAFRAME)
# print(type(d))

# d = pytesseract.image_to_data(img, output_type=Output.DATAFRAME)
# d.to_csv('./word.csv', index=False)

'''Bounding box'''
# df = pd.read_csv('./word.csv')
# df['text'].replace('', np.nan, inplace=True)
# print(df)
# df.dropna(subset=['text'], inplace=True)
# print(df['level'].iloc[1])
# for i in range(len(df['level'])):
#     (x, y, w, h) = (df['left'].iloc[i], df['top'].iloc[i], df['width'].iloc[i], df['height'].iloc[i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

'''Bounding box'''
# pdf = pytesseract.image_to_pdf_or_hocr(img, lang='eng')
# f = open("demofile.pdf", "w+b")
# f.write(bytearray(pdf))
# f.close()

'''Put text on new image'''
# df = pd.read_csv('./word.csv')
# df['text'].replace('', np.nan, inplace=True)
# df.dropna(subset=['text'], inplace=True)

print(img.shape)
# newImg = np.ones(img.shape, np.uint8) * 255
# for i in range(len(df['level'])):
#     (x, y, w, h) = (df['left'].iloc[i], df['top'].iloc[i], df['width'].iloc[i], df['height'].iloc[i])
#     cv2.putText(newImg, str(df['text'].iloc[i]), (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,0,0), 1, cv2.LINE_AA)

# plt.imshow(cv2.cvtColor(newImg, cv2.COLOR_BGR2RGB))
# plt.show()

'''PDF output'''
df = pd.read_csv('./word.csv')
df['text'].replace('', np.nan, inplace=True)
df.dropna(subset=['text'], inplace=True)
# (x, y, w, h) = (df['left'].iloc[0], df['top'].iloc[0], df['width'].iloc[0], df['height'].iloc[0])
# print(x, y, w, h)

from fpdf import FPDF
pdf = FPDF('P','pt','A4')
pdf.add_page()
pdf.set_font('Arial', '', 12)
for i in range(len(df['level'])):
    (x, y, w, h) = (df['left'].iloc[i], df['top'].iloc[i], df['width'].iloc[i], df['height'].iloc[i])
    pdf.set_xy(x, y)
    pdf.cell(w, h, df['text'].iloc[i], ln=2)
pdf.output('tes.pdf')
