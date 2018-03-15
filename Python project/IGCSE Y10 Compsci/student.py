student=int(input("Input number of students:"))
score=[]
name=[]

for i in range(student):
    a=str(input("Name:"))
    name.append(a)
    b=str(input("Score:"))
    score.append(b)
for a in score:
    bigNum=score[0]
    if a>bigNum:
        a=bigNum
        h=name[score.index(bigNum)]
print("High score student is:",h)
#what happen if 2 students got same high score







