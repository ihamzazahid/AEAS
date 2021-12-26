# -*- coding: utf-8 -*-
"""
Created on Mon May  3 05:44:42 2021

@author: HAMZA
"""
import cv2
import imutils
from time import sleep
dir_cascade =  '/home/pi/tensorflow/Final_Codes/Recognition_Final/haarcascade_frontalface_default.xml'
dir_training = '/home/pi/tensorflow/Final_Codes/Recognition_Final/Training.yaml' 
cascade = cv2.CascadeClassifier(dir_cascade)
model = cv2.face.LBPHFaceRecognizer_create()
model.read(dir_training)
Stream = cv2.VideoCapture(-1)
color = (0,255,0)
global ID
ID = None
while True:
    ret,frame = Stream.read()
    frame = imutils.resize(frame,width=400)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces)==1:
        for x,y,h,w in faces:
            ID,conf=model.predict(gray[y:y+h,x:x+w])
            if conf<55:
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
                cv2.putText(frame,str(ID),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.45,(0,255,0),2)
            else:
                ID="Unknown"
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.putText(frame,str(ID),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.45,(0,0,255),2)
    cv2.imshow("Recognisor",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

Stream.release()
cv2.destroyAllWindows()
  

