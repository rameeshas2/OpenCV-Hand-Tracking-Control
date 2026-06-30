import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionConfidence = 0.5, trackConfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionConfidence,
            min_tracking_confidence=self.trackConfidence
        )

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #convert it into rgb, hands uses only rgb images

        self.results = self.hands.process(imgRGB) 
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self, img, handNo = 0, draw = True):

        self.lmList = []
        if self.results.multi_hand_landmarks: #to use results here we have to use self in upper and this function
            myHand = self.results.multi_hand_landmarks[handNo] #point to particulalar no (hand no)

            for id, lm in enumerate(myHand.landmark): # get that first hand and their landmarks
                # print(id, lm) #multiply with width and height to get answer in pixels
                h, w, c = img.shape #channel
                cx, cy = int(lm.x * w),  int(lm.y * h) #position of center
                # print(id, cx, cy)

                self.lmList.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 12, (77, 0, 153), cv2.FILLED)
                # elif id == 4:
                #     cv2.circle(img, (cx, cy), 15, (255, 128, 191), cv2.FILLED)

        return self.lmList

    def fingersUp(self):
        fingers = []

        # Thumb
        if self.lmList[4][1] > self.lmList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other fingers
        tipIds = [8, 12, 16, 20]

        for id in tipIds:
            if self.lmList[id][2] < self.lmList[id-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector() #no need of parameters here as they are already defined

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        if len(lmList) != 0: 
            print(lmList[4])

        #Track one of these points / positions
        cTime = time.time()
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


if __name__ == "__main__":
    main() 
#what is written in main() will run dummy code to show what this module can do...