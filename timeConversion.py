t12 = input()
t24=''
ll = t12[8:]

if(ll=='PM'):
    if(t12[:2]=='12'):
        t24 = "12" + t12[2:8]
    else:
        timeConv = int(t12[:2])
        timeConv = timeConv + 12
        t24 = str(timeConv) + t12[2:8]
elif(ll=='AM'):
    if(t12[:2]=='12'):
        t24 = "00"+t12[2:8]
    else:
        t24 = t12[:8]

print(t24)