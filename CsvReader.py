#!/usr/bin/python 

import csv

#Set here the path to the file
fileName = "test.csv"

file = open(fileName, "rb")

try:
	reader = csv.reader(file)
	for row in reader:
		print row

finally:
	file.close()
