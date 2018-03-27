import cv2
import numpy as np
img=cv2.imread('Ironman.jpg')
cb_img=cv2.addWeighted(img, 4, np.zeros(img.shape,dtype=img.dtype), 0, 100)
cv2.imshow('img', cb_img)
cv2.waitKey(0)
cv2.destroyAllWindow()

