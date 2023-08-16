import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
fields = ['country', 'points','price', 'variety']
wine_reviews = pd.read_csv('C:\Personal\python\python-modules\Seaborn-Matplot\wine_reviews.csv', usecols = fields)
lista_paises = ['Argentina','Chile','Spain']
wine_reviews_filtradas = wine_reviews[wine_reviews['country'].isin(lista_paises)]
iris_data = pd.read_csv('C:\Personal\python\python-modules\Seaborn-Matplot\iris_dataset.csv')
iris_data.drop(columns = ['fila'], inplace= True)
lista_variedades = ['Malbec','Red Blend','Cabernet Sauvignon']
vinos = wine_reviews_filtradas[wine_reviews_filtradas['variety'].isin(lista_variedades)].dropna()
print(vinos.head())

fig = plt.figure()
ax = plt.axes()

""" Histogramas: Graficar la distribución de una variable aleatoria
Seaborn posee una función para graficar la distribución de una variables aleatoria llamada distplot(). La misma tiene tres parametros principales

hist: Es el parametro que controlo si dibujamos o no el histograma (por default en True).
kde: permite graficar un estimado de la distribución mediante una técnica llamada Kernel Density Estimation, KDE para los amigos (por default en True).
rug: Dibuja sobre el eje horizonal una pequeña linea por cada valor, esto se llama rugplot (por default en False).
Ademas también peude tomar el parámetro bins, con el cual determinamos al cantidad de barras del histograma.

Para el caso del dataset dataset Iris podriamos graficar, por ejemplo, la distribución del largo de los pétalos: """
sns.distplot(iris_data['sepal_length'], hist=True, kde=False, rug=True)
#Con el fin de comparar, se pueden graficar varias distribuciones en una misma figura. Por ejemplo, para el caso del dataset de vinos, podemos graficar el precio según variedad:
#creamos otro fig para poder ver las 2 graficas separadas
fig1 = plt.figure()
ax1 = plt.axes()
ax1=sns.distplot(vinos[(vinos['variety'] == 'Malbec') | (vinos['variety'] == 'Red Blend')].price)


plt.legend(['Malbec','Red Blend','Cabernet Sauvignon'])
plt.xlim(0,100)
""" Otra función interesante de Seaborn es la función jointplot(), la cual grafica un scatterplot junto a dos histogramas, uno para cada una de las variables.

Dejamos un ejemplo de su uso en el iris dataset, y pueden recurrir a su documentación para mas detalles: https://seaborn.pydata.org/generated/seaborn.jointplot.html?highlight=jointplot#seaborn.jointplot """

ax2=sns.jointplot(x="sepal_length", y="petal_length", marginal_kws=dict(bins=15, rug=True), data=iris_data)
""" Pairplots (https://seaborn.pydata.org/generated/seaborn.boxplot.html)
La función pairplot() de Seaborn será utilizada reiteradas veces durante la cursada, ya que resulta muy cómoda para hacer una primera inspección de un dataset.

La misma genera una grilla de N x N ejes, donde N es el número de variables numéricas que tiene el dataset (features que toman valores numéricos). Para cada par de variables numéricas, genera un scatterplot y en la diagonal grafica la distribucion de esos valores. """
sns.pairplot(data=iris_data)

""" Además, podemos diferenciar los datos según alguna de las variables categóricas del dataset mediante el parámetro hue. Esto resulta particularmente útil en el caso que querramos usar las variables numericas con el fin de predecir esta varaible categórica (ya desarrollaremos esta idea en las próximas clases). """
sns.pairplot(data=iris_data, hue="species")
plt.show()