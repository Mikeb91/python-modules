import random

options = ("rock", "paper", "scissors")

def define_turns():
    numberOfTurns = input("How many rounds you want to play?: ")
    return int(numberOfTurns)

def choose_options():
    userOption = input('Rock, Paper, Scissors =>')
    userOption = userOption.lower()
    if not userOption in options:
        print('Thats not an option' )

    computerOption = random.choice(options)

    print('userOption =>', userOption)
    print('ComputerOption =>', computerOption)
    return userOption, computerOption

def rock_case(computerOption, userVictories, computerVictories):
    if computerOption == 'scissors':
        print('Rock wins over Scissors')
        print('You win!')
        userVictories += 1
    else:
        print('Paper wins over Rock')
        print('You loose!')
        computerVictories += 1
    return userVictories, computerVictories

def paper_case(computerOption, userVictories, computerVictories):
    if computerOption == 'rock':
        print('Paper wins over Rock')
        print('You win!')
        userVictories += 1
    else:
        print('Scissors wins over Paper')
        print('You loose!')
        computerVictories += 1
    return userVictories, computerVictories

def scissors_case(computerOption, userVictories, computerVictories):
    if computerOption == 'paper':
        print('Scissors wins over Paper')
        print('You win!')
        userVictories += 1
    else:
        print('Rock wins over Scissors')
        print('You loose!')
        computerVictories += 1
    return userVictories, computerVictories

def execute_game_routine():
    numberOfTurns = define_turns()
    userVictories = 0
    computerVictories = 0
    currentTurn = 1
    while currentTurn <= numberOfTurns:
        print("**********************")
        print("")
        print("ROUND: ", currentTurn)
        userOption, computerOption = choose_options()
        if userOption == computerOption:
            print('Tie!')
        elif userOption == 'rock':
            userVictories, computerVictories = rock_case(computerOption, userVictories, computerVictories)
        elif userOption == 'paper':
            userVictories, computerVictories = paper_case(computerOption, userVictories, computerVictories)
        elif userOption == 'scissors':
            userVictories, computerVictories = scissors_case(computerOption, userVictories, computerVictories)
        currentTurn +=1 #For this modification of currentTurn python asumes currentTurn is local to the function. 
    
    validate_winner(userVictories, computerVictories)

def validate_winner(userVictories, computerVictories):
    if userVictories > computerVictories:
        print("******************************")
        print("*You got the global victory*")
        print("******************************")
    elif computerVictories > userVictories:
        print("*************************")
        print("*you loose the full game*")
        print("*************************")
    else:
        print("****************")
        print("*tie! try again*")
        print("****************")

execute_game_routine()