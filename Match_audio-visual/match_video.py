import os
import pandas as pd
import csv
import shutil


dir_audio="./upload_video"


if __name__ == '__main__':
    ## 抓info資料 type=3
    dr = pd.read_csv('video.csv', index_col=False)
    df = dr["write"]
    ## result save as tmp_df
    tmp_df=dr.copy()
    delete_index=[]
    matched_video_num = 0
    idx=0
    for file_name in df:
        filepath=dir_audio+'/'+file_name
        if not os.path.isfile(filepath):
            print("idx:",idx,file_name,"is not exist!")
            delete_index.append(idx)
        else:
            print("idx",idx,file_name,"is exist")
            shutil.copyfile(filepath, "./matched_video/"+file_name)
            matched_video_num += 1
        idx += 1
    print(len(delete_index))
    # delete the rows of non-exist files
    print(tmp_df.shape)
    tmp_df=tmp_df.drop(delete_index)
    print(tmp_df.shape)
    save_file="matched_video.csv"
    # print(save_file)
    tmp_df.to_csv(save_file, index=False, header=True)
    print('matched video:',matched_video_num)