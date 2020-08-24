""" 	Area of Triangle :
Given the lengths of three sides of a triangle, calculate the area of the triangle. """

import math
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('The area of the triangle is %0.2f' %area)
