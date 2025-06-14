import random

rounds = int(input('How many rounds you want to play?'))
curRoundNum = 0
if(rounds <= 0):
    print('means you do not want to play, ok thats fine, bye!')
else:
    while(rounds > curRoundNum):
        userInput = input('want to play?').lower()
        if(userInput == 'yes') : 
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print("(",die1, ",",die2, ")")
            curRoundNum = curRoundNum + 1
        elif(userInput == 'no') :
            print('Thanks for Playing!')
            break
        else : 
            print('Invalid Input')

