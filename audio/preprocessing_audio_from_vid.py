import os

raw_wavpath='matched_video/'
tar_wavpath='preprocessed_matched_audio_from_video/'
for f in os.listdir(raw_wavpath):
    # check file size if > 500 bytes
    if (os.path.getsize(raw_wavpath+f)>500):
        # -ac channel num -ar sample rate
        f_name = tar_wavpath+f.split('.')[0]+'.wav'
        command ='ffmpeg -i '+raw_wavpath+f+' -ac 1 -ar 16000 '+f_name
        print(command)
        os.system(command)
