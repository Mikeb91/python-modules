
'''

SETS:
Sets have the following features: 

- Can be modified
- Don't have specific order
- Cannot have duplicated elements.

'''
set_countries = {'col', 'mex', 'bol'}

#Even though starts similar to a dictionary, 
#it is of type set, because we dont have the 
#key-value structure inside the brakets.

print(set_countries)
print(type(set_countries))

set_countries = {'col', 'mex', 'bol', 'col'} #If we try to add duplicates:
print(set_countries) #this prints: {'col', 'bol', 'mex'} - Do not accept duplicates

#Can be of different types
set_numbers = {1, 2, 2,  443, 23}
print(set_numbers) 

set_types = {1, "hola", False, 12.34}
print(set_types)


#Sets can be created from other types:
set_from_string = set('hola')
print(set_from_string) #creates a set with each character of the string

set_from_tuple = set(('abc', 'cbv', 'abc', 'as'))
print(set_from_tuple)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
uniqueNumbers = list(set_numbers)
print(uniqueNumbers)