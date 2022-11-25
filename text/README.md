# Text emotion recognition based on BERT (4 emotions)
- The training and testing data are not included here.
- If you have any questions about the code, please email: g192e1654k@gmail.com

===========================================
# Result
- 5fold test
![image](https://github.com/Evanston0624/Multimodal-Emotion-Recognition/edit/main/text/result/system_5fold_cm.png)

===========================================
# Introduction 
- For the text emotion recognition model, this github uses BERT pre-trained from Chinese Wiki text data for fine-tuning. 
- The data used for fine-tuning is the data of 4 emotions taken from Ren -CECps.
- 4 emotions included : happy, angry, sad, and neutral.

===========================================
# Run the program
## Setting
- input = ./data_emofold/BD_data.txt, ./text.csv 
- output = ./EP.csv
- configuration = ./requirement.txt, ./conda_list.txt, ./package_version.txt

## run steps :
- step1. Preprocess text data
- preprocess_text.py

- step2. Text emotion recognition
- sh BD_extract_4emo_new.sh

- step3. Copy the result ./EP.csv and ./text.csv to Proprocess_multimedia folder

===========================================