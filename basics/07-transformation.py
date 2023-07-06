name = "Sebastian"
print(type(name))

#variables can change its type by directly changing its value: (dynamicaly)

name = 12
print(type(name))

name = True
print(type(name))

#WARNING: This kind of transformation must be done carefully. 

print("Nicolas" + "Molina")
print(10 + 20)
#print("Nicolas" + 12) # This will throw an error since Python wont know what to do

age = 12
#print("I am " + 12 + "years old") #This is an error since the + int instruction will confuse python. To accomplish this direct transformation must be used: 

print("I am " + str(age) + " years old")

#Another way to accomplish this: 
print(f"I am {age} years old") #format function automatically transforms number into a str



#Transform from str to int
age = input("How old are you? ")
age = int(age)
print(type(age))
print(f"In 10 years, you will be {age + 10} years old")