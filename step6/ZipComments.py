from __future__ import print_function
import zipfile

zf = zipfile.ZipFile("channel/channel.zip")
f = open("channel/90052.txt",'r')
fileName = f.read().replace("Next nothing is ", "")
print (zf.getinfo("90052.txt").comment, end='')

while fileName:
	filePath = "channel/"+fileName+".txt"
	f = open(filePath)
	fileName = f.read().replace("Next nothing is ","")
	print (zf.getinfo(fileName+".txt").comment, end='')
