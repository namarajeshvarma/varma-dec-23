size=input("what size pizza do u want (s/m/l)  ")
bill=0
if size=='S' or size=='s':
    bill +=100
    print("for small size pay 100")
elif size=='M' or size=='m':
    bill +=200
    print("for medium size pay 200")
else:
    bill +=300
    print("for large size pay 300")
add_pepperoni=input("do u wnt add pepporani (y/n)")
if add_pepperoni=='y' or add_pepperoni=='Y':
    if size=='S' or size=='s':
         bill +=30
    else:
         bill +=50
print(f"your total bill is {bill}")
