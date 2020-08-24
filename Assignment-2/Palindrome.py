"""	Take a string from end user and check if the value is palindrome or not """
str=input("Enter the str:").lower()
if str==str[::-1]:
    print("Yeah! It Is A Palindrome")
else:
    print("Sorry, It Is Not A Palindrome")