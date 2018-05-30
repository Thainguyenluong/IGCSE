students=["Dung","Thai","Vu","Minh","An"]
for x in range(len(students)):
    for c in range(x):
        if students[c]<students[c+1]:
            temp=students[c]
            students[c]=students[c+1]
            students[c+1]=temp
print(*students[::-1])








