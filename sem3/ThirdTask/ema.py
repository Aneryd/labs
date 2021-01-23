import openpyxl

wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.active
a = []
for cell in sheet['A']:
    a.append(cell.value)
del a[0]
print(a)
a.sort()
print(a)


b = len(a)
ema = []
ema1=1
F=2/(9)

for i in range(b):
    ema1=a[i]+(1-F)*ema1
    print()
    print(ema1)
    print()
    ema.append(ema1)
print(ema)