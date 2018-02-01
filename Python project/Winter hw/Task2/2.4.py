myList = [2,1,4,5,1,6,87,1,9,43]
biggestNumber = 0
for eachNumber in myList:

    if eachNumber > biggestNumber:

        biggestNumber = eachNumber



print("Biggest number:",biggestNumber)

smallestnum=biggestNumber
for eachNumber in myList:
    if eachNumber<smallestnum:
        smallestnum=eachNumber
print("Smallest number:",smallestnum)

count=0
for eachNumber in myList:
    if eachNumber==1:
        count=count+1
    else:
        count=count+0
print("Number of 1s are:",count)

sum= sum(myList)
print("Sum:",sum)

count1=0
for eachNumber in myList:
    count1=count1+1
Average=sum/count1
print("Average:",Average)

