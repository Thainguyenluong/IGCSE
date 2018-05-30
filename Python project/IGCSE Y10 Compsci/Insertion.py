Array=["Dung","Thai","Vu","Minh","An"]
for i in range(len(Array)):
    y=Array[i]
    x=i-1
    while x>=0 and Array[x]>y:
        Array[x+1]=Array[x]
        x=x-1
    Array[x+1]=y
print(Array)
