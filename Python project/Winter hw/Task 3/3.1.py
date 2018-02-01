
num=int(input("Enter a year:"))
Roman=str("")
while ( num<=0 or num>=10000):
    print("Out of range. Enter another year.")
    num=int(input("Enter a year:"))

if (num//5000 ==1):
    Roman=Roman+"V_"
    num=num-5000

if (num//4000 ==1):
    Roman=Roman+"IV_"
    num=num-4000

count = num//1000
for a in range(1,count+1):
    Roman=Roman+"M"
    num=num-1000
if num//900==1:
    Roman=Roman+"CM"
    num=num-900
if num//500==1:
    Roman=Roman+"D"
    num=num-500
if num//400==1:
    Roman=Roman+"CD"
    num=num-400
count= num//100
for b in range(1,count+1):
    Roman=Roman+"C"
    num=num-100
if num//90==1:
    Roman=Roman+"XC"
    num=num-90
if num//50==1:
    Roman=Roman+"L"
    num=num-50
if num//40==1:
    Roman=Roman+"VL"
    num=num-40
count=num//10
for c in range(1,count+1):
    Roman=Roman+"X"
    num=num-10
if num//9==1:
    Roman=Roman+"IX"
    num=num-9
if num//5==1:
    Roman=Roman+"V"
    num=num-5
if num//4==1:
    Roman=Roman+"IV"
    num=num-4

count=num//1
for d in range(1,count+1):
    Roman=Roman+"I"
    num=num-1




print(Roman)

























