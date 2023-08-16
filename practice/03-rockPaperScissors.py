import random

options = ("rock", "paper", "scissors")

numberOfTurns = input("How many rounds you want to play?: ")
numberOfTurns = int(numberOfTurns)
currentTurn = 1

userVictories = 0
computerVictories = 0

while currentTurn <= numberOfTurns:
    print("**********************")
    print("")
    print("ROUND: ", currentTurn)
    userOption = input('Rock, Paper, Scissors =>')
    userOption = userOption.lower()
    if not userOption in options:
        print('Thats not an option' )

    computerOption = random.choice(options)

    print('userOption =>', userOption)
    print('ComputerOption =>', computerOption)

    if userOption == computerOption:
        print('Tie!')
    elif userOption == 'rock':
        if computerOption == 'scissors':
            print('Rock wins over Scissors')
            print('You win!')
            userVictories += 1
        else:
            print('Paper wins over Rock')
            print('You loose!')
            computerVictories += 1
    elif userOption == 'paper':
        if computerOption == 'rock':
            print('Paper wins over Rock')
            print('You win!')
            userVictories += 1
        else:
            print('Scissors wins over Paper')
            print('You loose!')
            computerVictories += 1
    elif userOption == 'scissors':
        if computerOption == 'paper':
            print('Scissors wins over Paper')
            print('You win!')
            userVictories += 1
        else:
            print('Rock wins over Scissors')
            print('You loose!')
            computerVictories += 1
    currentTurn +=1

if userVictories > computerVictories:
    print("******************************")
    print("*You got the complete victory*")
    print("******************************")
elif computerVictories > userVictories:
    print("*************************")
    print("*you loose the full game*")
    print("*************************")
else:
    print("****************")
    print("*tie! try again*")
    print("****************")
