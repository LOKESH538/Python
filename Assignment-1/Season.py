#Develop a program that prompts user to enter month and  print respective season.
month = input("Enter month :")
l = [["Winter", "december", "january", "febuary"], ["Spring", "march", "april", "may"],
     ["Summer", "june", "july", "august"], ["Autumn", "september", "october", "november"]]
for i in range(len(l)):
    if month.lower() in l[i]:
        print(l[i][0])

