set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#Adding elements to the set
set_countries.add('pe')
print('pe' in set_countries)

#Updating elements in set - Can add a full set to the set
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

#Removing elements from set
set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')
print(set_countries)

#If we try to remove an element that does not exist, it will throw an error: 
#set_countries.remove('ur')

#For removing only if the element exists, we got discard()
set_countries.discard('arg')
print(set_countries)

set_countries.discard('mex')
print(set_countries)

#Removing all content from set:
set_countries.clear()
print(set_countries)