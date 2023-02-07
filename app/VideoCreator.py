#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : syfer   
# Created Date: 01/01/2023
# version ='1.0'
# ---------------------------------------------------------------------------
""" Ce fichier contient tou les module necaisaire a cree une video nigthcore a partire d'une image (jpg) et d'un son (mp3). Il sera combiner avec un module pour tellecarger les deux ellement et aussi a un module pour le tellecharger sur youtube """  
# ---------------------------------------------------------------------------
# Imports nightcore,asyncio,shazamio,audioread,PIL,subprocess,os,numpy,resizeimage,math
# ---------------------------------------------------------------------------

import nightcore as nc
import asyncio
from shazamio import Shazam
import cv2
import audioread
from PIL import Image
import subprocess
import numpy as np
from resizeimage import resizeimage
from math import *
import os

import time

''''
https://pypi.org/project/shazamio/
https://pypi.org/project/ShazamAPI/

https://pypi.org/project/ffmpegio/



ffmpeg -i video.mp4 -i song.mp3 -map 0:v:0 -map 1:a:0 output.mp4
ffmpeg -y -i video.mp4 -stream_loop -1 -i animated.gif -filter_complex [0]overlay=x=0:y=0:shortest=1[out] -map [out] -map 0:a? test.mp4
'''

def nightcoreSong():
    ''' Fonction qui utilise la librairi nightcore pour accelerait un fichier audio song/original.mp3  '''
    try :
        nc_audio = "song/original.mp3" @ nc.Tones(1.5) # Lien vers song orrigine : song/original.mp3
        nc_audio.export("song/speed_song.mp3") # Lien sond de sortie : song/seep
    except : 
        print("Erreur dans [nightcoreSong()]")

def get_time():
    '''Fonction qui renvoit le temps en seconde de la musique'''
    with audioread.audio_open('song/original.mp3') as f:
        totalsec = int(f.duration)*0.85
    return round(totalsec)#revois en second la duree de la musique 

async def Sha():#envois une requte a l'API shazam 
  '''Chepas top x)'''
  shazam = Shazam()
  out = await shazam.recognize_song('song/original.mp3')#Lien vers le song de depard 
  return out

def get_title():
    ''' utilise Sha() et renvoit le titre de la mussique '''
    loop = asyncio.get_event_loop()
    loop = loop.run_until_complete(Sha())

    return loop["track"]["title"]


def compretion_img():
    '''Compretion image'''
    image_path = "img/img.jpg"
    image_file = Image.open(image_path)
    image_file.save("img/img.jpg", quality=50)

def video():
    out_video_full_path = "video/video.mp4"
    cv2_fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    fimg  = Image.open("img/img.jpg")
    #ajouter une condition
    #fimg = resizeimage.resize_width(fimg,2000)


    heigth = fimg.height
    width = fimg.width

    video = cv2.VideoWriter(out_video_full_path,cv2_fourcc,25,[width,heigth])

    for seconde in range(get_time()):   
        for frame in range(1,25):
            fimg 
            colorImage = np.asarray(fimg) 
            image_rgb = cv2.cvtColor(colorImage,cv2.COLOR_BGR2RGB)

            video.write(image_rgb)

    video.release()

def videoAnimation():
    out_video_full_path = "video/video.mp4"
    cv2_fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    fimg  = Image.open("img/img.jpg")
    
    if fimg.width > 1500:
        fimg = resizeimage.resize_width(fimg,1500)

    heigth = fimg.height
    width = fimg.width

    video = cv2.VideoWriter(out_video_full_path,cv2_fourcc,25,[width,heigth])

    max_rotate = 1

    rotateD = max_rotate
    rotateG = 0

    rotate = True

    for seconde in range(get_time()):   
        for frame in range(1,25):
            
            if rotate :
                toto = fimg.rotate(rotateG)
                rotateG += 0.05

                if floor(rotateG)  == max_rotate:
                    rotate = False
                    rotateG = -max_rotate
            else:
                toto = fimg.rotate(rotateD)
                rotateD -= 0.05

                if floor(rotateD)  == -max_rotate*2:
                    rotate = True
                    rotateD = max_rotate
                

            colorImage = np.asarray(toto) 
            image_rgb = cv2.cvtColor(colorImage,cv2.COLOR_BGR2RGB)

            video.write(image_rgb)

    video.release()


def assembleur():
    '''assemble le song et la video pour sortir une video '''
    subprocess.run("ffmpeg -i video/video.mp4 -i song/speed_song.mp3 -c copy -map 0:0 -map 1:0 video/video_finale.mp4" , shell=True)

def compretion(): 
    subprocess.run("ffmpeg -i video/video_finale.mp4 -vcodec libx265 -crf 28 video/upload/{}-Nightcore-unmei-lyrics.mp4".format(str(get_title())) , shell=True)

def cleeaner():
    for dossier in ["img/","song/","video/"]:
        fichiers = os.listdir(dossier)
        for fichie in fichiers:
            try:
                os.remove(dossier+fichie)
            except:
                pass


start = time.time()
print("start ... ")
nightcoreSong()

print("compretion image")
compretion_img()

print("Creation video")
videoAnimation()

print("assrembler le song et la video")
assembleur()

print("compretion ")
compretion()
print("le temps d'execusion du programme est de {} seconde. ".format(time.time() - start))
