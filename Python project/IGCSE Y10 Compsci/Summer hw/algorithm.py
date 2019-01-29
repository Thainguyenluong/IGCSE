global countodd
global counteven
def upc():
    while True:
        try:
            upc=int(input("Enter a 12-digit number:"))
            break
        except ValueError:
            print("Incorrect value")
    upc=str(upc)
    if len(upc)!=12:
        print("Incorrect length")
    countodd=0
    counteven=0
    for i in range(len(upc)-1):
            if i%2==0:
                countodd=countodd+int(upc[i])
            elif i%2!=0:
                counteven=counteven+int(upc[i])
    checksum=(countodd*3)+counteven
    checkdigit=10-(checksum%10)
    if checkdigit==int(upc[11]):
        print("correct")
    elif checkdigit!=int(upc[11]):
        print("Incorrect")
def isbn13():
    while True:
        try:
            isbn13=int(input("Give 13 digit ISBN :"))
            break
        except ValueError:
            print("Incorrect Value")
    isbn13=str(isbn13)
    total=0
    if len(isbn13)!=13:
        return False
    else:
        for x in range(len(isbn13)-1):
            if x%2==0:
                total=total+int(isbn13[x])*1
            elif x%2!=0:
                total=total+int(isbn13[x])*3
    modulo=total%10
    checkdigit=10-modulo
    if checkdigit==int(isbn13[12]):
                print("True")
    elif checkdigit!=int(isbn13[12]):
                print("False")

def isbn10():
    while True:
        try:
            isbn10=int(input("Enter a 10-digit number:"))
            break
        except ValueError:
            print("Incorrect value")
    isbn10=str(isbn10)
    if len(isbn10)!=9:
        print(len(isbn10))
        print("Incorrect length")
    isbn=isbn10[::-1]
    count=0
    for i in range(len(isbn)):
        count=count+(int(isbn[i]))*(i+1)
    if count%11==0:
        print("Correct")
    else:
        print("Incorrect")

choice=input("Upc,Isbn10 or Isbn13")
choice=choice.lower()
if choice=="upc":
    upc()
if choice =="isbn10":
    isbn10()
if choice=="isbn13":
    isbn13()


