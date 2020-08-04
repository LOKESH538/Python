"""A theater in Delhi wants to develop a computerized Booking System. The theater offers different types of seats.
 The Ticket rates are- Stalls- Rs. 625/-, Circle- Rs.750/-, Upper Class- Rs.850/- and Box- Rs.1000/-.
 A discount is given 10% of total amount if tickets are purchased on Cash.
 In case of credit card holders 5% discount is given."""
seat=input("Type of seat (stalls/circle/upperclass/box):")
pm=(input("Payment Mode (cash/credit card):"))
x=[['stalls',625],['circle',750],['upperclass',850],['box',1000]]
y=[['cash',10],['credit card',20]]
for i in range(len(x)):
    if seat.lower()==x[i][0]:
        prize=x[i][1]
for j in range(len(y)):
    if pm.lower()==y[j][0]:
        discount=prize/y[j][1]
Bill=prize-discount
print("Cost of ticket :",Bill)
