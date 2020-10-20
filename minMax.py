def DataCollector(strData):
    originalData = []
    TempData = strData.split()
    for i in TempData:
        originalData.append(int(i))
    return originalData

def Carrier(arr, skipValue):
    carry = 0
    for i in range(0, len(arr)):
        if i == skipValue:
            continue
        else:
            carry = carry + arr[i]
    return carry

def MinMaxFinder(arr):
    sumList = []
    for i in range(0, len(arr)):
        sumList.append(Carrier(arr, i))
    return sumList

x = MinMaxFinder(DataCollector(input()))
print(min(x), max(x))
