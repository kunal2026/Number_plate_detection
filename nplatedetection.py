import cv2
frameWidth=640
frameHeight=480
NumberPlateCascade=cv2.CascadeClassifier(r'C:\Users\USER\Downloads\haarcascade_russian_plate_number.xml')
minArea=500

abc=cv2.VideoCapture(0)  # use 0 for default web cam 

while True:

    success, img=abc.read()
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    nplates=NumberPlateCascade.detectMultiScale(img_gray,1.1,4)
    
    #rectangle around plate
    for(x,y,w,h) in nplates:
        area=w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            main_img= img[y:y+h,x:x+w]
            cv2.imshow("Main",main_img)
            
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break