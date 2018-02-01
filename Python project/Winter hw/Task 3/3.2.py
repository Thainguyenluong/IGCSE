print('Roman numerals equivalent to numbers from 1 to 3999.Python cannot print 4000 or up in Roman numerals.')
Roman=str(input("Enter a roman numeral:"))
num=0
length = len(Roman)
for i in range(0,length):
    if i<=length:
        if Roman[i]=="M":
            num=num+1000
        elif Roman[i]=="D":
            num=num+500
        elif Roman[i]=="C":
            num=num+100
        elif Roman[i]=="L":
            num=num+50
        elif Roman[i]=="X":
            num=num+10
        elif Roman[i]=="V":
            num=num+5
        elif Roman[i]=="I":
            num=num+1
    if i<length-1:
        if Roman[i]=="C"and Roman[i+1]=="M":
            num=num-200
        if Roman[i]=="C" and Roman[i+1]=="D":
            num=num-200
        if Roman[i]=="X"and Roman[i+1]=="C":
            num=num-20
        if Roman[i]=="X"and Roman[i+1]=="L":
            num=num-20
        if Roman[i]=="I" and Roman[i+1]=="X":
            num=num-2
        if Roman[i]=="I" and Roman[i+1]=="V":
            num=num-2
    elif i>length-1:
        print("Out of range")



print(num)
print(Roman)



