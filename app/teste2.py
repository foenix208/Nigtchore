import subprocess
from PIL import Image


def overlay():
    fimg  = Image.open("img/img2.jpg")

    heigth = fimg.height 
    width = fimg.width

    subprocess.run("ffmpeg -y -i video_finale.mp4 -stream_loop -1 -i Library/animation.gif -filter_complex [0]overlay=x={}:y={}:shortest=1[out] -map [out] -map 0:a? test.mp4".format(width, heigth), shell=True)


overlay()