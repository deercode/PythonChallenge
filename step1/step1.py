strArg = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

def Decrypt(strArg):
	temp = ""
	for i in strArg :	
		if ( i == " " or i == "'" or i == "."):
			temp = temp + i
		elif ((ord(i) + 2 ) > ord('z')) :
			temp = temp + chr( ord(i) + 2 - ord('z') + ord('a') -1)
		else:
			temp = temp + chr( ord(i) + 2 )
	return temp

print(Decrypt(strArg))
