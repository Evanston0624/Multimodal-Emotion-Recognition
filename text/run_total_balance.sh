#!/bin/bash

CUDA_VISIBLE_DEVICES=1 python3 run_classifier_total.py --text_file data/emo_fold/balanced_4emotions_texts.txt --condition_file data/emo_fold/balanced_4emotions_labels.txt --bert_model bert-base-chinese --output_dir bert_result/total/balance --label_num 4 --max_seq_length 35 --do_train --train_batch_size 32 --learning_rate 2e-5 --num_train_epochs 20

: <<'END'
測試 learning rate:
    測試使用者句子情緒分類
    測試系統句子情緒分類
參數:
    text_file 語料(使用者輸入句/系統回應句)
    condition_file 標籤
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

END