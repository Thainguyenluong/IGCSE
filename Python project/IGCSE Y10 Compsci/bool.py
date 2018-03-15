floor=["1","2","3","4","5","6","7","8","9","10"]
destination=input("Enter floor:")
global current
current=False
boolfloor=[]

for eachfloor in floor:
    if destination==eachfloor:
        current=True
        boolfloor.append("True")
    else:
        current=False
        boolfloor.append("False")
print(boolfloor)

