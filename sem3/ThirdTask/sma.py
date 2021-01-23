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
sma = []
sum = 0
count=0
count2=4

for i in range(4, b):
    for j in range(count, count2):
        print(j)
        sum += a[j]
    print()
    print(sum)
    print()
    count+=1
    count2+=1
    mid = sum/4
    sma.append(mid)
print(sma)