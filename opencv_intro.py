import cv2
img=cv2.imread('Ironman.jpg')
if img is None:
	print('Image is not loaded')
else:
	print('Image loaded')
cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)

