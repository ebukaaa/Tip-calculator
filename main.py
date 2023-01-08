#Welcome the user to the Tip Calculator
print ("Welcome to the Tip Calculator")
#Ask the user what the total bill is
bill = float (input ("What was the total bill? $"))
#print (type(bill))
#Ask the user what % of tip would they like to give. 10, 12 or 15?
tip = int (input ("What percentage of tip would you like to give? 10, 12 or 15? "))
#print (type (tip))
#Ask the user how many people are splitting the bill
split_btwn = int(input ("How many people are going to split the bill? "))
#print (type(split_btwn))
#Tell the user how much each person should pay
customers_pay = ((tip / 100) * bill) + bill
each_pay = customers_pay / split_btwn
# rounding the number upto 2 decimal places
new_decimal = format(each_pay,".2f")
#print (new_decimal)
print (f"Each person should pay: ${new_decimal}")