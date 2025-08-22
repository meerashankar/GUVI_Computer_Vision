
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=np.zeros((500,500),dtype=np.uint8)
rect=cv2.rectangle(img,(50,50),(100,100),(255,255))
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()