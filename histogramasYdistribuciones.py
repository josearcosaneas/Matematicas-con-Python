# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:07:58 2016

@author: José Arcos Aneas

Ejemplos de gráficas y distribuciones con Python

"""

"""
 Distribucion normal
"""
import matplotlib.pyplot as plt # importando matplotlib
# seaborn es una libreria para la visualización de datos estadistivos
import seaborn as sns # importando seaborn http://stanford.edu/~mwaskom/software/seaborn/
import numpy as np # importando numpy
from scipy import stats # importando scipy.stats

# .set_palette
# parametros esteticos de seaborn (tema,proporcion)
sns.set_palette("dark", desat=.6)
# .set_context
# context : dict, None, or one of {paper, notebook, talk, poster}
# font_scale : float, optional
# rc : dict, optional
sns.set_context(rc={"figure.figsize": (8, 4)})
# definimos una media y una desviación estandares
mu, sigma = 0, 0.1
# creamos un conjunto de datos
s = np.random.normal(mu, sigma, 1000) 

# histograma de distribución normal.
cuenta, cajas, ignorar = plt.hist(s, 30, normed=True)
normal = plt.plot(cajas, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp( - (cajas - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

         
"""         
Distribuciones simetrica y asimetricas
"""         
# Dibujando la distribucion Gamma
x = stats.gamma(3).rvs(5000)
gamma = plt.hist(x, 70, histtype="stepfilled", alpha=.7)         
# Calculando la simetria con scipy
stats.skew(x)

"""
cuartiles y diagramas de cajas
"""

datos_1 = np.random.normal(100, 10, 200)
datos_2 = np.random.normal(80, 30, 200)
datos_3 = np.random.normal(90, 20, 200)
datos_4 = np.random.normal(70, 25, 200)
 
datos_graf = [datos_1, datos_2, datos_3, datos_4]

# Creando el objeto figura
fig = plt.figure(1, figsize=(9, 6))

# Creando el subgrafico
ax = fig.add_subplot(111)

# creando el grafico de cajas
bp = ax.boxplot(datos_graf)

