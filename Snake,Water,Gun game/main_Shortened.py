# This below logic is written in on the basis of computer-you


import random

computer = random.choice([-1,0,1])

youstr = input("Enter your choice :")
yourDict ={"s" : 1,"w" : -1,"g" : 0}
reverseDict = {1:"Snake", -1: "Water", 0 : "Gun"}

you = yourDict[youstr]

print(f"you choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw!")

else:                 #Basically this is the shorten part written with logic.
    if((computer - you) == -1 or (computer - you) == 2):
        print("You lose!")

    else:
        print("You win!")