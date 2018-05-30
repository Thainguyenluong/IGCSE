Array=["A","A","B","A","C","C","B"]
count=[0,0,0]
for Letter in Array:
    if Letter=="A":
        count[0]=count[0]+1
    if Letter=="B":
        count[1]=count[1]+1
    if Letter=="C":
        count[2]=count[2]+1
print(count)





