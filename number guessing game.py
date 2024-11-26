import random

cnumber = random.randrange(1,101)
userInput = int(input("enter your number :-"))

if userInput > cnumber:
    print("computer number :-",cnumber)
    print("your guess number is too high :-",userInput)
elif userInput < cnumber:
    print("computer number :-", cnumber)
    print("your guess number  is too low :-",userInput)
else:
    print("computer number :-", cnumber)
    print("guess number is equal to the computer number :-",userInput)
