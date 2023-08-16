import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Definimos las columnas que nos interesan
fields = ['country', 'points','price', 'variety']

# Cargamos el DataFrame solo con esas columnas
wine_reviews = pd.read_csv('C:\Personal\python\python-modules\Seaborn-Matplot\wine_reviews.csv', usecols = fields)
print(wine_reviews.head())
# Tomamos como coordenadas en x los precios
x = wine_reviews.price.values
# Tomamos como coordenadas en y el puntaje de la review
y = wine_reviews.points.values
#usando matplot
fig = plt.figure()
ax = plt.axes()
figseab = plt.figure()
axseab = plt.axes()

ax.scatter(x, y)
ax.set(xlabel='price', ylabel='points')

#usando seaborn
axseab = sns.scatterplot(x="price", y="points", data=wine_reviews)
plt.show()