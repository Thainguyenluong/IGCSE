import time
found=False
file=open("passwords.txt","r")
password=[""]
for passlist in file:
    passlist=passlist.strip("\n")
    password.append(passlist)
file.close()

word=input("What is your password?")
start=time.time()
for i in range(len(password)):
    if password[i]==word:
        print("Password is found.")
        print("Your password is found at:",i+1)
        found=True
        print(time.time()-start,"seconds")
        break
if not found:
            print("Not found")





