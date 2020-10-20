def ProfGradRules(Arr):
    results = []
    for i in Arr:
        temp = i
        while(i%5!=0):
            if(i-temp < 3):
                results.append(i)
        else:
            results.append(i)
            

x = int(input())
data = []
for i range(0, x):
    data.append(input())

ProfGradRules(data)
