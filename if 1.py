units=int(input("enter the unites  u r used"))
bill=0
if units<=100:
    bill=0
if (units>100)and(units<=200):
    bill=(units-100)*5
if units>200:
    bill=500+(units-200)*10
print(f"total bill amout is rs{bill}")

