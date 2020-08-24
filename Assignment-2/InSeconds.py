""" Units of Time
   Create a program that reads duration from the user as a number of days, hours, minutes, and seconds.
 Compute and display the total number of seconds represented by this duration."""

secpermin=60
secperhour=3600
secperday=86400
days=int(input("Enter the number of Days: "))
hours=int(input("Enter the number of Hours: "))
minutes=int(input("Enter the number of Minutes: "))
seconds=int(input("Enter the number of Seconds: "))
totalseconds=days*secperday+(hours*secperhour)+(minutes*secpermin)+seconds
print("Total number of seconds = ","%d"%(totalseconds))