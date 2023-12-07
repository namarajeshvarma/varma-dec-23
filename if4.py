a=int(input("enter the triangle side in "))
b=int(input("enter the triangle side 2"))
c=int(input("enter the triangle of side 3"))
if a==b==c:
   print("equilent triangle")
elif a==b or b==c or c==a:
    print("isoscele triangle")
else:
    print("scalen triangle")