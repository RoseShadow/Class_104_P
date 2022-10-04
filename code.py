import cv2

image= cv2.imread("solar-system.jpg")

cv2.putText(image,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"Mercury",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

output= cv2.imwrite("solar-system.jpg",image)

cv2.imshow(output)
cv2.waitKey(0)