yearlist=[230,1999,2018,4096,1986,2020,512,2054,1837,1945,1360,3000,2048,1066,4,930,1024,32]
import datetime
now=datetime.datetime.now()
def leap():
    if year<now:
        if year%4==0 and year%100!=0:
                print("This is a leap year.")
        elif year%4==0 and year%100==0 and year%400==0:
            print("This is a leap year.")

    else:
        print("This is not a leap year.")
for year in yearlist:
    leap()




