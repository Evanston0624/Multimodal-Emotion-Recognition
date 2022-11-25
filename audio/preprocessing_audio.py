import os

raw_wavpath='./matched_audio/'
tar_wavpath='./proprocessed_matched_audio/'
for f in os.listdir(raw_wavpath) :
    # check file size if > 100 bytes
    if (os.path.getsize(raw_wavpath + f) > 100):
        command='ffmpeg -i '+raw_wavpath+f+' -ac 1 -ar 16000 '+tar_wavpath+f
        print(command)
        os.system(command)
