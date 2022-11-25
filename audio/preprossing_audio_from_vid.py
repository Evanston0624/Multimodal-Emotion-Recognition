import os

raw_wavpath='./matched_video/'
tar_wavpath='./preprocess_audio_from_video/'
for f in os.listdir(raw_wavpath):
    # -ac channel num -ar sample rate
    f_name = tar_wavpath+f.split('.')[0]+'.wav'
    command ='ffmpeg -i '+raw_wavpath+f+' -ac 1 -ar 16000 '+f_name
    print(command)
    os.system(command)
