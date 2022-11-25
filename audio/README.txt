*github SOURCE : https://github.com/x4nth055/emotion-recognition-using-speech

matched_audio
matched_video
==========================================
**RUN
# step1. 刪除過小的檔案(error) 以及 將檔案變成  mono channel 16000Hz 的 .wav
preprocessing_audio.py
preprocessing_audio_from_video.py

# step2. get 4emo of audio and auidio_form_vid (output:predict_audio_from_vid.csv , predict_audio.csv)
predict_audio_4emo.py
predict_audio_from_vid_4emo.py

# put predict_audio_from_vid.csv , predict_audio.csv in Proprocess_multimedia folder