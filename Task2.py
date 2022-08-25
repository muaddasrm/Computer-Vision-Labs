# import libraries......
import cv2
import numpy as np

img = cv2.imread("frog.png", 0)
img = cv2.resize(img, (300, 300))

# Apply laplacian filter....
laplacian = cv2.Laplacian(img,cv2.CV_64F)

# Apply Prewitt (horizontal,vertical) filter....
kernelX=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernelY=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
prewittx=cv2.filter2D(img,-1,kernelX)
prewitty=cv2.filter2D(img,-1,kernelY)


# Apply Sobel (horizontal,vertical) filter....
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

# Apply average filter....
average = cv2.blur(img,(5,5))


cv2.imwrite('Task2_images/laplacian.jpg', laplacian)
cv2.imwrite('Task2_images/prewittx.jpg', prewittx)
cv2.imwrite('Task2_images/prewitty.jpg', prewitty)
cv2.imwrite('Task2_images/sobelx.jpg', sobelx)
cv2.imwrite('Task2_images/sobely.jpg', sobely)
cv2.imwrite('Task2_images/average.jpg', average)


# Display your results in a horizontal window,
img1 = cv2.imread('Task2_images/laplacian.jpg')
img2 = cv2.imread('Task2_images/prewittx.jpg')
img3 = cv2.imread('Task2_images/prewitty.jpg')
img4 = cv2.imread('Task2_images/sobelx.jpg')
img5 = cv2.imread('Task2_images/sobely.jpg')
img6 = cv2.imread('Task2_images/average.jpg')
horizontal_concat = np.concatenate((img1, img2, img3, img4,img5,img6), axis=1)
cv2.imshow("Horizontal plot", horizontal_concat)
cv2.waitKey(5000)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image
