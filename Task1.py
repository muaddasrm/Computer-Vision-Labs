# import libraries......
import cv2
import numpy as np

img=cv2.imread("frog.png",-1)
img=cv2.resize(img,(300,300))

cv2.imshow('sample image', img)

cv2.waitKey(5000)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

