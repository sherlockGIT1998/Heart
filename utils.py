import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config

class HeartDiesese():

    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):

        self.age = age 
        self.sex = sex
        self.cp = cp 
        self.trestbps = trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach 
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca 
        self.thal = thal

    def load_models(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.logistic_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.save_data  = json.load(f)

    def get_predicted_heart_di(self):
        self.load_models()

        array = np.zeros(len(self.save_data['column']))

        array[0] = self.age 
        array[1] = self.sex
        array[2] = self.cp
        array[3] = self.trestbps
        array[4] = self.chol
        array[5] = self.fbs
        array[6] = self.restecg
        array[7] = self.thalach
        array[8] = self.exang
        array[9] = self.oldpeak
        array[10] = self.slope 
        array[11] = self.ca 
        array[12] = self.thal

        print("TESTING an Array -->\n", array)

        yes_no = self.logistic_model.predict([array])[0]

        return yes_no
    
if __name__ == "__main__":

    age = 63.0
    sex = 1.0
    cp = 3.0
    trestbps = 145.0
    chol = 233.0
    fbs = 1.0
    restecg = 0.0
    thalach = 150.0
    exang = 0.0
    oldpeak = 2.3
    slope = 0.0
    ca = 0.0
    thal = 1.0  

    heart_diesese = HeartDiesese(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

    yes_no = heart_diesese.get_predicted_heart_di()

    if yes_no == 1:
         print("The Patient has Heart Disease..")
    else:
         print("The Patient do not have Heart Disease..")

        