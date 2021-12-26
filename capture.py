# -*- coding: utf-8 -*-
"""
Created on Mon May  3 04:05:36 2021

@author: HAMZA
"""
import cv2
import time
dir_cascade = '/home/pi/tensorflow/Final_Codes/Recognition_Final/haarcascade_frontalface_default.xml'
dir_dataset = '/home/pi/tensorflow/Final_Codes/Recognition_Final/dataset/'
cascade = cv2.CascadeClassifier(dir_cascade)

name = str(input('Enter the name: '))
roll_no = str(input("Enter the roll no without '-': "))
stream = cv2.VideoCapture(-1)
count = 0
while True:
    check,frame = stream.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray,1.3,3,0)
    for x,y,h,w in faces:
        count+=1
        cv2.imwrite(dir_dataset+'users.'+roll_no+'.'+str(count)+'.'+'jpg',gray[y:y+h,x:x+h])
        
        print('[INFO] Image has been written!')
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)
    cv2.imshow('Capture',frame)
    time.sleep(1)
    cv2.waitKey(1)
    if count>10:
        break

print('Dataset of '+name+' having roll no '+roll_no+' has been captured!')

stream.release()
cv2.destroyAllWindows()

