w=float(input("enter weight in kg"))
h=float(input("enter height inmeters"))
bmi=round(w/h**2)
if bmi<18.5:
    print(f" ypur bmi is{bmi} and u r under weight")
elif bmi<25:
    print(f" ypur bmi is{bmi} and u r normal ")
elif bmi<30:
    print(f" ypur bmi is{bmi} and ur overr weight")
elif bmi<35:
    print(f" ypur bmi is{bmi} and u r obese weight")
else:
    print(f" ypur bmi is{bmi} and u r clinically obese")