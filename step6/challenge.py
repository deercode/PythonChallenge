f = open("channel/90052.txt",'r')

fileName=f.read().replace("Next nothing is ","")
print (fileName)
i=0
while fileName:
	filePath = "channel/"+fileName+".txt"
	f = open(filePath)
	fileName = f.read().replace("Next nothing is ","")
	print (str(i) + " " + fileName)
	i = i+1

