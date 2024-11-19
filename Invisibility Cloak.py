# Import Libraries
import numpy as np
import cv2
import time

# To use webcam enter 0 and enter the video path in double-quotes.

cap = cv2.VideoCapture(0)
time.sleep(2)     
background = 0

# In the time function, we have used the value so that the video 
# can be captured in the first 2 seconds after running the program.

# Capturing the Image of the background in the first two seconds.

for i in range(50):
    ret, background = cap.read()

# Capturing the video feed using Webcam

while(cap.isOpened()): 
    ret, img = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
#Setting the values for the cloak and making masks and all this Comes in the while loop

    # HSV range for black color
    lower_black = np.array([0, 0, 0])        # Lower bound for black
    upper_black = np.array([180, 255, 50])   # Upper bound for black
    mask1 = cv2.inRange(hsv, lower_black, upper_black)


#Combining the masks so that It can be viewd as in one frame
    # mask1 = mask1 +mask2
#After combining the mask we are storing the value in deafult mask.

# Using Morphological Transformations to remove noise from the cloth and unnecessary Details.

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)

    mask2 =cv2.bitwise_not(mask1)

# Combining the masks and showing them in one frame

    res1 = cv2.bitwise_and(background,background,mask=mask1)
 
#The basic work of bitwise_and is to combine these background and store it in res1

    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Invisible Cloak',final_output)
    k = cv2.waitKey(10)
    if k==27:
        break
    
cap.release()
cv2.destroyAllWindows()
