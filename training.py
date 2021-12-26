from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np
import os

class Trainer:
    def __init__(self):
        self.data = []
        self.labels = []
        
        dataset = r"E:\\Mask_Final\\dataset"
        types = ["with_mask", "without_mask"]
        
        for category in types:
            path = os.path.join(dataset, category)
            for img in os.listdir(path):
                img_path = os.path.join(path, img)
                image = load_img(img_path, target_size=(224, 224))
                image = img_to_array(image)
                image = preprocess_input(image)
                
                self.data.append(image)
                self.labels.append(category)
            
        label_binarizer = LabelBinarizer()
        self.labels = label_binarizer.fit_transform(self.labels)
        self.labels = to_categorical(self.labels)
        
        self.data = np.array(self.data,dtype='float32')
        self.labels = np.array(self.labels)
        
        (trainX,testX,trainY,testY)=train_test_split(self.data,self.labels,test_size=0.20,stratify=self.labels,random_state=42)
        
        aug = ImageDataGenerator(rotation_range=20,zoom_range=0.15,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.15,horizontal_flip=True)
        
        Base_Model = MobileNetV2(include_top=False,input_tensor=Input(shape=(224,224,3)))
        
        headModel = Base_Model.output
        #Changing the pool size of Average Pooling 2D layer
        headModel = AveragePooling2D(pool_size=(7,7))(headModel)
        headModel = Flatten(name='flatten')(headModel)
        #Changing the activation of Dense layer from None to relu
        headModel = Dense(128,activation='relu')(headModel)
        headModel = Dropout(0.5)(headModel)
        headModel = Dense(2,activation='softmax')(headModel)
        
        my_model = Model(inputs=Base_Model.input,outputs = headModel)
        
        for layer in Base_Model.layers:
            layer.trainable=False
        
        print('[*] compiling the model') 

        initial_lr = 1e-4
        Epochs = 25
        
        Optimizer = Adam(lr=initial_lr,decay=initial_lr/Epochs)
        
        my_model.compile(loss='binary_crossentropy',optimizer=Optimizer,metrics=['accuracy'])               
        
        print('[*] training the head of the neural network')
        
        head = my_model.fit(aug.flow(trainX,trainY),steps_per_epoch=len(trainX)/32,validation_data=(testX,testY),validation_steps=len(testX)/32,epochs=Epochs)
        
        print('[*] Evaluating the neural network')
        
        predictions = my_model.predict(testX,batch_size=32)
        
        predictions = np.argmax(predictions,axis=1)
        
        print('[*] Printing the classification report\n\n')
        
        print(classification_report(testY.argmax(axis=1),predictions,target_names=label_binarizer.classes_))
        
        print('[*] Saving the model')
        
        my_model.save('mask.model',save_format='h5')
        
        
        N = Epochs
        plt.style.use("ggplot")
        plt.figure()
        plt.plot(np.arange(0, N), head.history["loss"], label="training loss")
        plt.plot(np.arange(0, N), head.history["val_loss"], label="value loss")
        plt.plot(np.arange(0, N), head.history["accuracy"], label="training accuracy")
        plt.plot(np.arange(0, N), head.history["val_accuracy"], label="val accuracy")
        plt.title("Training Loss and Accuracy")
        plt.xlabel("Epochs ")
        plt.ylabel("Loss/Accuracy")
        plt.legend(loc="best")
        plt.savefig("Training_Graph.png")

t1 = Trainer()
