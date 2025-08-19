import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image.jpg")
rows,cols=img.shape[:2]
(h, w) = img.shape[:2]

flipped = cv2.flip(img, 1)

cropped = img[50:100,100:300]

resize = cv2.resize(img,(200,400))

M = np.float32([[1,0,-10],[0,1,0]])
translate = cv2.warpAffine(img,M,(cols,rows))

RM = cv2.getRotationMatrix2D((w//2,h//2),45,1.0)
rotated = cv2.warpAffine(img, RM, (w,h))

scaled = cv2.resize(img,None,fx=2,fy=2)

line = cv2.line(img, (50,50), (200,50),(0,255,0),2)

rect = cv2.rectangle(img,(20,20),(50,70),(255,0,0),1)

circle = cv2.circle(img,(30,30),50,(0,0,255),2)
cv2.putText(img,"Open CV",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
plt.imshow(cv2.cvtColor(translate ,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

cv2.imwrite("output.jpeg",img)