# Load the required libraries
import numpy as np
import cv2

# Make a dummy function to be used with 'Taskbar' creation
def dummy(val):
	pass

# Define all the kernels to be used with the filter functionality
identity_kernal=np.array([[0,0,0],[0,1,0],[0,0,0]])
sharpen_kernel=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
#gaussian_kernel=np.array([[1,2,1],[2,4,2],[1,2,1]],np.float32)/16
gaussian_kernel_1=cv2.getGaussianKernel(3,0)
gaussian_kernel_2=cv2.getGaussianKernel(5,0)
box_kernel=np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)/9

# Make a list of all the kernels so that they can be accessed using indices
kernals=[identity_kernal,sharpen_kernel,gaussian_kernel_1,gaussian_kernel_2,box_kernel,sharpen_kernel]

# Load the original image and make a copy of itso that we do not modify the original one.
color_original=cv2.imread('Ironman.jpg')
color_modified=color_original.copy()

# Similarly create a copy of the original gray scale image 
gray_original=cv2.cvtColor(color_original,cv2.COLOR_BGR2GRAY)
gray_modified=gray_original.copy()

# Create a window to add all the buttons and taskbars. Set the range over which taskbar values can be varied
cv2.namedWindow('app')
cv2.createTrackbar('contrast','app',1,100,dummy)
cv2.createTrackbar('brightness','app',50,100,dummy)
cv2.createTrackbar('filter','app',0,len(kernals)-1,dummy)
cv2.createTrackbar('grayscale','app',0,1,dummy)


count=1	# Counter to save modified images

# Create the loop over which the program will monitor any change to the taskbars made by the user
while True:
# Show the original image and make modifications on the original image if grayscale is 0 else use the grayscale image
	grayscale=cv2.getTrackbarPos('grayscale','app')
	if grayscale==0:
		cv2.imshow('app',color_modified)
	else:	
		cv2.imshow('app',gray_modified)	

# Wait for any key to be pressed and if the key matches the expected input, then perform the required operations	
	k=cv2.waitKey(1) & 0xFF
	if k == ord('q'):	# Press 'q' to quit
		break
	elif k==ord('s'):	# Press 's' to save
		if grayscale==0:
			cv2.imwrite('Ironman_modified%d.png'%count,color_modified)	
		else:
			cv2,imwrite('Ironman_modified%d.png'%count,gray_modified)
		count=count+1	
# Get the trackbar position updates made by the user
	contrast=cv2.getTrackbarPos('contrast','app') 
	brightness=cv2.getTrackbarPos('brightness','app')
	kernel=cv2.getTrackbarPos('filter','app')
		
# Apply the filters to the color image as well as the color image
	color_modified=cv2.filter2D(color_original,-1,kernals[kernel])	
	gray_modified=cv2.filter2D(gray_original,-1,kernals[kernel])	
		
# Apply the contrast and brightness to the original and gray image 
	color_modified=cv2.addWeighted(color_modified,contrast,np.zeros(color_original.shape,dtype=color_original.dtype),0,brightness-50)
	gray_modified=cv2.addWeighted(gray_modified,contrast,np.zeros(gray_original.shape,dtype=gray_original.dtype),0,brightness-50)

# Once everything is performed, close  all the windows
cv2.destroyAllWindows()

