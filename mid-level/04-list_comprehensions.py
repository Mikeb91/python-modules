##This is the common way to create a list from iterables: 
numbers = []
for element in range(1, 11):
    numbers.append(element)

print(numbers)

##This can be achieved by list comprehensions: ([element for element in iterable])

numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

##If I want to change the elements I am putting inside the list: 
##This is the common way to create a list from iterables: 
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

##This can be achieved by creating the modification in element:

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

##Conditionals can be added to the list-comprehension:
##   [i*2 for i in range(1, 101) if i % 2 == 0]

##Classic approach:
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)