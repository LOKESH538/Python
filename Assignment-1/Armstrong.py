#Print all Armstrong numbers between 1 to 1000.
count=0
for i in range(1,1001):
    sum=str(i)
    for i in sum:
        count=count+(int(i)**3)
    if int(sum)==count:
        print(count)
    count=0