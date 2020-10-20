def SumFinder(strData):
    TempData = strData.split()
    totSum = 0
    for i in TempData:
        totSum = totSum + int(i)
    return totSum

x = int(input())
print(SumFinder(input()))