#from SimpleCV import Camera
import numpy as np
import cv2
import time

camera_port=0
camera = cv2.VideoCapture(0)

#cam = Camera()
time.sleep(0.1)
return_value, image1 = camera.read()
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

time.sleep(1)

return_value2, image2 = camera.read()
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

(thresh1, im_bw1) = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print thresh1
#thresh1 = 127
im_bw1 = cv2.threshold(image1, thresh1, 255, cv2.THRESH_BINARY)[1]
(thresh2, im_bw2) = cv2.threshold(image2, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print thresh2
#thresh2 = 127
im_bw2 = cv2.threshold(image2, thresh2, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite("p1.tiff", im_bw1)
cv2.imwrite("p2.tiff", im_bw2)


#a = cam.getImage()
a = cv2.imread("p1.tiff")
#time.sleep(1)
#b = cam.getImage()
b = cv2.imread("p2.tiff")

#d = image1 - image2

d = b-a

cv2.imwrite("diff.png", d)
#mat = d.getNumpy()
#avg = mat.mean()
#avg = d.mean()

print(abs(d.mean()))

if abs(d.mean()) > 2:
    print("Motion Detected")
else:
    print("No Motion")
