# import libraries......
import cv2
import numpy as np

img = cv2.imread("frog.png", 1)
# resize image 300x300
img = cv2.resize(img, (300, 300))

# Transpose image
transpose_img = cv2.transpose(img)


# Convert an image from color to grayscale
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Invert a color image and a grayscale image
back_to_rgb = cv2.cvtColor(grayscale, cv2.COLOR_GRAY2RGB)

# Save your results in a directory
cv2.imwrite('resize_img.jpg', img)
cv2.imwrite('transpose_img.jpg', transpose_img)
cv2.imwrite('grayscale.jpg', grayscale)
cv2.imwrite('back_to_rgb.jpg', back_to_rgb)


# Display your results in a horizontal window,
img1 = cv2.imread('resize_img.jpg')
img2 = cv2.imread("transpose_img.jpg")
img3 = cv2.imread("grayscale.jpg")
img4 = cv2.imread("back_to_rgb.jpg")
horizontal_concat = np.concatenate((img1, img2, img3, img4), axis=1)
cv2.imshow("Horizontal plot", horizontal_concat)
cv2.waitKey(500)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

# Capture a video using OpenCV
cap= cv2.VideoCapture(0)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

while True:
    ret,frame= cap.read()
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()