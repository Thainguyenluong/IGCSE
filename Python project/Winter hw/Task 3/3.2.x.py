def asknum():
    a=int(input("Enter a number:"))
    b=int(input("Enter another number:"))
    sum=a+b
    print("The sum is:",sum)
asknum()

e=int(input("Enter a number:"))
f=int(input("Enter another number:"))
def product():
    p=e*f
    print("Product of the 2 numbers:",p)
def subtract():
    s=e-f
    print("First number-second number=",s)
def divide():
    d=e/f
    print("First number/secondnumber=:",d)
    if f==0:
        print("Invalid.")
product()
subtract()
divide()


def product2():
    g=int(input("Enter a number:"))
    h=int(input("Enter another number:"))
    r=g*h
    print("Product=",r)
def add():
    x=int(input("Enter a number:"))
    y=int(input("Enter another number:"))
    o=x+y
    print("Sum=",o)
def sqrt():
    z=int(input("Enter a number"))
    m=z**(1/2)
    print("Square root of",z,"=",m)



def menu_function():
    ask=input("Add or multiply or square root or finish :")
    ask=ask.lower()
    if ask=="add":
        add()
    if ask=="multiply":
        product2()
    if ask=="square root":
        sqrt()
    if ask=="finish":
        exit
menu_function()



















