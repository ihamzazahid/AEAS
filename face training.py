# -*- coding: utf-8 -*-
"""
Created on Mon May  3 04:57:25 2021

@author: HAMZA
"""
import cv2
import numpy as np
from PIL import Image
import os
from imutils.video import VideoStream
from time import sleep
model = cv2.face.LBPHFaceRecognizer_create()
dir_dataset = '/home/pi/tensorflow/Final_Codes/Recognition_Final/dataset'
stream = VideoStream(src=-1).start()
print('[INFO] Wait for two seconds')
sleep(2)
def getimage(dir_dataset):
    imagePaths = [os.path.join(dir_dataset,i) for i in os.listdir(dir_dataset) ]
    print(imagePaths)
    faces = []
    IDs = []
    for imagePath in imagePaths:
        img = Image.open(imagePath).convert('L')
        imgNp = np.array(img,'uint8')
        ID = (os.path.split(imagePath)[-1].split('.')[1])
        ID = int(ID)
        print('[INFO] Training ',ID)
    
        faces.append(imgNp)
        IDs.append(ID)
        cv2.imshow('Training Data',imgNp)
        cv2.waitKey(1)
    return IDs,faces

IDs,faces = getimage(dir_dataset)
IDs = np.array(IDs)
model.train(faces,IDs)
model.write('/home/pi/tensorflow/Final_Codes/Recognition_Final/Training.yaml')
print('\n[INFO] Recognisor has been trained successfully!')
cv2.destroyAllWindows()    
stream.stop()
