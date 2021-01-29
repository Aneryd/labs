import openpyxl
import numpy as np

wb = openpyxl.load_workbook('data1.xlsx')
sheet = wb.active
spisok = []
for cell in sheet['A']:
    spisok.append(cell.value)



mid = 0
b = len(spisok)
mediana = []
count=0
count2=2

for i in range(b-1):
    temp = []
    for j in range(count, count2):
        temp.append(spisok[j])
    np.sort(temp)
    mid = temp[1]
    del temp
    file = open('medianadata.txt', 'a')
    file.write(str(mid) + '\n')
    count+=1
    count2+=1