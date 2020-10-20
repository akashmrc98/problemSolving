x = int(input())
data = list(map(int, input().rstrip().split()))

def BirthDayCandles(Arr):
    count=0
    big = max(Arr)
    for i in range(len(Arr)):
        if(Arr[i]==big):
            count+=1
    return count

print(BirthDayCandles(data))