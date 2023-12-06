#TUPLAS: no se puede modificar los elementos de una tupla
tupla = (100, 'Hola mundo', [1,2,3,4,5], -5.0)
'''print(tupla)'''

#Indice de las tuplas

'''
print(tupla[0]) #Imprime el primer elemento de la tupla y asi sucesivamente
print(tupla[-1]) #Imprime el ultimo elemento de la tupla y asi para atras
print(tupla[2:]) #Imprime desde el elemento 2 hasta el final
print(tupla[2][-1]) #Imprime el ultimo elemento de la lista que esta en la posicion 2 de la tupla
print(len(tupla)) #Imprime la longitud de la tupla
'''
#METODO INDEX Y COUNT
'''
print(tupla.index(100)) #Imprime el indice del elemento 100 y saber su posicion
print(tupla.count(100)) #Imprime cuantas veces se repite el elemento 100 en la tupla
'''

#CONJUNTOS O SET: no se puede acceder a un elemento por indice, no se puede modificar los elementos de un conjunto, no se puede tener elementos repetidos

'''conjunto = {1,2,3,4,5}

conjunto.add(0) #Agrega un elemento al conjunto

print(conjunto)''' #Imprime el conjunto 

'''grupo = {'Daniel', 'Juan', 'Maria', 'Pedro'}

print('Daniel' in grupo) #Imprime True si el elemento esta en el conjunto y False si no esta

print('Daniel' not in grupo) #Imprime False si el elemento esta en el conjunto y True si no esta'''

'''test = {'Daniel', 'Juan', 'Daniel', 'Pedro'}

# Los conjuntos no pueden tener el mismo elemento mas de una vez, por lo que se va a borrar automaticamente los que esten duplicados
print(test) #Imprime el conjunto sin el elemento repetido'''

'''lista = [1,2,3,1,2,3]
print(lista)

lista = list(set(lista)) #Convierte la lista en un conjunto y luego lo convierte en una lista

print(lista)'''

#DICTONARIOS: es un tipo de dato que almacena un conjunto de datos, en formato clave-valor. Es parecido a un array asociativo o un objeto json

'''colores = {'amarillo':'yellow', 'azul':'blue'}

print(colores['amarillo']) #Imprime el valor de la clave amarillo

colores['verde'] = 'green' #Agrega un nuevo elemento al diccionario

print(colores)

del(colores['amarillo']) #Elimina el elemento del diccionario

print(colores)

numeros = {10:'diez', 20:'veinte'} #Se puede usar numeros como clave

print(numeros[20])

edades = {'Juan': 20, 'Agustin': 19, 'Rocio': 18}
edades['Rocio'] += 1 #Aumenta en 1 el valor de la clave Rocio

print(edades)

print(edades['Juan'] + edades['Agustin']) #Suma los valores de las claves Juan y Agustin'''

'''edades = {'Juan': 20, 'Agustin': 19, 'Rocio': 18}

for edad in edades: #Recorre el diccionario
    print(edad) #Imprime las claves del diccionario
    print(edades[edad]) #Imprime los valores de las claves del diccionario'''
    
#Agregamos con .apeed variables DICCIONARIO a la lista vacia.
'''personajes = []

gandalf = {'Nombre':'Gandalf', 'Clase':'Mago', 'Raza':'Humano'}
legolas = {'Nombre':'Legolas', 'Clase':'Arquero', 'Raza':'Elfo'}
gimli = {'Nombre':'Gimli', 'Clase':'Guerrero', 'Raza':'Enano'}

personajes.append(gandalf)
personajes.append(legolas)
personajes.append(gimli)

print(personajes)'''

#LIFO (Last In First Out) / El ultimo elemento en entrar es el primero en salir

'''pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)'''

pila = [1,2,3]
print(pila.pop()) #Elimina el ultimo elemento de la pila

numero = pila.pop()
print(numero)

#COLAS: FIFO (First In First Out) / El primer elemento en entrar es el primero en salir

cola = ['Hector', 'Juan', 'Maria']
