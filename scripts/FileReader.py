#!/usr/bin/python 
# -*-coding:Utf-8 -*

import os
import sys

filein="/home/pipav/Documents/donnees"

file = open(filein, "r")
for line in file :
	print(line)
	
file.close()
