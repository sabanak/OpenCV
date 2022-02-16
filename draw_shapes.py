import cv2
image=cv2.imread('lenaa.jpg',1)
cv2.line(image,(0,0),(400,400),(255,0,0),5)
cv2.rectangle(image,(0,0),(400,400),(255,0,255),4)
cv2.circle(image,(200,200),100,(255,255,0),-1)
font=cv2.FONT_ITALIC
cv2.putText(image,'hello',(100,100),font,4,(255,255,255),cv2.LINE_AA)
cv2.imshow('shapes',image)
cv2.waitKey(0)
cv2.destroyAllWindows()