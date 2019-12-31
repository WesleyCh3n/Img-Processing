import matplotlib.pyplot as plt
import cv2

img = cv2.imread('./img.jpg')
# ax = plt.gca()
# fig = plt.gcf()
# implot = ax.imshow(img)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img)

def onclick(event):
    if event.xdata != None and event.ydata != None:
        print(event.xdata, event.ydata)
        plt.plot(event.xdata, event.ydata, '.')
        fig.canvas.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
# plt.draw()

plt.show()

