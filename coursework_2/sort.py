import numpy

# mass = [1, 3, 2, 9, 4, 5, 0]
mass = numpy.random.random_integers(1, 1000+1, 100)
m = []

def bubble(mass):
	for i in range(len(mass)-1):
		for j in range(len(mass)-1-i):
			if mass[j] > mass[j+1]:
				mass[j], mass[j+1] = mass[j+1], mass[j]
	return mass

def shell(mass):
    inc = len(mass) // 2
    while inc:
        for i, el in enumerate(mass):
            while i >= inc and mass[i - inc] > el:
                mass[i] = mass[i - inc]
                i -= inc
            mass[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return mass

def select(mass):
	for i in range(len(mass)):
		index = i
		for j in range(i+1, len(mass)):
			if mass[j] < mass[index]:
				index = j
			mass[i], mass[index] = mass[index], mass[i]
	return mass

def introsort(mass):
	
	for i in range(len(mass) // 2):
		heapSort(mass)

	return mass

def heapinit(mass, n, i):
	lar = i
	l = 2*i+1
	r = 2*i+2

	if (l < n and mass[i] < mass[l]):
		lar = l

	if (r < n and mass[lar] < mass[r]):
		lar = r

	if lar != i:
		mass[i], mass[lar] = mass[lar], mass[i]

		heapinit(mass, n, lar)

def heapSort(mass):
	n = len(mass)

	for i in range(n, -1, -1):
		heapinit(mass, n, i)

	for i in range(n-1, 0, -1):
		mass[i], mass[0] = mass[0], mass[i]
		heapinit(mass, i, 0)

print("Сортировка пузырьком:" + " " + str(bubble(mass)))
print("Сортировка Шелла:" + " " + str(shell(mass)))
print("Сортировка выбором:" + " " + str(select(mass)))
print("Сортировка heapsort" + ' ' + str(introsort(mass)))
