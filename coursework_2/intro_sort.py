# import numpy
import math
import random

mass = []
# mass = numpy.random.random_integers(1, 1000+1, 100)
for i in range(0, 1000, 1):
	mass.append(random.randint(1, 1000))

def introSort(mass, a):
	b = len(mass)

	if b <= 1:
		return

	elif a == 0:
		heapSort(mass)

	else:
		p = part(mass)
		mass_1 = mass[:p]
		mass_2 = mass[p+1:b]
		introSort(mass_1, a-1)
		introSort(mass_2, a-1)

		for i in range(0, len(mass_1)):
			mass.insert(i, mass_1[i])
			mass.pop(i + 1)

		for i in range(0, len(mass_2) - 1):
			mass.insert(i + p + 1, mass_2[i])
			mass.pop(i + p + 2)

def heapSort(mass):
	END = len(mass)

	for i in range(int(math.floor(END / 2)) - 1, -1, -1):
		heap(mass, END, i)

	for i in range(END, 1, -1):
		swap(mass, 0, i - 1)
		heap(mass, i - 1, 0)

def part(mass):
	h = len(mass) - 1
	x = mass[h]
	i = 0

	for j in range(0, h - 1):
		if mass[j] <= x:
			swap(mass, i, j)
			i += 1
	swap(mass, i, h)
	return i

def swap(mass, j, i):
	temp = mass[i]
	mass[i] = mass[j]
	mass[j] = temp

def heap(mass, end, root):
	L = 2 * root + 1
	R = 2 * root + 2

	if R < end:
		if (mass[root] >= mass[L] and mass[root] >= mass[R]):
			return

		else:
			if(mass[L] > mass[R]):
				j = L

			else:
				j = R

			swap(mass, root, j)
			heap(mass, end, j)

	elif L < end:
		if(mass[root] >= mass[L]):
			return

		else:
			swap(mass, root, L)
			heap(mass, end, L)

	else:
		return

for i in range(0, 1000, 1):
	print(introSort(mass, 2))
