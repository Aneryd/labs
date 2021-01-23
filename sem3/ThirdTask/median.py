import openpyxl

wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.active
spisok = []
for cell in sheet['A']:
    spisok.append(cell.value)
print(spisok)
spisok.sort()
print(spisok)

b = len(spisok)
mediana = []

for i in range(b-1):
    mediana.append(spisok[i+1])
print('Median filter =',mediana)