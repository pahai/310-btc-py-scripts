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

#gray bits通道线索
gray_channel = Image.open(r'C:\Users\Pahai\Desktop\challenge.png')
data = gray_channel.load()
bin_red = []
for i in range(2944):
	bin_red.append(bin(data[i,310][0])[-1])
bin_red = ''.join(str(i) for i in bin_red)
xor = ''.join(str(int(bin1[i])^int(bin_red[i])) for i in range(2800))
xor = xor.replace('0','2')
xor = xor.replace('1','0')
xor = xor.replace('2','1')
xor = xor[:1960]
c= hex(int(str(xor),2))[2:]
#d= binascii.a2b_hex(c)
#e = hex(int(bin2))
print(c)
