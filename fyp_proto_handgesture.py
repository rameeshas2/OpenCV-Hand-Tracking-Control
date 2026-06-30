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


mode = "IDLE"
prev_cx = 0
gestureTime = 0
cooldown = 1   # seconds between gesture triggers
language = "EN"



detector = htm.handDetector(detectionConfidence=0.7) #we can change the confidence level here, default is 0.5

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        # Thumb & Index finger positions
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Draw points
        cv2.circle(img, (x1, y1), 12, (255,255,0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 12, (255,255,0), cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255,255,0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255,255,0), 2)

        length = math.hypot(x2-x1, y2-y1)

        # ---------------- PINCH DETECTION ----------------
        if length < 40 and time.time() - gestureTime > cooldown:
            mode = "TRANSLATION"
            gestureTime = time.time()

        # ---------------- OPEN PALM (STOP) ----------------
        fingers = detector.fingersUp()

        if fingers == [1,1,1,1,1] and time.time() - gestureTime > cooldown:
            mode = "IDLE"
            gestureTime = time.time()

        # ---------------- SWIPE DETECTION ----------------
        hand_cx = lmList[9][1]   # center of palm
        dx = hand_cx - prev_cx

        if time.time() - gestureTime > cooldown:

            if dx > 60:
                mode = "DETECTION"
                gestureTime = time.time()

            elif dx < -60:
                language = "UR" if language == "EN" else "EN"
                gestureTime = time.time()

        prev_cx = hand_cx

        # ------------- OPTIONAL: KEEP VOLUME CONTROL -------------
        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])
        volume.SetMasterVolumeLevel(vol, None)

    # ----------- VOLUME BAR -----------
    cv2.rectangle(img, (50, 150), (85, 400), (255,0,0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255,0,0), cv2.FILLED)
    cv2.putText(img, f'Vol: {int(volPer)} %', (40, 450),
                cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)

    # ----------- MODE DISPLAY -----------
    cv2.putText(img, f'Mode: {mode}', (350, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

    cv2.putText(img, f'Lang: {language}', (350, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    # ----------- FPS -----------
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
