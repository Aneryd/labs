import numpy


mass = numpy.random.random_integers(1, 1000+1, 100)

def select(mass):
	for i in range(len(mass)):
		index = i
		for j in range(i+1, len(mass)):
			if mass[j] < mass[index]:
				index = j
			mass[i], mass[index] = mass[index], mass[i]
	return mass