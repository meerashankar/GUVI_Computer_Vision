import cv2
import matplotlib.pyplot as plt
imag=cv2.imread("images.jpg")
gray=cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
threshold,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
hist=cv2.calcHist(gray,[0],None,[256],[0,256])
#plt.imshow(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))
plt.plot(hist)
plt.show()

