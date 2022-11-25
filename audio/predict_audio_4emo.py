import pickle
from utils import extract_feature, AVAILABLE_EMOTIONS
import csv
import os

file_path='proprocessed_matched_audio/'
if __name__ == '__main__':
    res=[]
    num = 0
    t = 2452
    with open('./best_4emo_model/4emo_classifier.pickle','rb') as f:
        clf2 = pickle.load(f)
        #features=["mfcc","chroma","mel"]
        for fn in os.listdir(file_path):
            print(fn)
            num+=1
            print('num:',num)
            audio_path=file_path+fn
            feature=extract_feature(audio_path,mel=True,mfcc=True,chroma=False).reshape(1,-1)
            prediction = clf2.predict_proba(feature)[0]
            
            tmp=list(prediction)
            
            tmp.insert(0,fn)
            print(tmp)
            res.append(tmp)
            #print("Prediction:",prediction)
        #print(res)
        with open('predict_audio_res.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(res)
            
            
