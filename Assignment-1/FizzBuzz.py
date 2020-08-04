#Write a Java program which iterates the integers from 1 to 100.
# For multiples of three print "Fizz" instead of the number and print "Buzz" for the multiples of five.
# When number is divided by both three and five, print "fizz buzz".
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)