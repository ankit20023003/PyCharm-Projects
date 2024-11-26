import random
l = ["Rock","Paper","Scissor"]
"""
Rock vs Paper = Paper wins
Rock vs Scissor = Rock wins
Paper vs Scissor = Scissor wins
"""

while True:
    ccount = 0
    ucount = 0
    user = int(input("""
    Game Start......
    1 Yes
    2 No | Exit
    """))
    if user ==1:
        for i in range(1,6):
            userInput = int(input("""
            1.Rock
            2.Scissor
            3.Paper
            """))
            if userInput == 1:
                uchoice = "Rock"
            elif userInput == 2:
                uchoice = "Paper"
            elif userInput == 3:
                uchoice = "Scissor"
            else:
                uchoice="invalid"

            Cchoice = random.choice(l)

            if Cchoice == uchoice:
               print("computer value",Cchoice)
               print("user value",uchoice)
               print("game draw")
               ucount = ucount+1
               ccount = ccount+1
            elif (uchoice == "Rock" and Cchoice == "Scissor") or(uchoice == "Paper" and Cchoice == "Rock") or (uchoice == "Scissor" and Cchoice == "Paper"):
               print("computer value", Cchoice)
               print("user value", uchoice)
               print("you win")
               ucount = ucount+1
            else:
               print("computer value", Cchoice)
               print("user value", uchoice)
               print("computer win")
               ccount = ccount + 1

        if ucount == ccount:
            print("series draw")
            print("user score",ucount)
            print("coumputer score",ccount)
        elif ucount > ccount:
            print("series winner is user")
            print("user score",ucount)
            print("coumputer score",ccount)
        else:
            print("series winner is computer")
            print("user score", ucount)
            print("coumputer score", ccount)

    else:
        break