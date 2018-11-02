#获取图片第310行像素，转为一串二进制
from PIL import Image

img = Image.open(r'C:\solved.bmp')
data = img.load()
code = []
for i in range(2800):	
	pix = list(data[i,310])
	if pix == [0,0,0]:
		code.append(1)
	if pix == [255,255,255]:
		code.append(0)

binary = ''.join(str(i) for i in code)
img.close()


#转换为对应的ascii字符,base64解码
import binascii
import base64

hex_0  = hex(int(str(binary),2))[2:]
base64_str = binascii.a2b_hex(hex_0)
salted_str = base64.b64decode(a)
open(r'C:\ENCRYPTED.txt','w').write(str(base64_str))
