#TUPLAS: no se puede modificar los elementos de una tupla
tupla = (100, "Hola mundo", [1,2,3,4,5], -5.0)
"""print(tupla)"""

#Indice de las tuplas

"""
print(tupla[0]) #Imprime el primer elemento de la tupla y asi sucesivamente
print(tupla[-1]) #Imprime el ultimo elemento de la tupla y asi para atras
print(tupla[2:]) #Imprime desde el elemento 2 hasta el final
print(tupla[2][-1]) #Imprime el ultimo elemento de la lista que esta en la posicion 2 de la tupla
print(len(tupla)) #Imprime la longitud de la tupla
"""
#METODO INDEX Y COUNT
"""
print(tupla.index(100)) #Imprime el indice del elemento 100 y saber su posicion
print(tupla.count(100)) #Imprime cuantas veces se repite el elemento 100 en la tupla
"""

#CONJUNTOS O SET: no se puede acceder a un elemento por indice, no se puede modificar los elementos de un conjunto, no se puede tener elementos repetidos

conjunto = {1,2,3,4,5}

conjunto.add(0) #Agrega un elemento al conjunto

print(conjunto)