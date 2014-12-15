import re, urllib                                                                            



url = "http://www.pythonchallenge.com/pc/def/equality.html"                                       
                                                                                            
response=urllib.urlopen(url).read()                                                          
                                                                                            
m = response.find(r"kAewtloY")                                                                                                                                                           
strArg =  response[m:len(response)-5] 

def CountSmallBoss(strArg):
	bossString = ""
	for i in range(4, len(strArg)-4):
		if ( strArg[i].islower() ):
			if ((strArg[i-4].islower() and strArg[i-3].isupper() and strArg[i-2].isupper() and strArg[i-1].isupper() and strArg[i+1].isupper() and strArg[i+2].isupper() and strArg[i+3].isupper() and strArg[i+4].islower() )):
				bossString = bossString + strArg[i]
	return bossString

print(CountSmallBoss(strArg))
    
