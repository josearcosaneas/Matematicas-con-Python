# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:10:13 2016

@author: José Arcos Aneas

Ejercicios de matrices con Python
"""
import matplotlib.pyplot as plt
import numpy as np
import sympy

def dibuja_figura():
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



A = sympy.Matrix( [[ 2,-3,-8, 7],
                   [-2,-1, 2,-7],
                   [ 1, 0,-3, 6]] )
print "Matriz A"
print A
# Transpuesta
print "Transpuesta de A"
print A.transpose()
# transpuesta de transpuesta vuelve a A.
print "Transpuesta de la transpuesta de A"
A.transpose().transpose()
# Creando matriz simetrica
As = A*A.transpose()
# Comprobando simetria.
print "Transpuesta de As"
print As.transpose()
# Matriz invertible
A = sympy.Matrix( [[1,2],
                   [3,9]] )
print "Matriz A"
print A
A_inv = A.inv()
print "Inversa de A"
print A_inv

# A * A_inv = I
A*A_inv
# forma escalonada igual a indentidad.
A.rref()
# la inversa de A_inv es A
A_inv.inv()
# Resolviendo el sistema de ecuaciones.
A = np.array([[1.2, -2.2],
              [1.1, 1.4]])
b = np.array([0., 0.])

x = np.linalg.solve(A, b)
print x


# Solución gráfica.
x_vals = np.linspace(-5, 5, 50) # crea 50 valores entre 0 y 5
ax = dibuja_figura()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid()
ax.plot(x_vals, (1.2 * x_vals) / -2.2) # grafica 1.2x_1 - 2.2x_2 = 0
a = ax.plot(x_vals, (1.1 * x_vals) / 1.4) # grafica 1.1x_1 + 1.4x_2 = 0


# Sympy para resolver el sistema de ecuaciones lineales
a1, a2, a3 = sympy.symbols('a1, a2, a3')
A = sympy.Matrix(( (3, 3, 3, 0), (2, 2, 2, 0), (2, 1, 0, 0), (3, 2, 1, 0) ))

sympy.solve_linear_system(A, a1, a2, a3)
A = sympy.Matrix(( (1, 1, 1, 0), (-2, 1, 1, 0), (-1, 2, 0, 0) ))
sympy.solve_linear_system(A, a1, a2, a3)

# Calculando el rango con SymPy
A = sympy.Matrix([[1, 1, 1, 4],
                  [1, 2, 1, 5],
                  [1, 1, 1, 6]])
# Rango con SymPy
print A.rank()

# Calculando el rango con numpy
A = np.array([[1, 1, 2, 4],
              [1, 1, 2, 5],
              [1, 1, 2, 6]])

print np.linalg.matrix_rank(A)


# Determinante con sympy
A = sympy.Matrix( [[1, 2, 6],
                   [2,-2, 0],
                   [2, 3, 5]] )
print A.det()

# Determinante con numpy
A = np.array([[2, 2, 3],
              [2, 1, 4],
              [2, 1, 5]] )
print np.linalg.det(A)

# valores_propios con numpy
A = np.array([[3, 2],
              [7, -2]])

x, v = np.linalg.eig(A)

# x valor_propio, v vector_propio
print "valor propio y vector propio de A"

print x, v


# valores_propios con SymPy
A = sympy.Matrix([[3, 2],
                  [7, -2]])

# Valores_propios
print A
print "valores propios"
print A.eigenvals()
print "vectores propios"
# vector_propio
print A.eigenvects()
