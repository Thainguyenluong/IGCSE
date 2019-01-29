def compress():
    count=[]
#data=["A","A","A","C","C","D","E","E","A","A"]
    data=input("Enter:")
    tempcount=1



    for i in range(len(data)-1):
        char=data[i]
        if char==data[i+1]:
            tempcount=tempcount+1
        elif char!=data[i+1]:
            count.append(char)
            count.append(str(tempcount))
            tempcount=1
    count.append(data[i+1])
    count.append(str(tempcount))  #Add the last type of character


    print(*count)
def decompress():
    count=[]
    text=input("Enter string:")
    for i in range(int(len(text)/2)):
        a=text[i*2]
        b=int(text[i*2+1])
        for c  in range(b):
            count.append(a)
    print(*count)


decompress()






