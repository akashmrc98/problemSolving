def DataCollector(strData):
    originalData = []
    TempData = strData.split()
    for i in TempData:
        originalData.append(int(i))
    return originalData

x = int(input())
matrix = []

for i in range(0,x):
    matrix.append(DataCollector(input()))

d1 = 0
d2 = 0

for i in range(0,len(matrix)):
    d1 = d1 + matrix[i][i]
    d2 = d2 + matrix[i][len(matrix)-(i+1)]

print(abs(d1-d2))