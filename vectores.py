# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:21:35 2016

@author: José Arcos Aneas

Ejercicios de vectores con python 
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy

# imprimir con notación matemática.
sympy.init_printing(use_latex='mathjax')

# graficando vector en R^2 [2, 4]
def dibujar_figura():
    """Crea la figura de pyplot y los ejes."""
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")

    return ax

def vector_plano(vector, color): 
    """Genera el grafico de los vectores en el plano"""
    v = vector
    ax.annotate(" ", xy=v, xytext=[0, 0], color=color,
                arrowprops=dict(facecolor=color,
                                shrink=0,
                                alpha=0.7,
                                width=0.5))
    ax.text(1.1 * v[0], 1.1 * v[1], v)

ax = dibujar_figura()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid()
vector_plano([2, 4], "blue")

# Suma de dos vectores
# [3, 2] + [1, -2]

ax = dibujar_figura()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid()

vecs = [[3, 2], [1, -2]] 

for v in vecs:
    vector_plano(v, "blue")
v = np.array([2, 4]) + np.array([2, -2])
vector_plano(v, "red")

# Multiplicacion de un vector con un escalar
# [1, 2] * 2
ax = dibujar_figura()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.grid()

v = np.array([1, 2])
vector_plano(v, "blue")

v = v * 2
vector_plano(v, "red")


"""
Resolución de sistemas de ecuaciones con python
"""
# También podemos resolver sistemas de ecuaciones haciendo uso de la 
# libreria Sympy
# Primero hacemos una matriz
A = sympy.Matrix(( (2, 3, 5), (3, 6, 0), (8, 3, 6) ))
# Creamos la matriz B
b = sympy.Matrix(3,1,(52,61,75))
# Resolvemos la ecuacion Ax = b
x = A.LUsolve(b)
# Comprobando la solución
print A*x
