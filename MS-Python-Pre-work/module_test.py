greeting = "Hello"
school = "Moringa"

print(greeting + ", " + school + "!")   #Prints out greeting

greeting="Hello Dennis"
data="These are your Python assignments"

print(greeting + ", " + data +"!")  #Prints out greeting

#########################BMI-Calculator##########################
start="This is the BMI-Calculator Test"
#A code to find BMI
print(start)

height = float(input("Input your height in meters: "))  #Takes input of height in meters
weight = float(input("Input your weight in kilogram: "))  #Takes input of weight in kg
print("Your body mass index is: ", round(weight / (height * height), 2))  #Finds out the BDD

########################Car-Loans#################################
start="This is the Car-Loan Test"
#A code to find Car-Loan
print(start)

loan = float(input("Input your loan in Ksh: "))  #Takes loan input
salary= float(input("Input your salary in Ksh:")) #Takes salary input
print("You will take months: ", round(loan/salary))  #Calculates the months to pay up


#######################Circumference Calculation######################
start="Circumference Calculator"
#A code to find Circumference
print(start)

π=3.14
radius=float(input("Enter the radius in cm:")) #Tales the input radius
print("The Circumference is:",round(2*π*radius)) #Displays the circumference


#################################Birthday dates##############################
start = 'Birthday dates'
#A code to find Birthday date and year to reach 80years
print(start)
year=2019
age = int(input("Enter your age :"))#Takes  the age input
print("You were born in :",round(year-age))#Displays the year of birth
print("You will be 80years by :",round((80-age)+year ))#Displays the year you will turn


###################################Tip Calculator################################
start = 'Tip Calculator'
#A code to Find the tip on billing and total
print(start)
tip = 0.15 #Tip is 15% of total charge
bill = float(input("Enter your total bill charges:"))#Takes the bill charges
print("The total charge is :",round((bill*0.15)+ bill))#Finds total charges plus the tip
