person = {
    'name': 'Sergi',
    'lastName': 'molina',
    'langs': ['python', 'javaScript'],
    'age':50
}

print(person)

#Updating values: 
person['name'] = 'pedri'
person['age'] -= 50
person['langs'].append('rust')
person['email'] = "y@s.com"
print(person)

#deleting values:
del person['lastName']
person.pop('age')
print(person)




print('items') #Generate tuple with a list containing 
print(person.items())

print('keys') #Generate tuple with a list containing the keys of the dictionary
print(person.keys())

print('values') #Generate tuple with a list containing the values of the dictionary
print(person.values())