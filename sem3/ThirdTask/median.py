import openpyxl

wb = openpyxl.load_workbook('data1.xlsx')
sheet = wb.active
spisok = []
for cell in sheet['A']:
    spisok.append(cell.value)
del spisok[0]


mid = 0
b = len(spisok)
mediana = []
count=0
count2=2

for i in range(b-1):
    for j in range(count, count2):
        mediana.append(spisok[j+1])
        mid = spisok[j+1]
        break
    file = open('medianadata.txt', 'a')
    file.write(str(mid) + '\n')
    count+=1
    count2+=1