#######################Magic Ball###############################################
# Import the modules
import sys
import random

ans = True #Checks if answer is true

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(1,20)#Random numbers of 1-20

    if question == "":
        sys.exit()

    if answers == 1:
        print ("It is certain.")

    if answers == 2:
        print ("It is decidedly so.")

    if answers == 3:
        print ("Without a doubt.")

    if answers == 4:
        print ("Yes - definitely.")

    if answers == 5:
        print ("You may rely on it")

    if answers == 6:
        print ("As I see it, yes.")

    if answers == 7:
        print ("Most likely.")

    if answers == 8:
        print ("Outlook good.")

    if answers == 9:
        print (" Yes.")

    if answers == 10:
        print ("Signs point to yes.")

    if answers == 11:
        print ("Reply hazy, try again.")

    if answers == 12:
        print ("Ask again later.")

    if answers == 13:
        print ("Better not tell you now.")

    if answers == 14:
        print ("Cannot predict now.")

    if answers == 15:
        print (" Concentrate and ask again.")

    if answers == 16:
        print ("Don't count on it.")

    if answers == 17:
        print (" My reply is no.")

    if answers == 18:
        print ("My sources say no.")

    if answers == 19:
        print ("Outlook not so good.")

    if answers == 20:
        print ("Very doubtful.")
