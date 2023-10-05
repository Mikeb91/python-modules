def find_volume(length, width, depth):
    return length * width * depth

result = find_volume(10, 20, 3)

print(result)


#You can define default values toa void errors when parameters are not being sent: 
def find_volume(length=1, width=1, depth=1):
    return length * width * depth

result = find_volume(2, 30, 3)

print(result)


#You can also sent only one of the parameters when invoking the function: 
def find_volume(length=1, width=1, depth=1):
    return length * width * depth

result = find_volume(width=3)

print(result)



#Multiple elemenets can be returned from function: 
def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'

result = find_volume(2, 30, 3)

print(result) #This returns a tuple: (180, 30, 'hola')
print(result[0])

#You can also receive the results defining the variables with commas:
result_v2, width, text = find_volume(width=10)
print(result_v2)
print(width)
print(text)
