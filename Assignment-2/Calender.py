"""  Write a program that reads a date from the user and computes its immediate successor.The date is the format YYYY-MM-DD. So, 2020-04-15
 will have the successor 2020-04-16."""

year=int(input("Enter a year : "))
if year%400== 0:
    leapyear=True
elif year%100==0:
    leapyear=False
elif year%4==0:
    leapyear=True
else:
    leapyear=False
month=int(input("Enter a month between 1 to 12 : "))
if month in (1, 3, 5, 7, 8, 10, 12):
    monthlength=31
elif month==2:
    if leapyear:
        monthlength=29
    else:
        monthlength=28
else:
    monthlength=30
day=int(input("Enter a day between 1 to 31 : "))
if day<monthlength:
    day+=1
else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1
print("The immediate successor is YYYY-MM-DD : %d-%d-%d." %(year,month,day))