import random
compGuess=["stone","paper","scissors"]
print("WELCOME TO STONE,PAPER,SCISSORS GAME \nYOU WILL BE PROVIDED WITH 10 CHANCES TO COMPETE WITH  COMPUTER.\n"
      "AND FINALLY YOUR SCORE WILL BE GENERATED")
chance=10
userScore=0
compScore=0
while chance>0:
    randomno=random.randint(0,2)
    userGuess = input("Enter stone/paper/scissors: ").lower()
    if (compGuess[randomno] == "scissors" and userGuess == "stone") or (compGuess[randomno] == "stone" and userGuess == "paper") or (compGuess[randomno] == "paper" and userGuess == "scissors"):
        userScore+=1
        print(f"computer chose {compGuess[randomno]} and you chose {userGuess}")
        print("YOU WON!!!")
    elif compGuess[randomno] == userGuess:
        print("Aaah its a Draw")
    else:
        print(f"computer chose {compGuess[randomno]} and you chose {userGuess}")
        print("YOU LOST!!!")
        compScore+=1
    chance-=1
if userScore>compScore:
    print(f"Your Score is {userScore} and Computer Score is {compScore}\nYOU WON!!!CONGRATULATIONS")
    print("Game over!!!")
elif userScore == compScore:
    print("Its a Draw,better luck next time")
    print("Game over!!!")
else:
    print(f"Your Score is {userScore} and Computer Score is {compScore}\nYOU LOST!!!")
    print("Game over!!!")
