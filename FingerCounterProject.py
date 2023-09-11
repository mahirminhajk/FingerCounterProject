import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480

pTime = 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

#* folder path
folderPath = "images"
myList = os.listdir(folderPath) #* list of images
overlayList = []
#* loop through images
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)


detector = htm.handDetector(maxHands=1, detectionCon=0.75)

#* figer tip ids
tipIds = [4, 8, 12, 16, 20]

#* main loop
while True:
    success, img = cap.read()

    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        fingers = []

        #* thumb
        if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #* 4 fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)

    #* overlay image on top of camera feed
    h, w, c = overlayList[1].shape #* height, width, channels
    img[0:h, 0:w] = overlayList[1] 

    #* fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (2, 480), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 255), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)