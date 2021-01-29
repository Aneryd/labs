import openpyxl

wb = openpyxl.load_workbook('data1.xlsx')
sheet = wb.active

a = []

for cell in sheet['A']:
    a.append(cell.value)
del a[0]

b = len(a)
ema = []
ema1= a[1]
F=2/(9)

for i in range(b):
    ema1=a[i]+(1-F)*ema1
    ema.append(ema1)
    file = open('emadata.txt', 'a')
    file.write(str(ema1) + '\n')
print(ema)