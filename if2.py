sal=int(input("enter u r salary"))
exp=int(input("enter u r experience"))
if exp >10:
    b=sal*10/100
if exp >=6 and exp <=10:
    b=sal%8/100
if exp <6:
    b=sal*5/100
print(f"bonus is {b}")
print(sal+b)













