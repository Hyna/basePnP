import numpy as np
import cv2
from matplotlib import pyplot as plt
import pprint
import math
import pprint
# based on http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html



#img1 = cv2.imread('IC_template2.png',0) # template
img = cv2.imread('/home/hyna/Diplomka/sw/basePnP/doc/mereni/fiducials/fiduc_svetlostrop_crop.png',0) # CCD image
img2 = cv2.medianBlur(img, 5)
#pprint.pprint(img) # check -  img is none fue to wrong path or type. eg. jpg.

#img2 = cv2.Canny(img,20,330)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cimg2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)


crossColor = (255,0,0)
crossThickenss = 1



minDist = 150 # min distance between circles centers. Low enough value can even find circle inside circle. But it generates so many circles(useless). High value on the other side generate smaller amount of circles, but can miss the right one. So the strategy for PCB fiducials will be: Corp the CCD image only to small area where fiducial is expected. Use lower minDist value


circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist, param1=50,param2=30,minRadius=10,maxRadius=30)


circles2 = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,minDist, param1=50,param2=30,minRadius=5,maxRadius=30)


circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle( cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the crosshair
    cv2.line(cimg, (i[0]-25, i[1]), (i[0]+25, i[1]), crossColor,crossThickenss) # horizontal line
    cv2.line(cimg, (i[0], i[1]-25), (i[0], i[1]+25), crossColor,crossThickenss) # vertical line


pprint.pprint(circles)


circles2 = np.uint16(np.around(circles2))
for i in circles2[0,:]:
    # draw the outer circle
    cv2.circle( cimg2,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the crosshair
    cv2.line(cimg2, (i[0]-25, i[1]), (i[0]+25, i[1]), crossColor,crossThickenss) # horizontal line
    cv2.line(cimg2, (i[0], i[1]-25), (i[0], i[1]+25), crossColor,crossThickenss) # vertical line

#pprint.pprint(circles2)


fig = plt.figure()

f1 = fig.add_subplot(221)
f1.set_title('1. original')
f1.imshow(img) 

f2 = fig.add_subplot(222)
f2.set_title('2. medianBlur')
f2.imshow(img2, cmap='gray',vmin=0,vmax=255)

f3 = fig.add_subplot(223)
f3.set_title('3. circles')
f3.imshow(cimg)  

f4 = fig.add_subplot(224)
f4.set_title('4. circles blur')
f4.imshow(cimg2)  


#plt.imshow(img, 'gray'),plt.imshow(img2, 'gray'),
plt.show()
