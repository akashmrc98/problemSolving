def DataCollector(strData):
    originalData = []
    TempData = strData.split()
    for i in TempData:
        originalData.append(int(i))
    return originalData

x = int(input())
data = DataCollector(input())

ratioList = [0,0,0]

for i in data:
    if i > 0:
        ratioList[0] = ratioList[0]+1
    elif i < 0:
        ratioList[1] = ratioList[1]+1
    elif i == 0:
        ratioList[2] = ratioList[2]+1

newRatioList = []
for j in ratioList:
    newRatioList.append(j/x);

for k in newRatioList:
    print(k)