print(not True)
print(not False)

print('NOT AND')

print("Not True and True =>", not(True and True))
print("Not True and False =>", not(True and False))
print("Not False and True =>", not(False and True))
print("Not False and False =>", not(False and False))

stock = input('Provide the stock number =>')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))