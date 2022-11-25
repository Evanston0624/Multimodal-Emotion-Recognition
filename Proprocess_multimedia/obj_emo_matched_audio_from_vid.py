import os
import pandas as pd
import csv
import shutil
from datetime import datetime

dir_res="./obj_emo_res/"


# Match audio res and account name
if __name__ == '__main__':
    ## check audio
    columns = ['filename', 'sad', 'neutral', 'happy', 'angry']
    dr = pd.read_csv('predict_audio_from_vid.csv', header=None , index_col=False,names=columns)
    dr1 = pd.read_csv('matched_video.csv',index_col = False)
    # get len of rows
    user_account = []
    res_columns = ['filename', 'sad', 'neutral', 'happy', 'angry', 'Account', 'formatetime']
    res = [res_columns]
    tmp_fn = ''
    tmp_account =''
    idx = dr.shape[0]
    matched_num = 0
    print('data num:',idx)
    for i in range(0,idx):
        file_name = dr.iloc[i][0]
        file_name = file_name.split('.')[0] + '.mp4'

        print('filename',file_name)
        d = dr1[dr1['write'] == file_name]
        length = d.shape[0]

        # check if match file name
        if length == 0:
            print('error', file_name)
            continue
        else:
            print('matched', file_name)
            account = d.iloc[0][0]
            tmp_fn = dr.iloc[i][0]
            tmp_account = account
            matched_num += 1
        # map matched file name

        # account = d.iloc[0]['Account']
        sad = dr.iloc[i][1]
        neutral = dr.iloc[i][2]
        happy = dr.iloc[i][3]
        angry = dr.iloc[i][4]

        fn = tmp_fn
        date_of_file = fn.split('-',1)[0]
        year = date_of_file[0:4]
        mon = date_of_file[4:6]
        day = date_of_file[6:]
        date = str(year) + '-' + str(mon) + '-' + str(day)
        # date = datetime.strptime(date, "%Y-%m-%d")
        res.append([tmp_fn, sad, neutral, happy, angry, tmp_account ,date])
        print('tmp res', res)
    # insert the date to df

    #rename col
    #columns = ['filename', 'sad' , 'neutral' , 'happy' , 'angry','Account','formatetime']
    print('matched audio num',matched_num)

    with open('./obj_emo_res/audio_from_vid_res_by_user.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(res)