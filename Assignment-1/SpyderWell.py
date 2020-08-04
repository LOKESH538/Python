#Develop a code to calculate no.of steps that spider climbs to come out from well.
H=int(input("Enter height:"))
U=int(input("Enter meters climbs up :"))
D=int(input("Enter meters slips down :"))
step=0
while H>U:
    if H > U:
        H = H - (U - D)
        step += 1
        if H <= U:
            step += 1

print(step)






