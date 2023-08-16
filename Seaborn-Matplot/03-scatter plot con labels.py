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
fig, ax = plt.subplots(1,2)

wine_reviews_Argentina = wine_reviews[wine_reviews['country']=='Argentina']
wine_reviews_Chile = wine_reviews[wine_reviews['country']=='Chile']
wine_reviews_Spain = wine_reviews[wine_reviews['country']=='Spain']


ax[0].scatter(wine_reviews_Argentina.price.values, wine_reviews_Argentina.points.values, label = 'Vinos Argentinos')
ax[0].scatter(wine_reviews_Chile.price.values, wine_reviews_Chile.points.values, label = 'Vinos Chilenos')
ax[0].scatter(wine_reviews_Spain.price.values, wine_reviews_Spain.points.values, label = 'Vinos Españoles',alpha = 0.1)
ax[0].set(xlabel='Precio (usd)', ylabel='Puntaje',
       title='Precio vs. puntaje en vinos', xlim = (0,250))

ax[0].legend(loc='lower right', shadow=True, fontsize=13)
print(wine_reviews_filtradas.info())


#Si queremos graficar este mismo scatter plot usando seaborn, sólo precisamos escribir una linea de código:
ax [1]= sns.scatterplot(x="price", y="points", hue="country", data=wine_reviews_filtradas)
ax[1].set(title='2')

lista_variedades = ['Merlot','Malbec','Syrah']
wine_reviews_filtradas = wine_reviews[wine_reviews['variety'].isin(lista_variedades)]
fig1, ax1 = plt.subplots()

ax1 = sns.scatterplot(x="price", y="points", hue="variety", data=wine_reviews_filtradas)

ax1.set(ylabel="puntos",xlabel="precio en usd")


plt.show()

