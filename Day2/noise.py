import cv2
import matplotlib.pyplot as plt
imag=cv2.imread("noise images.jpg")
gaussian=cv2.GaussianBlur(imag,(5,5),0)
plt.imshow(cv2.cvtColor(gaussian,cv2.COLOR_BGR2RGB))
plt.show()