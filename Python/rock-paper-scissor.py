import random

def wantPlayMore(roundNum):
    if(roundNum > 0):
        userPermission = input("Continue? (y/n): ").lower()
        if(userPermission == 'n' or userPermission == 'no'):
            return False
        else:
            return True
    else: 
        return True

def feedback(won, roundNum):
    if(2 * won >= roundNum):
        print("You Won", won, "games out of", roundNum, "games, performance is better than 80 percent users, Well Done!")
    else:
        print("You Won", won,  "games out of", roundNum, "games, better Luck next Time!")
        

rounds = 0
try:
    rounds = int(input("How many games you want to play?"))
except: 
    print("Invalid input, give some number!")

roundNum = 0
won = 0
wantToPlay = True

options = ["rock", "paper", "scissor"]
print("Let's begin!")
while(roundNum < rounds):
    if(wantPlayMore(roundNum) == False):
           break
       
    systemCall = options[random.randint(0, 2)]
    userCall = input("Rock Paper Scissor (r/p/s): ").lower()
    if(userCall == systemCall):
        print("It's a tie!")
    elif(userCall == 'r' or userCall == 'rock'):
        if(systemCall == 'scissor'):
            print("Rock smashes scissor! You win!")
            won += 1
        else:
            print("Paper covers rock! You lose!")
    elif(userCall == 'p' or userCall == 'paper'):
        if(systemCall == 'rock'):
            print("Paper covers rock! You win!")
            won += 1
        else:
            print("Scissor cuts paper! You lose!")
    elif(userCall == 's' or userCall == 'scissor'):
        if(systemCall == 'paper'):
            print("Scissor cuts paper! You win!")
            won += 1
        else:
            print("Rock smashes scissor! You lose!")
    else:
        print("Invalid input, try again!")
        roundNum -= 1
    roundNum += 1

feedback(won, roundNum)