import numpy as np
import cv2
import argparse
from collections import deque

cap = cv2.VideoCapture(0) #Capture video through webcam
pts = deque(maxlen=64) #Points where object has visited
lwr_blue = np.array([110,50,50]) #Lower bound of hsv color to detect
upper_blue = np.array([130,255,255]) #Upper bound of hsv color to detect
while True:
    ret,frame =cap.read()  #Capture frame-by-frame
    frame = cv2.flip(frame,1) #Flipping the frame across y-axis
    #Converting from BGR to HSV
    hsv =  cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Making kernel (a 5x5 matrix)
    kernel=np.ones((5,5),np.uint8)
    #Constructing a mask for blue color and then applying a series of dilation and erosion
    mask=cv2.inRange(hsv,lwr_blue,upper_blue)
    mask = cv2.erode(mask,kernel, iterations=2)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)
    res=cv2.bitwise_and(frame,frame,mask=mask)
	#Finding the contours in the mask and intializing the center as "None"
    _,cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None
	#In case when it detects at least one contour
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)  #Finding the largest contour in the mask
        ((x, y), radius) = cv2.minEnclosingCircle(c)  #Finding the minimum enclosing circle
        M = cv2.moments(c)  #Calculating image moment(center of mass)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) #Centroid of the minimum enclosing circle
        if radius > 5:
            cv2.circle(frame, (int(x), int(y)), int(radius),(255,255,255), 2)  #Drawing a circle of thickness 2
            cv2.circle(frame, center, 5, (226, 43, 138), -1) #Drawing centroid on the frame

    pts.appendleft(center) #Appending the center to the left of deque
    for i in np.arange(1,len(pts)):
        #print(pts) #to check
        if pts[i-1]is None or pts[i] is None: #If either the current or previous point is "None" i.e. pen isn't detected in the frame
            continue
        thick = int(np.sqrt(len(pts) / float(i + 1))) #Computing the thickness of the line to be drawn
        #print("thick=",thick) #to check
        #print(points[i-1],points[i]) #to check
        cv2.line(frame, pts[i-1],pts[i],(223,70,70),thick) #Drawing the line

    #To display
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    cv2.imshow("Frame",frame)

    key=cv2.waitKey(30) & 0xFF
    if key==32:  #On hitting spacebar(To exit)
        break
#Cleanup the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
