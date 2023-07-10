text = "She knows python"
print(text[0])
print(text[1])
#print(text[10000])#Throws an error since that character does not exist

size = len(text)
print('size -> ', size)
print(text[size-1])


#This is gow python solves how last possition is retrieved: 
print(text[-1])


#Slicing
print(text[0:3]) #extracts word she

print(text[10:17]) #extracts word python

print(text[:10]) #If nothing is sent to specify where to start, python starts from the beginnig.

print(text[5:]) # Start point can be specified. If no end point is declared, it will go to the last character. 

print(text[10:16:1]) #you can specify jumps. In this case we got 1 which is the default jump
print(text[10:16:2]) #Output: pto