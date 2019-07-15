import sys

name = sys.argv[1]
age = sys.argv[2]

# print("How old are you?"))#Comment out to run and vice versa
# age = int(input())

print(name)
print(age) #Prints name and age if initiated with both name and age


list_a = list(range(0,5))#Comment out to run and vice versa
print(list_a)#Displays list from 0 to 5
#
#
# ##########################Using range#################################


for i in range(0,7):
    print("I would love " + str(i) + " cookies")

##########################For modulus loop##############################

numbers = [1, 2, 3, 4, 5]
for i in numbers:  #Checks out if it is divisible by 2
    if i % 2 == 0:
        print(i)  #Prints out numbers divisible by 2 i.e 2 and 4
########################### Printing in range############################

'''
in a team of members 20, some numbers are taken
and want to display the numbers that are not taken
so others don't pick the picked numbers
'''

# taken numbers
numTaken = [3,5,7,11,13] #Are numbers taken

print("Available numbers")#Directive to print avaliable numbers

# loop
for i in range(1,21):#range defines it from 1 to 21
    if i in numTaken:#Condition confirmation
        continue
    print(i)#Directive to print the numbers
