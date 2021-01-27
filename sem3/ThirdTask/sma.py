import openpyxl

wb = openpyxl.load_workbook('data1.xlsx')
sheet = wb.active
a = []
for cell in sheet['A']:
    a.append(cell.value)
del a[0]
print(a)



b = len(a)
sma = []
sum = 0
count=0
count2=4

for i in range(4, b):
    for j in range(count, count2):
        sum += a[j]
    count+=1
    count2+=1
    mid = sum/4
    sum=0
    sma.append(mid)
    file = open('smadata.txt', 'a')
    file.write(str(mid) + '\n')
print(sma)