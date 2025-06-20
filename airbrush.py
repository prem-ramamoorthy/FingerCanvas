import cv2 as cv
import numpy as np 
import handDetection as hd

wcam , hcam = 640 , 480 

logo = cv.imread(r"FingerCanvas\images\logo.jpg")
banner = cv.imread(r"FingerCanvas\images\banner.jpg")
eraser = cv.imread(r"FingerCanvas\images\eraser.jpg")
colors = cv.imread(r"FingerCanvas\images\colors.jpg")

colors = cv.resize(colors , (480 , 80))
logo = cv.resize(logo , (80 , 80))
banner = cv.resize(banner , (wcam , 80))
eraser = cv.resize(eraser , (80 , 80))

vid = cv.VideoCapture(0)
vid.set(3,wcam)
vid.set(4,hcam)

thickness = 5

detector = hd.handDetection(detectionCon=0.7)

xp , yp = 0, 0
selected_color = (255,255,255)
thickness = 5

imagecanvas = np.zeros((hcam , wcam , 3) , np.uint8)

while(True) :
    isTrue , frame = vid.read()
    if not isTrue :
        break
    
    frame = detector.findHands(frame )
    lmlist = detector.findposition(frame, draw= False)
    
    frame[0:80 , 0:wcam] = banner
    frame[0:80 , 0:80] = eraser
    frame[0:80 , 80:560] = colors
    frame[0:80 , (wcam-80):wcam] = logo
    
    if lmlist :
        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[12][1:]
        fingersopen = detector.fingersup()
        
        if fingersopen[1] and fingersopen[2] : 
            xp , yp = 0,0
            if(x1 >= 400 and x1 <= 530 and y1 <= 80):
                selected_color = (255, 0, 0)
            if(x1 >= 260 and x1 <= 380 and y1 <= 80):
                selected_color = (0, 255, 0)
            if(x1 >= 110 and x1 <= 230 and y1 <= 80):
                selected_color = (0, 0, 255)
            if(x1 >= 0 and x1<= 80 and y1 <= 80) :
                selected_color = (0,0,0)
            
            cv.rectangle(frame , (x1, y1) , (x2,y2) , selected_color , -1)
        
        if fingersopen[1] and fingersopen[2] == 0 :
            cv.circle(frame , (x1,y1) , int(thickness) , selected_color , -1)
            if xp == 0 and yp == 0 :
                xp , yp = x1 , y1
                
            cv.line(frame , (xp,yp) , (x1,y1) , selected_color , int(thickness) )
            cv.line(imagecanvas , (xp,yp) , (x1,y1) , selected_color , int(thickness) )
            xp , yp = x1, y1
            
        if fingersopen[0] and fingersopen[1] :
            x , y = lmlist[4][1] , lmlist[4][2]
            x0 , y0 = lmlist[8][1] , lmlist[8][2]
            distance = int(((x0 - x ) ** 2 + (y0 - y ) ** 2) ** 0.5)
            c1,c2 = (x +x0)//2 , (y +y0)//2
            thickness = np.interp(distance , [40 , 180] , [5,50])
        

    imgray = cv.cvtColor(imagecanvas , cv.COLOR_BGR2GRAY )
    _ , imgInv = cv.threshold(imgray , 50 , 255 , cv.THRESH_BINARY_INV)
    imgInv = cv.cvtColor(imgInv , cv.COLOR_GRAY2BGR)
    frame = cv.bitwise_and(frame , imgInv) 
    frame = cv.bitwise_or(frame , imagecanvas)
    
    frame = cv.flip(frame, 1)
    cv.imshow('Video' , frame)
    
    if cv.waitKey(1) & 0xFF == ord('d'):
            break