count=[]
data=["A","A","A","C","C","D","E","E","A","A"]
tempcount=1



for i in range(len(data)-1):
    char=data[i]
    if char==data[i+1]:
        tempcount=tempcount+1
    elif char!=data[i+1]:
        count.append(char)
        count.append(str(tempcount))
        tempcount=1
count.append(char)
count.append(str(tempcount))  #Add the last type of character


print(*count)







