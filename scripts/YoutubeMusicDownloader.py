#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

#This script requires pafy library : https://github.com/mps-youtube/pafy
#Create a txt file with URLs to music you want to download from Youtube
#One URL per line

#-- How to --
#run the script with your file as an argument as below
#./YoutubeMusicDownloader "path/to/your/file" 

import pafy
import os
import sys

fileList = []

for arg in sys.argv:
	print(arg)
	fileList.append(arg)

i = 1

while i < len(fileList) :
	file = open(fileList[i], "r")
	for line in file :
		print(line)
		target = pafy.new(line)
		audio = target.audiostreams
		audio[0].download()
		i +=1

file.close()
