import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#Track one of these points / positions
pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #convert it into rgb, hands uses only rgb images

    results = hands.process(imgRGB) #method(process) inside the object(hands) -> process frame for us and give us the results
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark): #ids for each position
                # print(id, lm) #multiply with width and height to get answer in pixels
                h, w, c = img.shape #channel
                cx, cy = int(lm.x * w),  int(lm.y * h) #position of center
                print(id, cx, cy)

                if id == 0:
                    cv2.circle(img, (cx, cy), 25, (77, 0, 153), cv2.FILLED)
                elif id == 4:
                    cv2.circle(img, (cx, cy), 15, (255, 128, 191), cv2.FILLED)



            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

#Track one of these points / positions
    cTime = time.time() #This will give us the currecnt time
    fps = 1 / ( cTime - pTime )
    pTime = cTime

    #Display on screen
    cv2.putText(img, 
        str(int(fps)), 
        (10, 70), 
        cv2.FONT_HERSHEY_PLAIN, 
        3,
        (255,0,255),
        3 
    )
# integer values for fps | position(value) | font | scale | color | thickness


    cv2.imshow("Image", img)
    cv2.waitKey(1)