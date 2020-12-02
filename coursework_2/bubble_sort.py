import numpy


mass = numpy.random.random_integers(1, 1000+1, 100)

def bubble_sort(mass):
	for i in range(len(mass)-1):
		for j in range(len(mass)-1-i):
			if mass[j] > mass[j+1]:
				mass[j], mass[j+1] = mass[j+1], mass[j]
	return mass

bubble_sort(mass)