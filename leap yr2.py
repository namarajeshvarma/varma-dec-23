year=int(input("enter the year fpr checking"))
if (year%4==0) and (year%400==0) :
    print("leap year")
if (year%4==0) and (year%100!=0):
     print("leap year")
else:
    print("non leap year")
