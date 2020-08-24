"""9. Sort 3 integers
  Given three integers (given through user input), sort the numbers using |min| and |max| functions."""

x=int(input("Enter the number of x:"))
y=int(input("Enter the number of y:"))
z=int(input("Enter the number of z:"))
min=min(x,y,z)
max=max(x,y,z)
rem=(x+y+z)-min-max
print("The Sorted order is:",min,rem,max)