import itertools
import subprocess
#利用生成器，生成所有可能的key
filename =r'C:\ENCRYPTED.txt'

sets = [ ['L3','3L'], ['02','20'], ['485','584'], ['9F','F9'], ['7'] ]
all_item_permutations = []

sets_permutations = list(itertools.permutations(sets, len(sets)))

for sets_permutation in sets_permutations:
    item_permutations = list(itertools.product(*sets_permutation))
    all_item_permutations += item_permutations
#print(all_item_permutations)

keys = []
for permutation in all_item_permutations:
    keys.append(''.join(permutation))
#print(keys)
#暴力破解
for key in keys:
	proc =  subprocess.Popen([r'C:\OpenSSL-Win64\bin\openssl','enc','-aes-256-cbc','-md', 'md5', '-base64','-d','-a','-k', key, '-in', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out,err = proc.communicate()
	if 'bad decrypt' not in str(err):
		print(out,key)
