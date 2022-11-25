import os
import pandas as pd
import csv
import shutil

#將收集到的語音資料放置資料夾
dir_audio="./upload_mic"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ## check audio
    # user_audio.csv => 抓info資料 type = 1
    dr = pd.read_csv('audio.csv', index_col=False)
    df = dr["write"]
    ## result save as tmp_df
    tmp_df=dr.copy()
    delete_index=[]
    #
    matched_audio_num = 0
    idx=0
    for file_name in df:
        filepath=dir_audio+'/'+file_name
        if not os.path.isfile(filepath):
            print("idx:",idx,file_name,"is not exist!")
            delete_index.append(idx)
        else:
            print("idx",idx,file_name,"is exist")
            matched_audio_num += 1
            shutil.copyfile(filepath, "./matched_audio/"+file_name)
        idx += 1
    print(len(delete_index))
    # delete the rows of non-exist files
    print(tmp_df.shape)
    tmp_df=tmp_df.drop(delete_index)
    print(tmp_df.shape)
    save_file="matched_audio.csv"
    # print(save_file)
    tmp_df.to_csv(save_file, index=False, header=True)
    print('matched audio:',matched_audio_num)