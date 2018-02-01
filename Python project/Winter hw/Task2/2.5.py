

count=0
for number in list(range(1,101)):
    if number%3==0:
        count=count+1
    else:
        count=count+0
print("Numbers from 1 to 100 that is divisible to 3 are:",count)


count1=0
for num in range(1,21):
    prime=True
    if num==1:
        prime=False
    for i in range(2,num):
        if num%i == 0:
            prime=False
    if prime== True:
        count1=count1+1

print("Number of prime numbers from 1 to 20 are:",count1)







