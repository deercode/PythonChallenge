from __future__ import print_function
from PIL import Image

im = Image.open("oxygen.png")
rgb_im = im.convert('RGB')
width, height = im.size
cnt = 0
for wid in range(0,width):
	r, g, b = rgb_im.getpixel((wid,50))
	if cnt == 1 :
		print(chr(r), end='')
	cnt = (cnt + 1) %7
		

print()


for i in [105,110,116,101,103,114,105,116,121]:
	print (chr(i), end='')
			
