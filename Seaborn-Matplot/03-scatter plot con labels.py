import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
fields = ['country', 'points','price', 'variety']
wine_reviews = pd.read_csv('C:\Personal\python\python-modules\Seaborn-Matplot\wine_reviews.csv', usecols = fields)
print(wine_reviews.head())

print("################### filtro de vinos argentinos chilenos y de españa##############")
lista_paises = ['Argentina','Chile','Spain']
wine_reviews_filtradas = wine_reviews[wine_reviews['country'].isin(lista_paises)]
print(wine_reviews_filtradas.head())

#precio vs puntaje en el cual diferencie por color el pais de origen de cada vino (Argentina, España o Chile).
fig = plt.figure()
ax = plt.axes()

wine_reviews_Argentina = wine_reviews[wine_reviews['country']=='Argentina']
wine_reviews_Chile = wine_reviews[wine_reviews['country']=='Chile']
wine_reviews_Spain = wine_reviews[wine_reviews['country']=='Spain']


ax.scatter(wine_reviews_Argentina.price.values, wine_reviews_Argentina.points.values, label = 'Vinos Argentinos')
ax.scatter(wine_reviews_Chile.price.values, wine_reviews_Chile.points.values, label = 'Vinos Chilenos')
ax.scatter(wine_reviews_Spain.price.values, wine_reviews_Spain.points.values, label = 'Vinos Españoles',alpha = 0.1)
ax.set(xlabel='Precio (usd)', ylabel='Puntaje',
       title='Precio vs. puntaje en vinos', xlim = (0,250))

ax.legend(loc='lower right', shadow=True, fontsize=13)
plt.show()