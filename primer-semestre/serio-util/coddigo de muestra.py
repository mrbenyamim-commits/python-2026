import random #importa la funcion de obtener cosas aleatorias
import time #importa la funcion de agregar un tiempo de espera

# el import es para sacar una funcion de una libreria

lista = (14,"diabloz","sexo") # esto es una lista la cual almacena multiples variables

diccionario = { # es un diccionario para guardar multiples listas
    "zapo": (1, "hola", "chao"), # esta es la primera lista
    "coño": ("sexto", "roberto", 12)} # y esta es la segunda

lista_random = random.choice(lista) #selecciona uno de las variables de la lista

diccionario_random = random.choice(list(diccionario)) #selecciona uno de las listas del diccionario

numero_random = random.randint(1, 3) # seleciona un numero aleatorio entre el 1 al 3 como una variable

print("\n",lista, "\n") # "\n" se usa para bajar una linea y ejecuta la lista completa
print(lista_random, "\n") # esto ejecuta la variable de un objeto aleatorio de la lista

time.sleep (1) # esto es el tiempo de espera de 1 segundo

print(numero_random, "\n") # esto ejecuta un numero aleatorio de la variable numero aleatorio

time.sleep (1) 

print(diccionario, "\n") # ejecuta el diccionario completo

print(diccionario_random, "\n") #esto ejecuta el titulo de una lista del dicionario de forma aleatoria

time.sleep (1) 

duda = input("aqui se ingresa un texto \n") #se ingresara un texto o nada pero abajo se puede escribir algo y lo guardara como una variable de texto y se tratara como tal

numero = int(input("aqui ingresar un numero \n")) #esto sirve para pasar lo escrito como un numero que se tratara como tal

calculo = numero * numero_random  #se multiplica el numero por el numero aleatorio

print(numero, "x", numero_random,  "=", calculo) #aqui muestra el calculo