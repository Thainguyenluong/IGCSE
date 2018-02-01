score =0
q1 = input("What's 1+1=?")
if q1 == "2":
    print("Correct")
    score=score+1
elif q1!=2:
    print("retake grade 1")
    score=score-1

q2=input("When did D-day start?Fill in the gaps _/_ /_")

if q2 == "6/6/1944":
    print("You have good historical knowledge.")
    score=score+1
else:
    print("study more")
    score=score-1

q3=input("what is the formula for the area of a triangle?")
q3=q3.lower()
if q3 == "1/2bh" or q3 == "1/2absinC":
    print("Correct")
    score=score+1
else:
    print("study your notes again")
    score=score-1
q4= input("What is the fastest mammal on land?")
q4=q4.lower()
if q4 == "cheetah":
    print("Correct")
    score=score+1
else:
    score=score-1
print("Score=",score,"over 4")
