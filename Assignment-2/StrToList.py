""" Write a Python code that takes a number and returns a list of its digits.
So for 586392 it should return [5,8,6,3,9,2]."""

num=input("Enter a number: ")
l=list(num)
m=list()
for i in l:
    m.append(int(i))
print(m)
