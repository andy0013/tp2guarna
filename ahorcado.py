import random

def cantidad_de_personas_nombres(mensaje,mensajedos):
   "esta funcion va a pedir la cantidad de jugadores , corroborar que sean menores a diez\
   luego va a pedir los nombres de los jugadores , y devuelve una lista de jugadores"

    seguir = True
    nombre = " "
    lista_con_nombres = []
    while seguir:
        personas = int(input(mensaje))
        if personas <= 10:
            seguir = False
        else:
            print("La cantidad de jugadores permitida debe ser menor a 10 , ingrese nuevamente un valor adecuado")

    for nombre in range(personas):
        nombre = input(mensajedos)
        lista_con_nombres += [nombre]
    return lista_con_nombres

def darlistanombresrandom(lista):
    "esta funcion recibe la lista de jugadores creada anteriormente y va a imprimir\
    una lista random de jugadores para que los usuarios sepan el orden de juego\
    y va a devolver la lista random "

    random.shuffle(lista,random.random)
    print("el orden de juego sera:")
    for nombre in range(len(lista)):
        print(nombre+1 , lista[nombre])
    return lista

def lista_de_las_palabras_con_su_longitud(lista):
    "esta funcion va a llamar a la lista proporcionada por Lean(\
    una lista de palabras sin repetir , etc) y va a crear un diccionario con la palabra y, su valor\
    que va a ser la cantidad de letras que tiene , para que despues los usuarios eligan la cantidad\
    de letras que van a adivinar y otorgarles las palabras,despues devuelve una lista que tiene\
    la palabra y cantidad de letras"

    palabra_y_longitud = []
    palabras_y_numero_letras = {}
    for palabras in lista:
        valor = len(palabras)
        palabras_y_numero_letras[palabras] = valor
    palabra_y_longitud = palabras_y_numero_letras.items()
    return palabra_y_longitud

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
    "esta funcion deberia devolver lo que vos pedis Pablo,pero aun no se como hacerla"
    jugadorysupalabra = {}
    random.shuffle(listadepalasconletra,random.random)
    cantidaduno = len(lista_de_nombres_random)
    cantidaddos = len(listadepalasconletra)
    if cantidaduno < cantidaddos:
        for nombres in range(len(lista_de_nombres_random)):
            jugadorysupalabra[nombres] = " "

texto = "anmistia caminando caminar almohada  camilla cantante animadores animales autistas antes"
lista_palabras_en_texto = (lista_de_las_palabras_con_su_longitud(texto))
lista_de_nombres = (cantidad_de_personas_nombres("cantidad de personas a jugar","nombre de persona"))
lista_de_nombres_random = (darlistanombresrandom(lista_de_nombres))
numero_de_letras = cantidaddeletras("cantidad de letras","solo mayor igual a 5")
listadepalasconletra = (darlistadepalabrasentextoconletrapedida(lista_palabras_en_texto,numero_de_letras))
print(listadepalasconletra)
print(asignarpalabraacadajugador(lista_de_nombres_random,listadepalasconletra))
