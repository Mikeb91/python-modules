import random

options = ("rock", "paper", "sissors")
userOption = input('Rock, Paper, Scissors =>')
userOption = userOption.lower()

if not userOption in options:
    print('Thats not an option' )

computerOption = random.choice(options)

print('userOption =>', userOption)
print('ComputerOption =>', computerOption)

if userOption == computerOption:
    print('Empate!')
elif userOption == 'rock':
    if computerOption == 'scissors':
        print('Rock wins over Scissors')
        print('You win!')
    else:
        print('Paper wins over Rock')
        print('You loose!')
elif userOption == 'paper':
    if computerOption == 'rock':
        print('Paper wins over Rock')
        print('You win!')
    else:
        print('Scissors wins over Paper')
        print('You loose!')
elif userOption == 'scissors':
    if computerOption == 'paper':
        print('Scissors wins over Paper')
        print('You win!')
    else:
        print('Rock wins over Scissors')
        print('You loose!')
