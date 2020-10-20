def DataCollector(strData):
    originalData = []
    TempData = strData.split()
    for i in TempData:
        originalData.append(int(i))
    return originalData

x = int(input())
data = DataCollector(input())
print(sum(data))