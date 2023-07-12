for element in range(20):
    print(element)
print("*******************************")
for element in range(1, 21):
    print(element)
print("*******************************")

myList = [23, 65, 78, 53, 10]

for element in myList:
    print(element)


print("*******************************")
myTuple = ('nico', 'juli', 'Andrew')
for element in myTuple:
    print(element)

print("*******************************")
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

print("*******************************")
#Iterating on a dictionary:
for key in product:
    print(key, "=>", product[key])

#Iterating on a dictionary - Different approach:
for key, value in product.items():
    print(key, "=>", value)

print("*******************************")

people = [
    {
        'name': 'nico',
        'age': 34
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 4
    }
]

for person in people:
    print('name =>', person['name'])
    print('age =>', person['age'])