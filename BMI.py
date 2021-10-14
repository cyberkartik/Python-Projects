#To get the weight and height of a person for calculating the BMI value and appropriate interpretation
height=float(input("Enter your height in cms:"))
weight=float(input("Enter your weight in kgs:"))
BMI=weight/(height/100)**2
print("Your BMI is", BMI, "kg/m^2")
if BMI<=16:
    print("You are seriously underweight")
elif 16<BMI<18:
    print("You are underweight")
elif 18<BMI<24:
    print("You have a normal weight")
elif 24<BMI<29:
    print("You are overweight")
elif 29<BMI<35:
    print("You are seriously overweight")
else:
    print("You are gravely overweight ")
