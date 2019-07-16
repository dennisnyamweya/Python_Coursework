###################################Tip Calculator################################
start = 'Tip Calculator'
#A code to Find the tip on billing and total
print(start)
tip = 0.15 #Tip is 15% of total charge
bill = float(input("Enter your total bill charges:"))#Takes the bill charges
print("The total charge is :",round((bill*0.15)+ bill))#Finds total charges plus the tip
