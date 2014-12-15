from __future__ import print_function
import urllib, pickle

url="http://www.pythonchallenge.com/pc/def/banner.p"
handle = urllib.urlopen(url)
doublelist = pickle.load(handle)
handle.close()

for list in doublelist:
	for i in list:
		for j in range(0, i[1]):
			print (i[0],end='')
	print('\n')
