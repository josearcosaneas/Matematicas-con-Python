# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:58:28 2016

@author: José Arcos Aneas

Ejemplos de estadística descriptiva con python

"""

 

import numpy as np 
from scipy import stats 
import pandas as pd 

np.random.seed(2182) # Semilla para el random

datos = np.random.randn(5, 4) # Generamos datos distribuidos

# media arítmetica

print datos.mean() 
print np.mean(datos) # Mismo resultado desde la funcion de numpy

# mediana
print np.median(datos) 

 # Desviación típica
print np.std(datos)

# varianza
print np.var(datos)
print np.var(datos, 0) # varianza de cada columna

# moda
print stats.mode(datos) # Calcula la moda de cada columna

# correlacion
print np.corrcoef(datos) # Crea matriz de correlación.

# calculando la correlación entre dos vectores.
print np.corrcoef(datos[0], datos[1])
# covarianza
print np.cov(datos) # calcula matriz de covarianza
# covarianza de dos vectores
print np.cov(datos[0], datos[1])

print 25*"*"
# Usando la libreria Pandas
print "Usamos Pandas"
dataframe = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'], 
                        columns=['col1', 'col2', 'col3', 'col4'])

                        
print "Resumen estadistico "                        
print dataframe.describe()
# sumando las columnas
print "Suma de columnas"
print dataframe.sum()
print "sumando filas"
print dataframe.sum(axis=1)
print "Acumulando valores"
print dataframe.cumsum() 
print " media aritmetica de cada columna"
print dataframe.mean()
print " media aritmetica de cada fila"
print dataframe.mean(axis=1)













































