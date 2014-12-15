import urllib2

def ExtractNumber( arg ):
	for s in arg.split():
		if ( s.isdigit()):
			return s

def RepeatQuery(nextLink):
	while nextLink :
		content = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(nextLink)).read()	
		nextLink = ExtractNumber(content)
		print nextLink

content = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345").read()

nextLink = content.replace("and the next nothing is ","")


RepeatQuery(nextLink)
RepeatQuery(8022)
