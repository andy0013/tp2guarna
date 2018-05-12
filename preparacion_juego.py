import precondiciones
import random

def obtener_numero(mensaje):
    numero = input(mensaje)
    while not numero.isdigit():
        print("ingrese numero no letras")
        numero = input(mensaje)
    return numero


def obtener_palabra(mensaje):
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
        cantidadJugadores = int(obtener_numero("Ingrese el numero de jugadores: "))
        if cantidadJugadores <= 10:
            seguir = False
        else:
            print("La cantidad de jugadores permitida debe ser menor a 10 , ingrese nuevamente un valor adecuado")

    for i in range(cantidadJugadores):
        nombreJugador = obtener_palabra("Ingrese el nombre completo de los jugadores:")
        listaJugadores.append(nombreJugador)
    return listaJugadores

def obtener_lista_jugadores(listaJugadores):
    "esta funcion recibe la lista de jugadores creada anteriormente y va a imprimir\
    una lista random de jugadores para que los usuarios sepan el orden de juego\
    y va a devolver la lista random "

    random.shuffle(listaJugadores)
    print("el orden de juego sera:")
    for index in range(len(listaJugadores)):
        posicion=index+1
        print(posicion , listaJugadores[index])
    return listaJugadores

def cantidaddeletras(mensaje,mensaje2):
    "funcion que pide a los jugadores la longitud de la palabra a adivinar , corrobora que sea mayorigual a 5\
    una vez que tiene el valor, devuelve el valor de la longitud"
    seguir = True
    while seguir:
        letrasenpalabra = int(input(mensaje))
        if letrasenpalabra >= 5:
            seguir = False
        else:
            print(mensaje2)
    return letrasenpalabra

def obtiene_lista_palabras_a_adivinar(lista):

def darlistadepalabrasentextoconletrapedida(lista_palabras_en_texto,numero_de_letras):
    "esta funcion recibe la lista de de palabras con su valor de longitud de letras\
    que fue hecha en la funcion (lista_de_las_palabras_con_su_longitud) y recibe\
    el valor que contiene la cantidad de letras a adivinar que devuelve la funcion\
    (cantidaddeletras), con esos valores busca la palabra que tenga la cantidad de letras pedida,\
    finalmente devuelve una lista con las palabras que tienen la longitud ingresada"

    palabras_en_el_texto = []
    for palabras in lista_palabras_en_texto:
        if palabras[1] == numero_de_letras:
            palabras_en_el_texto += [palabras[0]]
    return palabras_en_el_texto


def asignarpalabraacadajugador(lista_de_nombres_random,listadepalasconletra):
    "esta funcion deberia devolver lo que vos pedis Pablo"
    jugadorysupalabra = {}
    random.shuffle(listadepalasconletra,random.random)
    cantidaduno = len(lista_de_nombres_random)
    for numeros in range(cantidaduno):
        jugadorysupalabra[lista_de_nombres_random[numeros]] = [listadepalasconletra[numeros],0,0,0]
    return jugadorysupalabra

def Pablo():
    nombres = usuarios_nombres("ingrese la cantidad de jugadores: ","ingrese el nombre de el jugador: ")
    turnos = l_random(nombres)
    letra = cantidaddeletras("ingrese cantidad de letras: ","ingrese solo un numero mayor a 5")
    lista_longitud = lista_de_las_palabras_con_su_longitud(PalabrasValidas)
    lista_hecha = darlistadepalabrasentextoconletrapedida(lista_longitud,letra)
    l_final = asignarpalabraacadajugador(turnos,lista_hecha)
    return l_final


l_oraciones = texto.obtener_texto()
PalabrasEnTexto = Palabras(l_oraciones)
PalabrasValidas= EliminarRepes(PalabrasEnTexto)
Dicc = CrearDicc(PalabrasEnTexto)
print(Pablo())
