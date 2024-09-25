#importation de bibliotheque

import cv2
import numpy as np

#ouvrir une fenetre pour fixer les valeur de mask

def traitement(img):
    pass
video=cv2.VideoCapture (0)
cv2.namedWindow("TrackBar")
cv2.createTrackbar("hue_min_red","TrackBar",0,255,traitement)
cv2.createTrackbar("hue_max_red","TrackBar",255,255,traitement)
cv2.createTrackbar("sat_min_red","TrackBar",0,255,traitement)
cv2.createTrackbar("sat_max_red","TrackBar",255,255,traitement)
cv2.createTrackbar("val_min_red","TrackBar",0,255,traitement)
cv2.createTrackbar("val_max_red","TrackBar",255,255,traitement)
cv2.createTrackbar("hue_min_green","TrackBar",0,255,traitement)
cv2.createTrackbar("hue_max_green","TrackBar",255,255,traitement)
cv2.createTrackbar("sat_min_green","TrackBar",0,255,traitement)
cv2.createTrackbar("sat_max_green","TrackBar",255,255,traitement)
cv2.createTrackbar("val_min_green","TrackBar",0,255,traitement)
cv2.createTrackbar("val_max_green","TrackBar",255,255,traitement)

#programme principale

while(True):
    ret, img=video.read()
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min_red=cv2.getTrackbarPos("hue_min_red","TrackBar")
    hue_max_red=cv2.getTrackbarPos("hue_max_red","TrackBar")
    sat_min_red=cv2.getTrackbarPos("sat_min_red","TrackBar")
    sat_max_red=cv2.getTrackbarPos("sat_max_red","TrackBar")
    val_min_red=cv2.getTrackbarPos("val_min_red","TrackBar")
    val_max_red=cv2.getTrackbarPos("val_max_red","TrackBar")
    hue_min_green=cv2.getTrackbarPos("hue_min_green","TrackBar")
    hue_max_green=cv2.getTrackbarPos("hue_max_green","TrackBar")
    sat_min_green=cv2.getTrackbarPos("sat_min_green","TrackBar")
    sat_max_green=cv2.getTrackbarPos("sat_max_green","TrackBar")
    val_min_green=cv2.getTrackbarPos("val_min_green","TrackBar")
    val_max_green=cv2.getTrackbarPos("val_max_green","TrackBar")
    lower_red=np.array([hue_min_red, sat_min_red, val_min_red])
    upper_red=np.array([hue_max_red, sat_max_red, val_max_red])
    lower_green=np.array([hue_min_green, sat_min_green, val_min_green])
    upper_green=np.array([hue_max_green, sat_max_green, val_max_green])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    cnts_red, hei = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
    cnts_green, hei = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in cnts_red:
        area = cv2.contourArea(c)
        if area>300:
            peri=cv2.arcLength(c,True)
            approx=cv2.approxPolyDP(c, 0.02*peri,True)
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            if len(approx) ==4:
                cv2.putText(img, "Rectangle", (x+w+20, y+h), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(img, "red", (x + w + 20, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
            else:
                cv2.putText(img, "Circle", (x + w + 20, y + h), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(img, "red", (x + w + 20, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0, 255), 2)
        for c in cnts_green:
            area = cv2.contourArea(c)
            if area>300:
                peri=cv2.arcLength(c,True)
                approx=cv2.approxPolyDP(c, 0.02*peri,True)
                x,y,w,h=cv2.boundingRect(c)
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                if len(approx) ==4:
                    cv2.putText(img, "Rectangle", (x+w+20, y+h), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                    cv2.putText(img, "green", (x + w + 20, y + h+20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                else:
                    cv2.putText(img, "Circle", (x + w + 20, y + h), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                    cv2.putText(img, "green", (x + w + 20, y + h+20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("frame",img)
    cv2.imshow("Mask_red",mask_red)
    cv2.imshow("Mask_green", mask_green)
    k=cv2.waitKey(1)
    if k==ord ('q'):
        break
video.release()
cv2.destroyAllWindows()