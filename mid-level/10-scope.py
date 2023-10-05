price = 100  #Global scope
print(price)

def increment():
    print(price) #as this is a global variable, it is accesible from here


######################



'''
price = 100  

def increment():
    price = price + 10 #Even though outside the function price is defined, here when you create another variable called 'price' is has a complete different context and thats why this shows an error
    print(price)

print(price)
increment()
'''

price = 200  #Global scope
print(price)

def increment():
    result = price + 10
    print(result) #Python here knows what result is

#print(result) #Python here does not know what result is due to scope
increment()
