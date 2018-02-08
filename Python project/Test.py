print('Roman numerals equivalent to numbers from 1 to 3999.Python cannot print 4000 or up in Roman numerals.')
Roman=str(input("Enter a roman numeral:"))
num=0
length = len(Roman)
for i in range(0,length):
    if Roman =="":
        print("you haven't put anything.")
    if Roman[i]=="M":
        print("step ",i)
        num=num+1000
        print(num)
    elif Roman.find("C")+1==Roman.find("M"):
            print("step ",i)
            num=num-100
            print(num)
    elif Roman[i]=="D":
      num=num+500
      print(num)
    elif Roman[i]=="C" and Roman[i+1]=="D" :
        num=num-100
        print(num)
    elif Roman[i]=="C":
        print("step ",i)
        num=num+100
        print(num)
    elif Roman.find("C")-1==Roman.find("X"):
        num=num-10
        print(num)
    elif Roman[i]=="L":
        print("step",i)
        num=num+50
        print(num)
    elif Roman.find("X")+1==Roman.find("L"):
        print("step",i)
        num=num-10
        print(num)
    elif Roman[i]=="X":
        num=num+10
        print(num)
    elif Roman.find("I")+1==Roman.find("X"):
        num=num-1
        print(num)
    elif Roman[i]=="V":
        num=num+5
        print(num)
    elif Roman.find("I")+1==Roman.find("V"):
        num=num-1
        print(num)
    elif Roman[i]=="I":
        num=num+1
        print(num)
print(num)
print(Roman)

