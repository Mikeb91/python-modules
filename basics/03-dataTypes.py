# String
companyName = "Samsung"
userName = 'Smith'
print("company name: ", companyName)
print(type(companyName)) #Type will display the type of the variable, in this case str

#int
userAge = 28
print('user age', userAge)
print(type(userAge)) #Type will display the type of the variable, in this case int

#boolean
isSingle = True #First letter must be upper case. 
print("is single: ", isSingle) #Type will display the type of the variable, in this case bool
print(type(isSingle))

##################
#Inputs always produce a string: 

myAge = input('How old are you? ')
print('age: ', myAge)
print(type(myAge)) #As value was catch using input, the result will allways be a str
