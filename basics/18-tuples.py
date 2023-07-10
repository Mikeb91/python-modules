numbers = (1, 2, 3, 5)
strings = ('nico', 'mike', 'santi', 'nico')

print(numbers)
print('0 => ', numbers[0])
print('0 => ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#In tuples items cannot be inseted, or elements cannot be changed.  Tuples are inmutables. 

#Methods available for tuples: 

#find possition of an element within  the tuple: 
print(strings)
print(strings.index('mike'))

#Count repetitions: 
print(strings)
print(strings.count('nico'))

#Even though tuples cannot change, it can be transformed to a list: 
myList = list(strings)
print(myList)
print(type(myList))

myList[0] = 'juli'
print(myList)

#It can be converted back to a tuple: 
myTuple = tuple(myList)
print(myTuple)