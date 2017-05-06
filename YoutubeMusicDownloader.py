#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

#This script requires pafy library : https://github.com/mps-youtube/pafy
#Create a txt file with URLs to music you want to download from Youtube
#One URL per line

import pafy
import os

#Set here the path to your file
file = open("tracks.txt", "r")

for line in file :
	target = pafy.new(line)
	audio = target.audiostreams
	audio[0].download()

file.close()
