#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import cv2

class Rheumatoid :
    def __init__(self,filename):
        self.filename =filename


    def prediction_Rheumatoid (self):
        # load model
        model = load_model('RA.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        img_array = cv2.imread(imagename, cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array, (64, 64))
        new_image = new_array.reshape(-1, 64, 64, 1)
        # test_image = image.load_img(imagename, (64, 64))
        # test_image = image.img_to_array(test_image)
        # test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(new_image)
        print(result)

        if result[0][0] ==1:
            prediction = 'Not rheumatoid arthritis'
            return [{ "image" : prediction}]

        else:
            prediction = 'rheumatoid arthritis'
            return [{ "image" : prediction}]


