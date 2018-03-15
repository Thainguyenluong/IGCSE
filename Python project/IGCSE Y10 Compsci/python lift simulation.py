

global ground
global currentfloor
ground=1

def callLift():
    global ground
    global currentfloor
    currentfloor=int(input("Enter current floor:"))
    if 0<currentfloor<11:
        if currentfloor>ground:
            for i in range(ground,currentfloor+1):
                print(i)
        if currentfloor<ground:
            for i in range(ground,currentfloor,-1):
                print(i)
    else:
        print("There's no such floor")
        exit()

def setDestination():
    global floor
    floor=int(input("Enter floor:"))
    if floor>=11:
        print("Floor invalid")
        floor=int(input("Enter floor:"))
    if floor<=0:
        print("Floor invalid")
        floor=int(input("Enter floor:"))
    if floor==currentfloor:
        print("You're in the same floor idiot.")
        floor=int(input("Enter floor:"))


def moveUp():
    global currentfloor
    currentfloor=currentfloor+1
    print(currentfloor)
def moveDown():
    global currentfloor
    currentfloor=currentfloor-1
    print(currentfloor)
while True:
    callLift()
    setDestination()
    if 0<floor<11 and 0<currentfloor<11 and floor!=currentfloor:
        if currentfloor<floor:
            for a in range(int(floor-currentfloor)):
                moveUp()

        if currentfloor>floor:
            for b in range(currentfloor-floor):
                moveDown()
        if floor==currentfloor:
                print("You're here. Watch your step.")
                ground=floor

