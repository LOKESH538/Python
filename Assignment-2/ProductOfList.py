"""11. Compute product of a list of numbers [45,3,2,89,72,1,10,7]
  Output: 121111200"""

l=list([45,3,2,89,72,1,10,7])
n=1
for i in range(len(l)):
    n=n*l[i]
print(n)