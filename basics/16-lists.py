numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
print(numbers)
print(type(numbers))

tasks = ['make dishes', 'play videogames']

types = [1, True, 'hola'] #list can contain multiple data types
print(types)

print(numbers[0])
print(tasks[0])
text = 'Hola'
#text[0] = 'W' # -> this not possible, strings are inmutable. 

tasks[0] = "Watch a course" #List can be changed. 
print(tasks)

#same logic to extract specific character from strings, can be used to extract parameters inside a list can be applied
print(numbers[:2]) #Output: [1, 2]

#Operator in can be used to confirm if a lsit contains an specific element: 
print(1 in types)
print(2 in types)
print(True in types)