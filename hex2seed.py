m = '511b2033232841053022b0fe52ed0f7a165b52c7e75112f656fc4b'
shift_key = '20181002'
hex_num = '0123456789abcdef'

m0 = []

for i in range(len(m)):
	#分别获取密文和key的值
	m_char = m[i]
	shift_key_char = shift_key[i % len(shift_key)]
	#分别获取密文和key在16进制数中的位置
	m_index = hex_num.index(m_char)
	shift_key_index = hex_num.index(shift_key_char)
	#此处做减法
	new_char_index = (m_index - shift_key_index) % len(hex_num)
	new_char = hex_num[new_char_index]
	
	m0.append(new_char)

m0 = ''.join(m0)
answer = []
for i in range(0,len(m0),3):
	answer.append(m0[i:i+3])
	
print(answer)

seed = []
for i in answer:
	seed.append(int(i,16))

print(seed[6:])

#https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt

with open(r'C:\Users\Pahai\Desktop\bip39.txt') as f:
	wordlist = [ i.strip() for i in f.readlines() ]
	
for i in seed[6:]:
	print(wordlist[i-1])
