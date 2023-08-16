import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#Vamos a trabajar con el Dataset Iris. En el mismo tenemos 4 features distintos (medidas de ancho y largo de pétalos y sépalos) y tres labels distintos (variedad a la que pertenece la flor).
iris_data = pd.read_csv('C:\Personal\python\python-modules\Seaborn-Matplot\iris_dataset.csv')
iris_data.drop(columns = ['fila'], inplace= True)
print(iris_data.head())
""" Categorical plot básico
Como su nombre lo indica, los categorical plots son gráficos donde una de las variables a graficar es de tipo categórica. Este tipo de gráficos son muy usados en Data Science y Seaborn tiene una función especial dedicada a ellos, catplot.

Primero veamos un ejemplo de cómo hacer para realizar un grafico de este tipo en Matplotlib. El objetivo es graficar el ancho del petalo según la especie . """
especie = iris_data['species']
ancho_petalo = iris_data['sepal_length']

fig = plt.figure()
ax = plt.axes()
ax.scatter(especie,ancho_petalo)

""" Como podemos observar el resultado no es muy satisfactorio. Al estar todos los puntos sobre una misma linea, no se pueden distinguir entre sí.

Veamos ahora como realizar el mismo gráfico son seaborn: """
sns.catplot(data = iris_data, x = "species", y = "sepal_length",ci = "sd",estimator=np.median)
""" Como se puede observar, Seaborn le da automáticamente distintos colores a las categorías y además los separa para poder identificar la cantidad de puntos en cada grupo con facilidad.

Ejercicos:

Realizar con Seaborn un gráfico del ancho del petalo según la especie
Realizar el mismo gráfico, pero ahora como gráfico de barras. Pista: ver el parametro kind
¿Que representan las barritas negras?
Averiguar la utilidad de los parámetros ci y estimator. """

sns.catplot(data = iris_data, x = "species", y = "sepal_length",ci = "sd",estimator=np.median)
sns.catplot(data = iris_data, x = "species", y = "sepal_length",ci = "sd", kind='bar',estimator=np.median)
#Boxplot
""" Volvamos al dataset de vinos. Vamos a armar un nuevo dataset solo con los vinos de Argentina, Chile y España, pero esta vez sólo con las siguietnes variedades: 'Malbec', 'Red Blend' y 'Cabernet Sauvignon'. """
fields = ['country', 'points','price', 'variety']
wine_reviews = pd.read_csv('C:\Personal\python\python-modules\Seaborn-Matplot\wine_reviews.csv', usecols = fields)
lista_paises = ['Argentina','Chile','Spain']
wine_reviews_filtradas = wine_reviews[wine_reviews['country'].isin(lista_paises)]

lista_variedades = ['Malbec','Red Blend','Cabernet Sauvignon']
vinos = wine_reviews_filtradas[wine_reviews_filtradas['variety'].isin(lista_variedades)].dropna()
print(vinos.head())
""" Queremos realizar un único gráfico que muestre el precio de los vinos en gráfico de cajas (boxplots) para los 3 distintos paises y las 3 variedades de vinos. Debemos entonces usar el parámetro kind='box' para determinar que queremos un gráfico de cajas y el parámetro col='country' para indicar que queremos tantos ejes en el gráfico como valores distintos hay en el campo country. """
sns.catplot(x="variety", y="price", col="country", kind='box' , data=vinos)
#sns.boxplot(x="country", y="price", data=vinos)
sns.catplot(x="variety", y="price", col="country", kind='box', data=vinos[vinos['price'] < 90])

vinos_menores_a_noventa = vinos[vinos['price'] < 90]

sns.catplot(x="variety", y="price", kind='box', linewidth=2 , data=vinos )

p = sns.catplot(x="country", y="points", col="variety", kind='box' , data=vinos,height=8)

p.set_xticklabels(rotation = 90)

""" Ejercicios:

En el último gráfico, era difícil visualizar bien los resultados debido a precios que eran mucho más grandes que los demás. ¿Cómo podría solucionar facilmente este problema?
Averigüe cómo cambiar el gráfico si desea que los 3 ejes aparezcan apilados verticalmente en lugar de uno al lado del otro.
Averigüe cómo hacer un violin plot y conjeture en qué circunstancias podría ser de utilidad. """
p = sns.catplot(x="country", y="points", col="variety", kind='box' , data=vinos,height=8
                , col_wrap=80
                )

""" Histogramas: Graficar la distribución de una variable aleatoria
Seaborn posee una función para graficar la distribución de una variables aleatoria llamada distplot(). La misma tiene tres parametros principales

hist: Es el parametro que controlo si dibujamos o no el histograma (por default en True).
kde: permite graficar un estimado de la distribución mediante una técnica llamada Kernel Density Estimation, KDE para los amigos (por default en True).
rug: Dibuja sobre el eje horizonal una pequeña linea por cada valor, esto se llama rugplot (por default en False).
Ademas también peude tomar el parámetro bins, con el cual determinamos al cantidad de barras del histograma.

Para el caso del dataset dataset Iris podriamos graficar, por ejemplo, la distribución del largo de los pétalos: """
sns.distplot(iris_data['sepal_length'], hist=True, kde=False, rug=True)
#Con el fin de comparar, se pueden graficar varias distribuciones en una misma figura. Por ejemplo, para el caso del dataset de vinos, podemos graficar el precio según variedad:
sns.distplot(vinos[(vinos['variety'] == 'Malbec') | (vinos['variety'] == 'Red Blend')].price)



plt.legend(['Malbec','Red Blend','Cabernet Sauvignon'])
plt.xlim(0,100)

plt.show()