########################Car-Loans#################################
start="This is the Car-Loan Test"
#A code to find Car-Loan
print(start)

loan = float(input("Input your loan in Ksh: "))  #Takes loan input
salary= float(input("Input your salary in Ksh:")) #Takes salary input
print("You will take months: ", round(loan/salary))  #Calculates the months to pay up
