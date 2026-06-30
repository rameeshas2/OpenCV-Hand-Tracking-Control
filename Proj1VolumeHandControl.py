import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

################################################################
wCam, hCam  = 640, 480
#################################################################


cap = cv2.VideoCapture(0)
cap.set(3, wCam) #width
cap.set(4, hCam) #height
pTime = 0


device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(f"Audio output: {device.FriendlyName}")
print(f"- Muted: {bool(volume.GetMute())}")
print(f"- Volume level: {volume.GetMasterVolumeLevel()} dB")
print(f"- Volume range: {volume.GetVolumeRange()[0]} dB - {volume.GetVolumeRange()[1]} dB")

volRange = volume.GetVolumeRange() #get the range of volume in dB
minVol = volRange[0]
maxVol = volRange[1]

vol = 0
volBar = 400
volPer = 0

detector = htm.handDetector(detectionConfidence=0.7) #we can change the confidence level here, default is 0.5

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8]) #print the position of thumb and index finger

        x1, y1 = lmList[4][1], lmList[4][2] #thumb x | y
        x2, y2 = lmList[8][1], lmList[8][2] #index finger x | y

        cv2.circle(img, (x1, y1), 15, (255,255,0), cv2.FILLED) #thumb
        cv2.circle(img, (x2, y2), 15, (255,255,0), cv2.FILLED) #index finger

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2 #center point between thumb and index finger

        cv2.line(img, (x1, y1), (x2, y2), (255,255,0), 3) #line between thumb and index finger
        cv2.circle(img, (cx, cy), 15, (255,255,0), cv2.FILLED) #center point

        length = math.hypot(x2-x1, y2-y1)
        # print(length)


        #Hand range 50 - 300
        #Volume range -65(0%) - 0(100%)

        vol = np.interp(length, [50, 300], [minVol, maxVol]) #interp is used to convert one range to another range, here we are converting the length of the line between thumb and index finger to the volume range
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])
        # value | range we have | range to convert
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None) #if 0 -> 100% volume, -20 -> 50% volume, -60 -> 0% volume


        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0,255,0), cv2.FILLED) #change color to red if fingers are close

    cv2.rectangle(img, (50, 150), (85, 400), (255,0,0), 3)
    # initial position | ending position (85-50 = 35, ) | color | fill
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255,0,0), cv2.FILLED)
    cv2.putText(img, f'Vol: {int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)



    cTime  =time.time()
    fps = 1 /(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1) # 1 milisecond delay to show the image
