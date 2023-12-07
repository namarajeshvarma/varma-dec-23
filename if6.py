days=int(input("enter days u have used"))
bill=0
if days<=2:
    bill =days*2
elif days >=6 and days<=10:
    bill =(days-5)*3
elif days >=11 and days<=15:
    bill =25+(days-10)*4
else :
    days>15
    bill=45+(days-15)*5
print(bill)









