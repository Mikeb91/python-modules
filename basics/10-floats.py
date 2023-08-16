x = 3.3
y = 1.1 + 2.2

print(x)
print(y)

print(x == y) #This is false due to precision in python

#To compare floats:

#first approach:

y_str = format(y, ".2g")
print(y_str)
print(y_str == str(x))


#Second approach:
print(y,x)
tolerance = 0.00001
print(abs(x-y) < tolerance)