# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:06:01 2016

@author: José Arcos Aneas

Ejercicios con conjuntos
"""


# Creando un conjunto en python
A = {1,2,3,4,5}

# Creando un conjunto a partir de una lista
lista = ["bananas","aguacate","chirimollo" ,"manzanas", "naranjas", "limones"]
B = set(lista)
print B

# Los conjuntos eliminan los elementos duplicados
lista = ["bananas", "manzanas", "naranjas", "limones","aguacate","chirimollo",
        "bananas", "bananas", "limones", "naranjas","aguacate","chirimollo"]
B = set(lista)
print B

# Creando el conjunto vacío
O = set()
print O

# Cardinalidad de un conjunto con len().
print("El cardinal del conjunto A".format(A,len(A)))


# comprobando pertenecia
print 2 in A


# Igualdad entre conjuntos. El orden de los elementos no importa.
A = {1,2,3,4,5}
B = {5,4,2,3,1}
print A == B 

# Subconjunto.
A = {1,2,3}
B = {1,2,3,4,5}
print ("Es A un subconjunto de B")
print A.issubset(B)

# Python no tienen una funcion para el subconjunto propio
# podemos hacerlo de la siguiente manera

print "Es A un subconjunto propio de B"
print A.issubset(B) and A != B


# Union de conjuntos
A = {1,2,3,4,5}
B = {2,3,4,5,6,7,8,9,10}
print A.union(B)

# Intersección de conjuntos
print A.intersection(B)

# Diferencia entre conjuntos
print A - B
print B - A

"""
Conjunto y operaciones con conjuntos usando la libreria SYMPY
"""

# Utilizando FiniteSet de sympy
from sympy import FiniteSet
C = FiniteSet(1, 2, 3)

# Subconjunto y subconjunto propio
A = FiniteSet(1,2,3)
B = FiniteSet(1,2,3,4,5)
A.subset(B)

# Union de dos conjuntos
A = FiniteSet(1, 2, 3)
B = FiniteSet(2, 4, 6)
A.union(B)


# Interseccion de dos conjuntos
A = FiniteSet(1, 2) 
B = FiniteSet(2, 3) 
A.intersect(B)


# Diferencia entre conjuntos
print A - B


# Calculando el producto cartesiano. 
A = FiniteSet(1, 2)
B = FiniteSet(3, 4)
P = A * B
for elem in P:
    print(elem)
    
    
# Calcula el n producto cartesiano del mismo conjunto.
A = FiniteSet(1, 2, 3)
P3 = A ** 2
for elem in P3:
    print(elem)
