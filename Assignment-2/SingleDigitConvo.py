"""	Take a list of integers as an argument, and converts it into a single integer (return the integer).
*Input*: [11, 33, 50]
*Output*: 113350
"""
l=list([11,33,50])
c=list()
a=""
for i in l:
    i=str(i)
    c.append(i)
a=int(a.join(c))
print(a)