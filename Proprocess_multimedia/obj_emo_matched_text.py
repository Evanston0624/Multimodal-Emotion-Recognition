import os
import pandas as pd
import csv
import shutil



# 因為原本文字資料有空白資料' ' Bert不會有此種output
# 把從server上跑完BD的結果map到原本的data上
if __name__ == '__main__':
    ## check audio
    dr = pd.read_csv('text.csv', index_col=False)
    df = dr["write"]
    filter = dr["write"]!=' '
    filtered_df = dr[filter]
    print(len(filtered_df))
    filtered_df.drop(columns=["object_Anger", "object_Happiness","object_Sadness","icon"])
    filtered_df.to_csv('filtered_text.csv',index=0)
    ## result save as tmp_df
    dr = pd.read_csv('filtered_text.csv', index_col=False)
    print(len(dr))

    obj_emo_res =  pd.read_csv('EP.csv', index_col=False)
    print(len(obj_emo_res))

    #mapping
    anger = obj_emo_res['Anger'].values.tolist()
    happy = obj_emo_res['Happy'].values.tolist()
    neutral = obj_emo_res['Neutral'].values.tolist()
    sad = obj_emo_res['Sad'].values.tolist()
    # Anger, Happy, Neutral, Sad
    dr['object_Anger'] = anger
    # "object_Anger", "object_Happiness", "object_Sadness"
    dr["object_Happiness"] = happy
    dr["object_Neutral"] = neutral
    dr["object_Sadness"] = sad
    dr.to_csv('./obj_emo_res/user_text_res.csv',index=0)