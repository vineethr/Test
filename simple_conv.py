import cv2
import numpy as np
img=cv2.imread('Ironman.jpg')
Kernal=np.array([[0,-1,0],[-1,4,-1],[0,1,0]])
convolved=cv2.filter2D(img,-1,Kernal)
cv2.imshow('original',img)
cv2.imshow('convolved',convolved)
cv2.waitKey(0)
cv2.destroyAllWindows()

