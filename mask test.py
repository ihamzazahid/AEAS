import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import cv2
maskModel = '/home/pi/tensorflow/Final_Codes/Mask/mask.model'
def Mask_Detection(frame,faceNet,maskNet):
    
    (h,w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame,1.0,(224,224),104.0,swapRB=False)
    
    faceNet.setInput(blob)
    detections = faceNet.forward()
    
    faces = []
    locations = []
    predictions = []
    
    for i in range(0,detections.shape[2]):
        probability = detections[0,0,i,2]
        
        if probability>0.5:
            box= detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            (startX,startY) = (max(0,startX),max(0,startY))
            
            (endX,endY) = (min(w-1,endX),min(h-1,endY))
            
            face = frame[startY:endY,startX:endX]
            face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
            face = cv2.resize(face,(224,224))
            face = img_to_array(face)
            face = preprocess_input(face)
            
            faces.append(face)
            locations.append((startX,startY,endX,endY))
            
    if len(faces)>0:
        faces = np.array(faces,dtype='float32')
        predictions = maskNet.predict(faces,batch_size=32)
        
    return(locations,predictions)

prototxt_path ='/home/pi/tensorflow/Final_Codes/Mask/deploy.prototxt'
weights_path = '/home/pi/tensorflow/Final_Codes/Mask/res10_300x300_ssd_iter_140000.caffemodel'

faceNet = cv2.dnn.readNet(prototxt_path,weights_path)
maskNet = load_model(maskModel)

print('Camera is getting prepared')

Stream = VideoStream(src=-1).start()

while True:
    frame = Stream.read()
    frame = imutils.resize(frame,width=400)
    
    (locations,predictions) = Mask_Detection(frame,faceNet,maskNet)
    label = ''
    mask = 0.0
    withoutMask = 0.0
    for (box,prediction) in zip(locations,predictions):
        (startX,startY,endX,endY) = box
        (mask,withoutMask) = prediction
        label = 'Mask' if mask>withoutMask else 'No Mask'
        color = (0,255,0) if label=='Mask' else (0,0,255)
        
        label = '{}:{:.2f}%'.format(label,max(mask,withoutMask)*100)
        
        cv2.putText(frame,label,(startX,startY-10),cv2.FONT_HERSHEY_SIMPLEX,0.45,color,2)
        cv2.rectangle(frame,(startX,startY),(endX,endY),color,2)
        
    cv2.imshow('Detector',frame)
    key = cv2.waitKey(1) & 0xFF
        
    if key == ord('q') :
        break
    if label=='Mask' or mask>withoutMask:
        break
cv2.destroyAllWindows()
Stream.stop()    
        
        
    
        

