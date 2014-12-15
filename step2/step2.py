from collections import Counter
import re, urllib
# This code was originally made local PC. I moved it from Local PC to this place.
url = "http://www.pythonchallenge.com/pc/def/ocr.html"

response=urllib.urlopen(url).read()

m = response.find(r"%%$@_$^__")

strArg =  response[m:len(response)-5]

print(Counter(strArg))
