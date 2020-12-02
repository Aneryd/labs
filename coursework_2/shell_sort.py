import numpy


mass = numpy.random.random_integers(1, 1000+1, 100)

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