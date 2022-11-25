import pickle
from utils import extract_feature, AVAILABLE_EMOTIONS
import csv
import os

file_path='preprocessed_matched_audio_from_video/'
if __name__ == '__main__':
    res=[]
    with open('./best_4emo_model/4emo_classifier.pickle','rb') as f:
        clf2 = pickle.load(f)
        #features=["mfcc","chroma","mel"]
        for f in os.listdir(file_path):
            #print(f)
            
            audio_path=file_path+f
            #audio_path='./0316test.wav'
            feature=extract_feature(audio_path,mel=True,mfcc=True,chroma=False).reshape(1,-1)
            prediction = clf2.predict_proba(feature)[0]
            
            tmp=list(prediction)
            
            tmp.insert(0,f)
            print(tmp)
            res.append(tmp)
            #print("Prediction:",prediction)
        #print(res)
        with open('predict_audio_from_vid.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(res)
            
            
