def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def countsteps(a,b,c):
    v1=b
    v2=0
    count=1
    while ((v1 is not c) and (v2 is not c)):
        temp=min(v1,a-v2)
        v2=v2+temp
        v1=v1-temp
        count=count+1
        if ((v2==c)or(v1==c)):
            break
        if v1==0:
            v1=b
            count=count+1
        if v2==a:
            v2=0
            count=count+1
    return count
def ispossible(a,b,c):
    if a>b:
        temp=a
        a=b
        b=temp
    if c>b:
        return -1
    if (c%(gcd(b,a)) is not 0):
        return -1
    return(min(countsteps(b,a,c),countsteps(a,b,c)))
t=int(input("Enter no of testcases : "))
for i in range(t):
  a=int(input("Enter capacity of vessel a : "))
  b=int(input("Enter capacity of vessel b : "))
  c=int(input("Enter capacity to be obtained :"))
  print("Minimum number of steps required is : ",ispossible(a,b,c))
