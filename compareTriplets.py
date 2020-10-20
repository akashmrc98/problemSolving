def DataCollector(strData):
    originalData = []
    TempData = strData.split()
    for i in TempData:
        originalData.append(int(i))
    return originalData

def compare(a, b):
    winList = [0, 0]
    for i in range(0, len(a)):
        if(a[i]>b[i]):
            winList[0]=winList[0]+1
        elif(b[i]>a[i]):
            winList[1]=winList[1]+1
    return ' '.join(map(str, winList)) 

a = DataCollector(input())
b = DataCollector(input())

print(compare(a,b))