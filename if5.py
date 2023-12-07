units=int(input("enter ur units"))
bill=0
if units<=100:
    bill =0
    print("for usage of 100 units its free")
elif units>=100 and units<=300:
    bill =(units-100)*2
    print(bill)
elif units>=300:
    bill=400+(units-300)*5
    print(bill)