"""A Quick Fox Transport Co. wants to develop an application for calculating amount based on distance and weight of goods.
 The charges (Amount) to be calculated as per rates given below."""

d=int(input("Enter distance to be travelled (in Km) :"))
w=int(input("Enter weight of the goods (in Kg) : "))
if d >= 500:
    if w >= 100:
        c=5
    if w>=10 & w<100:
        c=6
    if w<10:
        c=7
if d<500:
    if w>=100:
        c=8
    if w<100:
        c=5
charge=d*c
print("Amount to be charged (in Rs) =",charge)
