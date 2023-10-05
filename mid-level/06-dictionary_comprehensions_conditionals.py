#Create dictionary from countries 
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print (population)

population_v2 = { country: random.randint(1, 100) for country in countries}
print (population_v2)

##Creating a new dictionary with population higher than 50

result = { country:population for (country, population) in population_v2.items() if population > 50}
print(result)


#Extracting vowels from text: 
text = 'Hola soy Mike'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)

################ LISTS vs TUPLES vs SET ######################
#         MUTABLE       ORDENADA    INDEXING/SLICING       DUPLICAR_ELEMENTOS
# LIST     YES           YES              YES                     YES
# TUPLE     NO           YES              YES                     YES
# SET      YES           NO                NO                      NO