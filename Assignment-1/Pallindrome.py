""" Print all palindrome numbers between 1 to 1000. """

l=list()
m=list()
count=0
for i in range(1,1001):
    sum=str(i)
    for i in sum:
        l.append(i)
        m.append(i)
    m.reverse()
    for j in range(0,len(l)):
        if l[j]==m[j]:
            count=count+1
        if l[j]!=m[j]:
            count=0
    if count>0:
        print(sum)
    l.clear()
    m.clear()
