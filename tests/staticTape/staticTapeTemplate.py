import numpy as np
import cv2
from matplotlib import pyplot as plt
import pprint
import math

# based on http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html


vision = False
# i pokud neni zaple vision, musi se hledat hned i prvni centrovaci kolecko, aby se dala vision zapnout i pozdeji


w = 8 # width of the tape in mm
p0 = 4 # pitch of sprocket holes on the tape in mm
p1 = 4 # pitch between parts
a0 = 1.2 # component size in X direction
b0 = 0.8 # component size in Y direction

tapeOrientation = 2 # 0-left X-, 1-top/back Y+, 2-right X+, 3-bottom/front Y-
pin1 = 'A' # pin 1 quadrant: Top, A, B, C, D

partCount = 4 # how many patrs the tape has.
partIndex = 1 # set the incremental index to 1 = 1st part in the tape

if vision is True:
	print('Top Vision: On')

else:
	print('Top Vision: Off')

#25,463 1st component

firstPartPos = (87,258) # normally determined by user by clicking into the image.
currentPartPos =  (0,0) 
previousPartPos = firstPartPos

#===============================================================================


img = cv2.imread('tape3.png',0) # CCD image
img2 = cv2.medianBlur(img, 5)

#img2 = cv2.Canny(img,20,330)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cimg2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)


crossColor = (255,0,0)
crossThickenss = 2	



minDist = 30 # min distance between circles centers. Low enough value can even find circle inside circle. But it generates so many circles(useless). High value on the other side generate smaller amount of circles, but can miss the right one. So the strategy for PCB fiducials will be: Corp the CCD image only to small area where fiducial is expected. Use lower minDist value

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist,
                            param1=50,param2=30,minRadius=20,maxRadius=45)

circles2 = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,minDist,
                            param1=50,param2=30,minRadius=20,maxRadius=45)


circles = np.uint16(np.around(circles))



#show all patrs positions

print ('1st part on firstPartPos')
# draw the crosshair
cv2.line(cimg2, (firstPartPos[0]-25, firstPartPos[1]), (firstPartPos[0]+25, firstPartPos[1]), crossColor,crossThickenss) # horizontal line
cv2.line(cimg2, (firstPartPos[0], firstPartPos[1]-30), (firstPartPos[0], firstPartPos[1]+30), crossColor,crossThickenss) # vertical line



for x in range(2,partCount+1):


	if tapeOrientation == 0:
		currentPartPos = (previousPartPos[0]-123, previousPartPos[1])
	elif tapeOrientation == 1:
		currentPartPos = (previousPartPos[0], previousPartPos[1]+123)
	elif tapeOrientation == 2:
		currentPartPos = (previousPartPos[0]+123, previousPartPos[1])
	elif tapeOrientation == 3:
		currentPartPos = (previousPartPos[0], previousPartPos[1]-123)

	previousPartPos = currentPartPos
	print "Part %d is on pos X: %d Y: %d" % (x, currentPartPos[0], currentPartPos[1])

    	# draw the crosshair
    	cv2.line(cimg2, (currentPartPos[0]-25, currentPartPos[1]), (currentPartPos[0]+25, currentPartPos[1]), crossColor,crossThickenss) # horizontal line
    	cv2.line(cimg2, (currentPartPos[0], currentPartPos[1]-30), (currentPartPos[0], currentPartPos[1]+30), crossColor,crossThickenss) # vertical line




'''

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle( cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the crosshair
    cv2.line(cimg, (i[0]-25, i[1]), (i[0]+25, i[1]), crossColor,crossThickenss) # horizontal line
    cv2.line(cimg, (i[0], i[1]-25), (i[0], i[1]+25), crossColor,crossThickenss) # vertical line
'''

#pprint.pprint(circles)

'''
circles2 = np.uint16(np.around(circles2))
for i in circles2[0,:]:
    # draw the outer circle
    cv2.circle( cimg2,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the crosshair
    cv2.line(cimg2, (i[0]-25, i[1]), (i[0]+25, i[1]), crossColor,crossThickenss) # horizontal line
    cv2.line(cimg2, (i[0], i[1]-25), (i[0], i[1]+25), crossColor,crossThickenss) # vertical line
'''
#pprint.pprint(circles2)




fig = plt.figure()

#f1 = fig.add_subplot(221)
#f1.set_title('1. original')
#f1.imshow(img) 

f2 = fig.add_subplot(121)
f2.set_title('2. medianBlur')
f2.imshow(img2)

#f3 = fig.add_subplot(223)
#f3.set_title('3. circles')
#f3.imshow(cimg)  

f4 = fig.add_subplot(122)
f4.set_title('4. circles blur')
f4.imshow(cimg2)  


#plt.imshow(img, 'gray'),plt.imshow(img2, 'gray'),
plt.show()

