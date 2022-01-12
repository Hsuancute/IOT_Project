#程式碼來源 https://github.com/ch-tseng/PanTilt 
#有做部分修改

# import the necessary packages
import os
from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2
import numpy
import RPi.GPIO as GPIO
from libCH.pantilt import PanTilt

GPIO.setmode(GPIO.BOARD)

imgsize_w = int(640*0.4)
imgsize_h = int(480*0.4)
moveDegree = 0.25

#_[LED_CONFIGURATION]__________________________________________
pinLED = 36
GPIO.setup(pinLED ,GPIO.OUT)

#_[PIR_CONFIGURATION]__________________________________________
pinPIR = 32
GPIO.setup(pinPIR ,GPIO.IN)

#_[PAN/TILT_SERVO_CONFIGURATION]_______________________________
motorPT = PanTilt(7,12)


# initialize the video stream and allow the cammera sensor to warmup
vs = VideoStream(usePiCamera=1).start()

time.sleep(2.0)

#_INTERRUPTS_FOR_PIR___________________________________________
#def MOTION(pinPIR):
#    global statusPIR
#    print("PIR detected!")
#    statusPIR = 1

def movePANTILT(diffX, diffY, yDegreeNow):  # yDegreeNow is for adjustment only.
    global moveDegree, imgsize_w, imgsize_h

    if yDegreeNow<=80 and yDegreeNow>=70:
        adjustDegreeX = moveDegree
        adjustDegreeY = moveDegree
    else:
        adjustDegreeX = moveDegree/2
        adjustDegreeY = moveDegree/2

    lengthX1 = (imgsize_w/2) * 0.2
    lengthY1 = (imgsize_h/2) * 0.2
    lengthX2 = (imgsize_w/2) * 0.4
    lengthY2 = (imgsize_h/2) * 0.4
    lengthX3 = (imgsize_w/2) * 0.5
    lengthY3 = (imgsize_h/2) * 0.5
    lengthX4 = (imgsize_w/2) * 0.7
    lengthY4 = (imgsize_h/2) * 0.7


    if abs(diffX)<lengthX1: adjustDegreeX = moveDegree/3
    if abs(diffX)<lengthX2 and abs(diffX)>=lengthX1: adjustDegreeX = moveDegree/2
    if abs(diffX)<lengthX3 and abs(diffX)>=lengthX2: adjustDegreeX = moveDegree
    if abs(diffX)<lengthX4 and abs(diffX)>=lengthX3: adjustDegreeX = moveDegree*2
    if abs(diffX)>=lengthX4: adjustDegreeX = moveDegree*3.0

    if abs(diffY)<lengthY1: adjustDegreeY = moveDegree/2
    if abs(diffY)<lengthY2 and abs(diffY)>=lengthY1: adjustDegreeY = moveDegree/1.5
    if abs(diffY)<lengthY3 and abs(diffY)>=lengthY2: adjustDegreeY = moveDegree
    if abs(diffY)<lengthY4 and abs(diffY)>=lengthY3: adjustDegreeY = moveDegree*1.5
    if abs(diffY)>=lengthY4: adjustDegreeY = moveDegree*2.0

    if diffX<0:
        motorPT.movePAN(-adjustDegreeX)
        print("Move X --> " + str(-adjustDegreeX))
    else:
        motorPT.movePAN(adjustDegreeX)
        print("Move X --> " + str(-adjustDegreeX))

    if diffY<0:
        motorPT.moveTILT(adjustDegreeY)
        print("Move Y --> " + str(adjustDegreeY))
    else:
        motorPT.moveTILT(-adjustDegreeY)
        print("Move Y --> " + str(-adjustDegreeY))

def fireDetect(yDegreeNow):
    
    global imgsize_w, imgsize_h, fireNow, cv2

    print("Fire Detect")
    frame = vs.read()
    frame = imutils.resize(frame, width=imgsize_w)
    #frame = imutils.rotate(frame, 180)

    fire_cascade = cv2.CascadeClassifier('/home/pi/lin/cascade.xml')
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(gray, 1.1, 5)
    fireNow = len(fire)

    ifire = 0
    for (x,y,w,h) in fire:
        if ifire == 0:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        else:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
            ifire += 1

    print ("Detected "+str(fireNow)+" fire(s)")

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if(fireNow>0):

        GPIO.output(pinLED, GPIO.HIGH)
        os.system('sudo uhubctl -a on -l 1-1')
        xfire = fire[0][0]
        yfire = fire[0][1]

        #print "x,y = " + str(xfire) + "," + str(yfire)
        diffX = (imgsize_w/2) - x - (w/2)
        diffY = (imgsize_h/2) - y - (h/2)
        #print "diffX, diffY = " + str(diffX) + "," + str(diffY)
        movePANTILT(diffX, diffY, yDegreeNow)

    else:
        GPIO.output(pinLED, GPIO.LOW)
        os.system('sudo uhubctl -a off -l 1-1')
        fireNow = 0



#GPIO.add_event_detect(pinPIR, GPIO.RISING, callback=MOTION)

iX=0
iY=0
statusPIR = 0
fireNow = 1

# loop over the frames from the video stream
while True:
    
    
    #statusPIR = GPIO.input(pinPIR)   

    if statusPIR == 0:
        if motorPT.inaction==0: 
            motorPT.start()

        for routinY in range(55,120,15): # Degrees for camera Y bar, you can change this.
            print(routinY)
            if iY%2 > 0:
                routinY = 50 - routinY  # Y bar = 45, 70, 95  , so, 95-45 = 50

            motorPT.moveTILTto(routinY/10.0)   # Move Tilt to the degree

            for routinX in range(25, 125, 5):  # X bar for camera is : 25,30,35.....,120
                print(routinX)
                if iX%2 > 0:   # this will let the PAN move reverse, do not need to move 180 degree to start.
                    routinX = 125 - routinX # 12.5 is 180 degree
                
                motorPT.movePANto(routinX/10.0)

                fireNow = 1
                while fireNow>0:  # check and track the fire until lost it.
                    time.sleep(5.0)
                    fireDetect(routinY)

            iX += 1
            statusPIR = 0

        iY += 1

    else:
        #print("No body here, sleep...")
        iX = 0
        iY = 0
        fireNow = 1
        if motorPT.inaction==1: 
            motorPT.stop()
