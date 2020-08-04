"""Develop a program that calculates the energy needed to heat water from an initial temperature to a final temperature.
 Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperatures of the water.
 The formula to compute the energy is
Q = M * (finalTemperature – initialTemperature) * 4184.
where M is the weight of water in kilograms, temperatures are in degrees Celsius,  and energy Q is measured in joules."""

M=int(input("Weight of water (in Kg):"))
finalTemp=int(input("finalTemp (in degree Celsius)"))
initialTemp=int(input("initialTemp (in degree Celsius)"))
Q=M*(finalTemp-initialTemp)*4184
print("Energy needed to heat water (in joules)= ",Q)
