name = "Juan"
lastName = "Perez"
age = 23
print(name)
print(lastName)

#Concatenation: 
fullName = name + " " + lastName
print(fullName)

#quote = 'I'm Juan' #this way will display an error, for this cases, you can use ""
quote = "I'm Juan"
print(quote)

#quote2 = "She said: "Hello"" #It works the other way around: 
quote2 = 'She said: "Hello"'
print(quote2)

#Format (3 different approaches)
template = "Hi, my name is " + name + " and my lastname is " + lastName
print(template)

template2 = "Hi, my name is {} and my lastname is {}".format(name, lastName)
print(template2)

template3 = f"Hi, my name is {name} and my lastname is {lastName}, and my age is {age}"
print(template3)