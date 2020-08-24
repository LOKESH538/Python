"""Tax Calculator
   Ask the user for their monthly salary. Calculate whether they have to pay tax and if so,
   how much is that amount .Print the result."""

salary=int(input("Enter the salary : "))
if (salary>=0) and (salary<=250000):
    tax=(salary*0)
elif (salary>250000) and (salary<=500000):
    tax=(salary*0.05)
elif (salary>500000) and (salary<=750000):
    tax=(salary*0.1)
elif (salary>750000) and (salary<=1000000):
    tax=(salary*0.15)
elif (salary>1000000) and (salary<=1250000):
    tax=(salary*0.2)
elif (salary>1250000) and (salary<=1500000):
    tax=(salary*0.25)
else:
    tax=(salary*0.3)
print("Tax is : ",tax)
