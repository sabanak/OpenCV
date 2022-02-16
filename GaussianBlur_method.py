import cv2
image=cv2.imread('abcd.jpg',1)
gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('image',image)
cv2.imshow('gaussian',gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()