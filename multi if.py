h=int(input("enter height meters"))
bill=0
if h>=3:
    print("you can ride")
    age = int(input("enter ur age"))
    if age<12:
        bill=150
        print(f"pay {bill}")
    elif age<=18:
        bill=250
        print(f"pay {bill}")
    else:
        bill=500
        print(f"pay {bill}")
    want_photo=input("do u want photo pls press y")
    if want_photo=='y'or want_photo=='Y':
         bill=bill+50
    print(f"ur total bill is {bill}")
else:
    print("u can't ride")
print("thank you")
