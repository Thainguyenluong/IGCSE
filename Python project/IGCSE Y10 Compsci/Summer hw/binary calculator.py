def choice():
    choice=input("Press 1 for binary to denary, press 2 for denary to binary:")
    choice=choice.lower()
    if choice=="2":
        denary()
    elif choice=="1":
        binary()

def binary():
    binary=str(input("Enter a binary number:"))
    a=binary[::-1]
    count=0
    for i in range(len(a)):
        if a[i]=="1":
            count=count+(2**i)
        elif a[i]=="0":
            count=count+0
    print(count)
def denary():
    num=int(input("Enter a denary number:"))
    binary=[]
    while num>=1:
        if num%2==0:
            binary.append("0")
            num=int(num/2)
        if num%2==1:
            binary.append("1")
            num=int(num/2)
    print(*binary[::-1])
while True:
    choice()


