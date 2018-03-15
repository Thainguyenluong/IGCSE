global ground
global currentfloor
import math

ground=1
distance=0
time=0

def callLift():
    global ground
    global currentfloor
    global x
    global distance
    global z
    currentfloor=int(input("Enter current floor:"))
    if 0<currentfloor<11:
        global time
        time=time+1
        if currentfloor>ground:
            x=abs(currentfloor-ground)
            distance=distance+x
            for i in range(ground,currentfloor+1):
                print(i)

        if currentfloor<ground:
            global y
            y=abs(ground-floor)
            distance=distance+y
            for i in range(ground,currentfloor,-1):
                print(i)
    else:
        z=distance/time
        print("There's no such floor")
        print("Number of journeys:",time)
        print("Average distance:",round(z,2))
        exit()

def setDestination():
    global floor
    floor=int(input("Enter floor:"))
    if floor>=11:
        z=distance/time
        print("Floor invalid")
        print("Number of journeys:",time)
        print("Average distance:",round(z,2))
        exit()
    if floor<=0:
        z=distance/time
        print("Floor invalid")
        print("Number of journeys:",time)
        print("Average distance:",round(z,2))
        exit()
    if floor==currentfloor:
        z=distance/time
        print("You're in the same floor idiot.")
        print("Number of journeys:",time)
        print("Average distance:",round(z,2))
        exit()


def moveUp():
    global distance
    global currentfloor
    currentfloor=currentfloor+1
    distance=distance+1

    print(currentfloor)
def moveDown():
    global currentfloor
    global distance
    currentfloor=currentfloor-1
    distance=distance+1
    print(currentfloor)
while True:
    callLift()
    setDestination()
    if 0<floor<11 and 0<currentfloor<11 and floor!=currentfloor:
        time=time+1
        if currentfloor<floor:
            for a in range(int(floor-currentfloor)):
                moveUp()

        if currentfloor>floor:
            for b in range(currentfloor-floor):
                moveDown()
        if floor==currentfloor:
                print("You're here. Watch your step.")
                ground=floor




