myDictionary = {}
print(type(myDictionary))

myDictionary = {
    'name': 'Mike',
    'lastname': 'Munoz',
    'age': '31',
    'mail': 'y@q.com'
}
print(myDictionary)
print(len(myDictionary))

print(myDictionary['age'])
print(myDictionary['lastname'])
#another way to retrieve a dictionary element: 
print(myDictionary.get('name'))
#What's the difference?
#If the key does not exist, with get you get a 'none' result, Using [index] will throw an error 
print(myDictionary.get('phone'))

#Check if a dictionary contains a key:
print('mail' in myDictionary)
print('email' in myDictionary)

