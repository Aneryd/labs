
from math import *

a = float(input("Введите a: "))
x = float(input("Введите x: "))
fun = str(input("Введите ф-ию которую вы хотите вычислить( g, f, y): "))
p = int(input('Сколько считать '))
sh = float(input('С каким шагом?: '))

if (fun == 'g'):
    for i in range(p):
        g = (-1 * (2 * (-5 * a**2 + 3 * a * x + 2 * x**2) / (5 * a**2 + 9 * a * x - 2 * x**2)))
        if (5*a**2 + 9*a*x - 2*x**2) == 0:
            print('ERROR')
        else:    
            print(g)
            print()
            a += sh
        
elif (fun == 'f'):
    for i in range(p):
        f = (sin(pi * (10 * a**2 + 37 * a * x + 7 * x**2)))
        if  (a == 0):
           print('ERROR') 
        else:
            print(f)
            a += sh

elif (fun == 'y'):
    for i in range(p):
        y = (log(-5 * a**2 - 16 * a * x + 16 * x**2 + 1) / log(2))
        print(y)
        a += sh
else:
    print("ERROR")
