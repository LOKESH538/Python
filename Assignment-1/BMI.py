""" write a program that prompts the user to enter a weight in pounds and height in inches and displays the BMI. """

weight=float(input("Weight (in pounds) :"))
height=float(input("Height (in inches) :"))
w=weight*0.45359237
h=height*0.0254
BMI=w/(h**2)
print("BMI =",BMI)
if BMI <18.5:
    print("Under Weight")
if BMI>=18.5 and BMI<25.0:
    print("Normal")
if BMI >=25.0 and BMI <30.0:
    print("Over Weight")
if BMI >=30.0:
    print("Obese")
