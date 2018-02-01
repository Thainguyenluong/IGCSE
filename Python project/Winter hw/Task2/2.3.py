number1=int(input("Enter an integer:"))
number2=int(input("Enter another integer:"))
number3=int(input("Enter another integer:"))

if number1>number2 and number1>number3:
    print("Largest number:",number1)
elif number2>1 and number2>number3:
    print("Largest number:",number2)
elif number3>number1 and number3>number2:
    print("Largest number:",number3)
elif number1== number2== number3:
    print("Three numbers are equal.")
