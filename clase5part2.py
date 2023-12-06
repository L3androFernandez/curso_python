#METODOS DE LAS CADENAS:

#Metodo upper()

print("hola mundo".upper())

#Metodo lower()

print("HOLA MUNDO".lower())

#Metodo capitalize() (devuelve la cadena con la primera letra en mayuscula)

print("hola mundo".capitalize())

#Metodo title() (devuelve la cadena con la primera letra de cada palabra en mayuscula)

print("hola mundo".title())

#Metodo count() (devuelve el numero de veces que aparece la cadena)

print("hola mundo".count("mundo"))

#Metodo find() (devuelve la posicion de la primera ocurrencia de la cadena)

print("hola mundo".find("hola"))

#Metodo isdigit() (devuelve true si la cadena es un numero)

x = '100'
print(x.isdigit())

#Metodo isalnumeric() (devuelve true si la cadena es alfanumerica)

c = '123Hola'
print(c.isalnum())

#Metodo isalpha() (devuelve true si la cadena es alfabetica)

c = 'Hola'
print(c.isalpha())

#Metodo islower() (devuelve true si la cadena esta en minusculas)

print("hola mundo".islower())

#Metodo isupper() (devuelve true si la cadena esta en mayusculas)

print("HOLA MUNDO".isupper())

#Metodo istitle() (devuelve true si la cadena esta en formato titulo)

print("Hola Mundo".istitle())

#Metodo isspace() (devuelve true si la cadena esta compuesta solo por espacios)

print(" ".isspace())

#Metodo startswith() (devuelve true si la cadena comienza con la cadena indicada)

print("hola mundo".startswith("hola"))

#Metodo endswith() (devuelve true si la cadena termina con la cadena indicada)

print("hola mundo".endswith("mundo"))

#Metodo split() (devuelve una lista con las palabras de la cadena)

print("hola,mundo,soy,leandro".split(','))

#Metodo join() (devuelve una cadena que es la union de los elementos de la lista)

print(" ".join(["hola","mundo","soy","leandro"]))

#Metodo strip() (devuelve una cadena eliminando los espacios en blanco al principio y al final)

print("       hola mundo       ".strip())

#Metodo replace() (devuelve una cadena reemplazando la primera cadena por la segunda)

print("hola mundo".replace("mundo","leandro"))
