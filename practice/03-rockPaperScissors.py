userOption = input('Rock, Paper, Scissors =>')
computerOption = 'Paper'

if userOption == computerOption:
    print('Empate!')
elif userOption == 'Rock':
    if computerOption == 'Scissors':
        print('Rock wins over scissors')
        print('You win!')
    else:
        print('Paper wins over Rock')
        print('You loose!')
elif userOption == 'Paper':
    if computerOption == 'Rock':
        print('Paper wins over Rock')
        print('You win!')
    else:
        print('Scissors wins over Paper')
        print('You loose!')
elif userOption == 'Scissors':
    if computerOption == 'Paper':
        print('Scissors wins over Paper')
        print('You win!')
    else:
        print('Rock wins over Scissors')
        print('You loose!')