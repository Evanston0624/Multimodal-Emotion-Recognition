#!/bin/bash
for i in $(seq 0 4)
do
    CUDA_VISIBLE_DEVICES=1 python3 run_classifier_5fold.py --train_text_file data/emo_fold/5_fold_4emo_tr_texts.${i}.txt --test_text_file data/emo_fold/5_fold_4emo_te_texts.${i}.txt --train_condition_file data/emo_fold/5_fold_4emo_tr_labels.${i}.txt --test_condition_file data/emo_fold/5_fold_4emo_te_labels.${i}.txt --bert_model bert-base-chinese --output_dir bert_result/5fold/WeiKai --label_num 4 --max_seq_length 35 --do_train --do_eval --train_batch_size 32 --eval_batch_size 8 --learning_rate 2e-5 --num_train_epochs 20 --fold_num ${i}
done

: <<'END'
    5fold訓練+測試:
        測試使用者句子情緒分類
        測試系統句子情緒分類
    參數:
        train_text_file fold訓練[tr]資料(使用者輸入句[q]/系統回應句[a])
        test_text_file fold測試[te]資料(使用者輸入句/系統回應句)
        train_condition_file fold訓練資料標籤
        test_condition_file fold測試資料標籤
        bert_model bert預訓練模型
        output_dir 輸出位置
        label_num 標籤數
        max_seq_length 句子最長字元數 
        do_train 訓練
        do_eval 測試
        train_batch_size  
        eval_batch_size  
        learning_rate  
        num_train_epochs 訓練epoch數
        fold_num 訓練的fold
END
