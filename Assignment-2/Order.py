"""	Unique Sort problem
Take a string as input that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
*Input*: orange,white,red,cyan,green,magenta,cyan,pink,white
*Output*: cyan,green,magenta,orange,pink,red,white
"""
str1=input("Enter a string: ").split(',')
str2=list()
for i in str1:
    if i not in str2:
        str2.append(i)
c=0
str2.sort()
for i in str2:
    c+=1
    if c!=len(str2):
        print('{},'.format(i),end='')
    else:
        print('{}'.format(i))