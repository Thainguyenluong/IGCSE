def hav():
    lat=float(input("Enter latitude:"))
    direction=input("N or S:")
    long=float(input("Enter longitude:"))
    direction2=input("W or E:")
    direction=direction.upper()
    direction2=direction2.upper()
    if direction=="S":
        lat=lat*-1
    if direction2=="W":
        long=long*-1
    import math
    from math import radians
    hnlat=21.0278
    hnlong=105.83
    r=6371
    lat,long,hnlat,hnlong=map(radians,[lat,long,hnlat,hnlong])

    latdif=lat-hnlat
    longdif=long-hnlong
    d= 2*r*math.asin((math.sin(latdif/2))**2+math.cos(lat)*math.cos(lat)*(math.sin(longdif/2))**2)**0.5
    d=round(d,2)
    print(d)

hav()
