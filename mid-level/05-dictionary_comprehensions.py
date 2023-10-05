#Same as lists, this classic way to create dictionaries from iterables:
dict = {}
for i in range(1, 5):
    dict[i] = i*2

print(dict)

#Can be replaced with comprehension sintax
dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)


#Create dictionary from countries 
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print (population)

##Using dictionary coprehensions: 

population_v2 = { country: random.randint(1, 100) for country in countries}
print (population_v2)

##You can Use lists to create dictionary compregensions: 

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

#The command zip will create a list of tuples created by joining 2 lists:
print(list(zip(names, ages))) ## This prints: [('nico', 12), ('zule', 56), ('santi', 98)]

#This is how the dictionary creation will look like: 
new_dict = {name: age for (name, age) in zip(names, ages)}
print (new_dict)

