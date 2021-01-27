import math

mass = []
k = 1

def file():
	file_open = open('newfile.txt')
	file_print = file_open.read()
	return file_print

def count(message):
	file_s = list(message)

	array_d = {}.fromkeys(file_s, 0)
	for a in file_s:
		array_d[a] += 1
	return array_d.values()

def ent(message):
	return -sum([i/len(message)*math.log2(i/len(message)) for i in count(message)])

text = file()
print(text)
print(ent(text))