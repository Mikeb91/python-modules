

'''
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1])
numbers[-1] = 10 #modifying list items
print(numbers)
numbers[-1] = 9

#Add elements: 
numbers.append(700)
print(numbers)



#Add element to specific possition: 
numbers.insert(0, 'Hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)



#You can concatenate lists:
tasks = ['todo 1', 'todo 2', 'todo 3']
newList = numbers + tasks 
print(newList)



#Identify the position of an element: 
index = newList.index('todo 2')
print(index)
newList[index] = 'todo changed'
print(newList)



#Remove elements from the list: 
newList.remove('todo 1')
print(newList)

#Remove the last element of a lsit:
newList.pop() #This way it removes the last item of the list
print(newList)

newList.pop(0) #If you provide an index as parameter to pop, it will remove the corresponding element from the list
print(newList)



#Reverse lists: 
newList.reverse()
print(newList)


#Order lists: 
numbersA = [1, 4, 6, 3, 2]
numbersA.sort()
print(numbersA)

#Order list of strings: 
textList = ["hij","defg", "abc"]
textList.sort()
print(textList)