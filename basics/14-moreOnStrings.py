text = "She knows how to code with python"

#Operator in:
#Verifies if a character or string is present in another string:
print('JavaScript' in text) #false
print('python' in text) #true

if 'python' in text:
    print('Cool')
else:
    print('Not cool')

#Method len gets the length of a String
size = len(text)
print(size)

#Capitalize:
print(text, text.upper())

#Lower:
print(text, text.lower())

#Counting occurrences within a string
print(text.count('o'))

#Swap each character case
print(text.swapcase())

#Check if string starts with:
print(text.startswith("She"))

#Check if string ends with:
print(text.endswith("python"))

#Replace a string within another string: 
print(text.replace('python', 'Golang'))


########################################

text2 = "this is a title"

#Capitalize 
print(text2.capitalize())

#Transform into a title:
print(text2.title())

#Check if digit:
print(text2.isdigit())
print("123".isdigit())