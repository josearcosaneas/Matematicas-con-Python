# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:44:57 2016

@author: José Arcos Aneas

Introducción al cálculo con Ptyhon.
"""
import numpy as np  
# importamos matplotlib para la representación gráfica.
import matplotlib.pyplot as plt

def dibuja_grafica():
    """Esta funcion divide el eje para la mejor representación 
    de la función, hace mas visibles los valores """
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    return ax
############################################################################
# definimos una función
def f(x):
    return np.sqrt(x)

x = np.array([0, 2, 4, 6])  # Creando el vector de valores de x
y = f(x) # Almacenamos en y el valor devuelto por la funcion al evaluarl x en ella


############################################################################
# Importamos pandas para la representación de datos.
import pandas as pd


tabla = pd.DataFrame( list(zip(x, y)), columns=['x', 'f(x)'] )
x = np.linspace(-2, 6, num=30)
ax = dibuja_grafica()
ax.grid()
ax.plot(x, f(x))
plt.title(r"Grafico de $f(x)=\sqrt{x}$")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()


############################################################################
# Definimos una nueva función
def f(x):
    return x**2 - x 

x = np.array([1, 1.5, 1.9, 2.5, 3 ])
y = f(x)
tabla = pd.DataFrame(list(zip(x, y)), columns=['x', 'f(x)'])
print tabla
x = np.linspace(-2, 4, num=30)

ax = dibuja_grafica()
ax.grid()
ax.plot(x, f(x))
ax.scatter(2, 2, label="limite cuando x tiende a 2", color='r')
plt.legend()
plt.title(r"Grafico de $f(x)=x^2 -x$")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()
############################################################################

from sympy.interactive import printing
from sympy import Limit, limit, Symbol, S

# imprimir con notación matemática.
printing.init_printing(use_latex='mathjax') 
x = Symbol('x') # Creando el simbolo x.
Limit(x**2 - x + 2, x, 2) # Creando el objeto Limit
# Resolviendo el Limite con el metodo doit()
Limit(x**2 - x + 2, x, 2).doit()

# La funcion limit nos da directamente el resultado
print limit(x**2 - x , x, 2)

# Resolviendo limite 1/x cuando x tiende a infinito
print Limit(1/x, x, S.Infinity).doit()


"""
Derivadas con python
"""
from sympy import Derivative, simplify

fx = (2*x + 1)*(x**3)
print "Función a derivar"
print fx
dx = Derivative(fx, x).doit()
print "Derivada sin simplificar"
print dx
# simplificando los resultados
print "Derivada simplificada"
print simplify(dx)
# Derivada de segundo orden con el 3er argumento.
print "Derivada de 2º orden"
print Derivative(fx, x, 2).doit()
"""
Integrales con python 

"""
from sympy import Integral, integrate

fx = x**3 - 6
print "Funcion a integrar"
print fx
dx = Integral(fx, x).doit()
print "resultado de integrar con la funcion Integral"
print dx
# la función integrate nos da el mismo resultado
print " resultado de integrar con la funcion integrate"
print integrate(fx, x)
print "Calculando la integral definida"
# Calculando integral definida para [0, 3]
print Integral(fx, (x, 0, 3)).doit()
