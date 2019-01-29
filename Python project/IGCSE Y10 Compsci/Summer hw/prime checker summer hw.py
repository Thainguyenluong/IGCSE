num=int(input("Input a number:"))

def primecheck():
    prime=True
    if num<0:
        print("Not prime.")
    if num==1 or num==2:
        print("Not prime.")
    if num==2:
        print("Prime")
    for i in range(2,num):
        if num%i!=0 and i<num:
            i=i+1
        if num%i==0 and i<num:
            prime=False
            print("Not prime")
            break
        if i==num and prime==True:
            print("Prime")
primecheck()

