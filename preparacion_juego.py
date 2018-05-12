import precondiciones
import random

def obtener_numero(mensaje):
    numero = input(mensaje)
    while not numero.isdigit():
        print("ingrese numero no letras")
        numero = input(mensaje)
    return int(numero)


def obtener_string(mensaje):
    palabra = input(mensaje)
    while palabra.isdigit():
        print("no ingresar numeros")
        palabra = input(mensaje)
    return palabra

def ingresar_nombre_jugadores():
    seguir = True
    nombre = ""
    listaJugadores = []

    while seguir:
        cantidadJugadores = obtener_numero("Ingrese el numero de jugadores: ")
        if cantidadJugadores <= 10:
            seguir = False
        else:
            print("La cantidad de jugadores permitida debe ser menor a 10 , ingrese nuevamente un valor adecuado")

    for i in range(cantidadJugadores):
        nombreJugador = obtener_string("Ingrese el nombre completo de los jugadores:")
        listaJugadores.append(nombreJugador)
    return listaJugadores

def imprimir_lista_jugadores(listaJugadores):
    "esta funcion recibe la lista de jugadores creada anteriormente y va a imprimir\
    una lista random de jugadores para que los usuarios sepan el orden de juego\
    y va a devolver la lista random "

    random.shuffle(listaJugadores)
    print("el orden de juego sera:")
    for index in range(len(listaJugadores)):
        posicion=index+1
        print(posicion , listaJugadores[index])


def obtener_cantidad_de_letras_en_palabra():
    "funcion que pide a los jugadores la longitud de la palabra a adivinar , corrobora que sea mayorigual a 5\
    una vez que tiene el valor, devuelve el valor de la longitud"
    seguir = True
    while seguir:
        letrasEnPalabra = obtener_numero("Ingrese la cantidad de letras en la palabra: ")
        if letrasEnPalabra > 5:
            seguir = False
        else:
            print("La cantidad de letras en la palabra a adivinar debe ser mayor que 5")
    return letrasEnPalabra

def crear_diccionario_palabras_longitud(listaPalabrasPotenciales):

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
    devuelve la lista random de palabras de ese tamaño"""

    flag=True
    listaPalabrasAAdivinar=[]

    while flag:
        longitudPalabra=obtener_cantidad_de_letras_en_palabra()
        if (len(diccionarioLongitudPalabras[longitudPalabra]) >= cantidadJugadores):
            flag=False
        else:
            print("No hay suficientes palabras de la longitud {0} para la cantidad de jugadores {1}. Vuelva a ingresar otro tamaño de palabra".format(longitudPalabra,cantidadJugadores))

    for i in range(cantidadJugadores):
        listaPalabrasAAdivinar.append(diccionarioLongitudPalabras[longitudPalabra][i])

    return random.shuffle(listaPalabrasAAdivinar)


def preparacion_juego():

    jugadores={}

    listaDePalabrasPotenciales=precondiciones.precondiciones()

    listaDeJugadores=ingresar_nombre_jugadores()
    imprimir_lista_jugadores(listaDeJugadores)
    diccionarioLongitudPalabras=crear_diccionario_palabras_longitud(listaDePalabrasPotenciales)
    listaDePalabrasAAdivinar=obtiene_lista_palabras_a_adivinar(diccionarioLongitudPalabras,len(listaDeJugadores))

    i=0
    for jugador in listaDeJugadores
        jug
