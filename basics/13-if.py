if True:
    print('this should be executed')

if False:
    print('This should not be executed')

pet = input('Which is your favorite pet?')

if pet == 'dog':
    print('cool, dogs rock!')

elif pet == 'cat':
    print('Great, cats are nice')

elif pet == 'pez':
    print('you are cool')
else:
    print("c'moon man")

stock = input('Provide the stock =>')
stock = int(stock)
if stock >= 100 and stock <= 1000:
    print("Stock is correct")
else:
    print("the stock is incorrect")