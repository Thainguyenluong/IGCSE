booknum=str(input("Give 13 digit ISBN :"))

def isbn():
    global x
    global booknum
    global total
    global modulo
    global checkdigit
    total=0

    if len(booknum)!=13:
        return False
    else:
        for x in range(len(booknum)-1):
            if x%2==0:
                total=total+int(booknum[x])*1
            elif x%2!=0:
                total=total+int(booknum[x])*3
    modulo=total%10
    checkdigit=10-modulo
    if checkdigit==int(booknum[12]):
                print("True")
    elif checkdigit!=int(booknum[12]):
                print("False")
def calCheckDigit():
    global booknum
    booknum2=str(input("Give me missing ISBN:"))
    global x
    global miscalnum

    global total2
    global modulo2
    global adddigit
    total2=0

    if len(booknum2)!=12:
        return False
    else:
        for x in range(len(booknum2)):
            if x%2!=0:
                total2=total2+int(booknum2[x])*1
            elif x%2==0:
                total2=total2+int(booknum2[x])*3
    modulo2=total2%10
    adddigit=10-modulo
    miscalnum=int(booknum2)*10+adddigit
    print(adddigit)
    print("Total2:",total2)

    print(miscalnum)
def calcMissing():
    global isbn
    global total3
    isbn=str(input("Enter ISBN number with ? at missing letter:"))
    total3=0
    for c in range(len(isbn)-1):
            if isbn[c]=="?":
                continue
            if c%2!=0:
                total3=total3+int(isbn[c])*1
            elif c%2==0:
                total3=total3+int(isbn[c])*3

    print(total3)









isbn()
calCheckDigit()
calcMissing()


