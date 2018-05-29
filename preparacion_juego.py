import re
import precondiciones
import random
from configuracion import diccionario_configuracion

def obtener_numero(mensaje):
    """Obtiene un numero y verifica que no se ingresen letras. Realizado por andres"""
    numero = input(mensaje)
    while not numero.isdigit():
        print("ingrese numero no letras")
        numero = input(mensaje)
    return int(numero)


def obtener_string(mensaje):
    """Obtiene un string y verifca que no se ingresen numeros. Realizado por andres"""
    palabra = input(mensaje)
    while (not re.fullmatch(r'[A-Za-z\s]+',palabra)):
        print("Ingresar solo letras o espacios en blanco")
        palabra = input(mensaje)
    return palabra

def ingresar_nombre_jugadores():
    """Solicita el numero de jugadores y sus nombres. Verifica que la cantidad de jugaddores
    no supere los 10 y devuelve la lista de jugadores ordenadas aleatororeamente. Realizada por andres"""
    seguir = True
    MAX_JUGADORES=diccionario_configuracion['MAX_USUARIOS']
    listaJugadores = []

    while seguir:
        cantidadJugadores = obtener_numero("Ingrese el numero de jugadores: ")
        if cantidadJugadores <= MAX_JUGADORES:
            seguir = False
        else:
            print("La cantidad de jugadores permitida debe ser menor a {0} , ingrese nuevamente un valor adecuado".format(MAX_JUGADORES))

    for i in range(cantidadJugadores):
        nombreJugador = obtener_string("Ingrese el nombre completo de los jugadores:")
        listaJugadores.append(nombreJugador)
        random.shuffle(listaJugadores)
    return listaJugadores

def imprimir_lista_jugadores(listaJugadores):
    """esta funcion recibe la lista de jugadores creada anteriormente y va a imprimir\
    la lista de jugadores para que los usuarios sepan el orden de juego. Realizada por andres"""

    print("el orden de juego sera:")
    for index in range(len(listaJugadores)):
        posicion=index+1
        print(posicion , listaJugadores[index])


def obtener_cantidad_de_letras_en_palabra():
    "funcion que pide a los jugadores la longitud de la palabra a adivinar , corrobora que sea mayorigual a 5\
    una vez que tiene el valor, devuelve el valor de la longitud.Realizado por andres"
    seguir = True
    LONG_PALABRA_MINIMA=diccionario_configuracion['LONG_PALABRA_MIN']
    while seguir:
        letrasEnPalabra = obtener_numero("Ingrese la cantidad de letras en la palabra: ")
        if letrasEnPalabra >= LONG_PALABRA_MINIMA:
            seguir = False
        else:
            print("La cantidad de letras en la palabra a adivinar debe ser mayor que {0}".format(LONG_PALABRA_MINIMA))
    return letrasEnPalabra

def crear_diccionario_palabras_longitud(listaPalabrasPotenciales):
    """Esta funcion crea un diccionario cuyos keys son las longitudes de palabra y contiene una lista desde
    la cual se van a obtener las palabras a adivinar. a partir de este diccionario se verifca si las palabras
    de x longitud alcanzan para la cantidad de jugadores. Realizado por andres"""

    diccionarioLongitudPalabras={}

    for palabra in listaPalabrasPotenciales:
        key=len(palabra)

        if key not in diccionarioLongitudPalabras.keys():
            diccionarioLongitudPalabras[key]=[]

        diccionarioLongitudPalabras[key].append(palabra)

    return diccionarioLongitudPalabras


def obtiene_lista_palabras_a_adivinar(diccionarioLongitudPalabras,cantidadJugadores):
    """Esta funcion pide que se ingrese el tamaño de la palabra a adivinar y si para esa
    cantidad no hay suficientes palabras pide que se ingrese un nuevo valor.
    devuelve la lista random de palabras de ese tamaño. Realizado por andres"""

    flag=True
    listaPalabrasAAdivinar=[]

    while flag:
        longitudPalabra=obtener_cantidad_de_letras_en_palabra()
        if (longitudPalabra in diccionarioLongitudPalabras.keys() and len(diccionarioLongitudPalabras[longitudPalabra]) >= cantidadJugadores):
            flag=False
        else:
            print("No hay suficientes palabras de la longitud {0} para la cantidad de jugadores {1}. Vuelva a ingresar otro tamaño de palabra".format(longitudPalabra,cantidadJugadores))

    random.shuffle(diccionarioLongitudPalabras[longitudPalabra])

    for i in range(cantidadJugadores):
        listaPalabrasAAdivinar.append(diccionarioLongitudPalabras[longitudPalabra][i])

    return listaPalabrasAAdivinar

def generar_lista_de_palabras_a_adivinar(listaDeJugadores):
    """Esta funcion llama al modulo de precondiciones y llama a las funciones que generan la lista de palabras.
    se usa en la primera ronda y en las subsiguientes rondas, cuando es llamada desde main. Realizado por andres"""

    listaDePalabrasPotenciales=precondiciones.precondiciones()
    diccionarioLongitudPalabras=crear_diccionario_palabras_longitud(listaDePalabrasPotenciales)
    listaDePalabrasAAdivinar=obtiene_lista_palabras_a_adivinar(diccionarioLongitudPalabras,len(listaDeJugadores))

    return listaDePalabrasAAdivinar

def preparacion_juego():
    """Esta es la funcion principal de este modulo se invoca desde main y se encarga de ingresar los nombres de los jugadores
    y generar la lista de palabras para la primera ronda
    Tambien devuelve las estructuras de datos necesarias en main para el funcionamiento del programa jugadores, turnos, acumulados
    Realizada por andres."""

    jugadores={}
    turnos=[]
    acumulados={}

    listaDeJugadores=ingresar_nombre_jugadores()
    imprimir_lista_jugadores(listaDeJugadores)
    listaDePalabrasAAdivinar=generar_lista_de_palabras_a_adivinar(listaDeJugadores)

    i=0
    for jugador in listaDeJugadores:
        jugadores[jugador]=[listaDePalabrasAAdivinar[i],0,0,0]
        turnos.append(jugador)
        acumulados[jugador]=[0,0,0,0]
        i+=1

    return jugadores,turnos,acumulados
