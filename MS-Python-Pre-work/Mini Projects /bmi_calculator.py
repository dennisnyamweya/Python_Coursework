
#########################BMI-Calculator##########################
start="This is the BMI-Calculator Test"
#A code to find BMI
print(start)

height = float(input("Input your height in meters: "))  #Takes input of height in meters
weight = float(input("Input your weight in kilogram: "))  #Takes input of weight in kg
print("Your body mass index is: ", round(weight / (height**2)))  #Finds out the BDD
