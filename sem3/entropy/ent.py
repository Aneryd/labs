import math

file_open = open('1.txt')
file_print = file_open.read()

data = list(file_print)
print(data)

l = len(data)
print(l)

set_list = set(data)
set_list = (list(set_list))

for item in set_list:
	ver = data.count(item)
	cnt = ver/l
	logver = math.log2(cnt)
entropy = -logver
print(entropy)

file_open.close