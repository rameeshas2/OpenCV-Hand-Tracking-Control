import cv2
import time
import os #to store the images of the fingers in a folder
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
pTime = 0

wCam, hCam = 640, 480

cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImages"
myList = os.listdir(folderPath)
print(myList) #get alll the names

overlayList = [] #overlay this image on our main image
for imPath in myList: #loop through the list of images
    image = cv2.imread(f"{folderPath}/{imPath}") #FingerImages/1.jpg -- imported image but not saved yet
    # print(f"{folderPath}/{imPath}") # -- imported image but not saved yet

    # RESIZE the image to match your 200x200 slice
    image = cv2.resize(image, (200, 200))

    overlayList.append(image) #append the image to the list

print(len(overlayList)) #print the number of images in the list


detector = htm.handDetector(detectionConfidence=0.75) #we can change the confidence level here, default is 0.5


tipIds = [4, 8, 12, 16, 20] #tip of the fingers


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False) #we already drawing so drawing is false 
    # print(lmList)

    if len(lmList) != 0:
        #    50    100 (finger open ) | 100    50 (finger closed)
        fingers = []

        # thumb
        if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]: #if the tip of the thumb is above the middle joint of the thumb, then it is considered as up
            fingers.append(1) #finger is open
        else:
            fingers.append(0) #finger is closed

# 4 fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]: #if the tip of the index finger is above the middle joint of the index finger, then it is considered as up
                fingers.append(1) #finger is open
            else:
                fingers.append(0) #finger is closed

        # print(fingers)
        totalFingers = fingers.count(1) #found how many 1 we have
        print(totalFingers)

        h, w, c = overlayList[totalFingers-1].shape
        img[0 : h, 0 : w] = overlayList[totalFingers-1]  #img 2 -1 = img 1
        # when its 0 (fist close) -> it gives us img 6
        #maintain 200x200 size of the image | 100:300 (0:200) is the range of height | 100:300 (0:200) is the range of width
        # SLICING - height | range of the height | range of width
            

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED) #rectangle for the text
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, 
                                            (255, 0, 0), 25) #text for the number of fingers



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)