import random

systemNum = random.randint(1, 100)
print("Hi! Hope you're doing well")
print("Get-Set ready to guess the Number which system has generated!")
print("You will have 6 chances to predict, otherwise you will lose")
chanceNum = 0

while(chanceNum < 6):
    guessNum = int(input("guess: "))
    chanceNum += 1
    if(guessNum == systemNum):
        print("Prediction is correct, You Won!")
        break
    elif(guessNum > systemNum):
        print("Too High!")
    elif(guessNum < systemNum):
        print("Too Low!")

if(chanceNum == 6):
    print("You Tried well, better luck next time!")