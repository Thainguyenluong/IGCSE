mess=[1,0,1,0,1,1,0,0]
check=input("Even or odd:")
count=0
for i in range(len(mess)):
    if mess[i]==1:
        count=count+1
    elif mess[i]==0:
        count=count+0
if check=="even":
    if count%2==0:
        mess.append(0)
        print(mess)
    elif count%2!=0:
        mess.insert(0,1)
        print(mess)
else:
    if count%2!=0:
        mess.append(0)
        print(mess)
    elif count%2==0:
        mess.insert(0,1)
        print(mess)


