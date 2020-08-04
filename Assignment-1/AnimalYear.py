#Develop a code to display animal year name for respective remainder when divided with 12.
year=int(input("Enter the year:"))
animals={0:"Monkey",1:"Rooster",2:"Dog",3:"Pig",4:"Rat",5:"Ox",6:"Tiger",7:"Rabbit",8:"Dragon",9:"Snake",10:"Horse",11:"Sheep"}
sum=year%12
print(animals[sum])
