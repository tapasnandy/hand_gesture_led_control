import cv2
from cvzone.SerialModule import SerialObject
from time import sleep
import handTrackingModule as ht
import math


"""arduino = SerialObject()


while True:
    
    arduino.sendData([1])
    sleep(2)
    arduino.sendData([0])
    sleep(2)
    
"""
cap = cv2.VideoCapture(0)
detector = ht.handDetector(detectionCon = 0.7)
arduino = SerialObject("COM3")
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    handlist = detector.findPosition(img, draw = False)
    if len(handlist) != 0:

        x1 , y1= handlist[4][1], handlist[4][2]
        x2 , y2= handlist[8][1], handlist[8][2]
        
        cv2.circle(img, (x1,y1), 8, (0,255,0), cv2.FILLED)
        cv2.circle(img, (x2,y2), 8, (0,255,0), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)

        length =int( math.hypot(x2-x1,y2-y1))
        
        data= '0'+str(length)
        print(int(data))
        arduino.sendData([int(data)])
        
        
    cv2.imshow("Hand Gesture", img)
    cv2.waitKey(1)
