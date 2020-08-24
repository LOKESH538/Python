"""	Write a program that reads a year from the user and displays a message
Indicating whether or not it is a leap year.
"""
year=int(input("Enter the year : "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Yeah! It is a leap year.")
else:
    print("Sorry, it is not a leap year.")