import random
import re
import texto

def Palabras(oraciones):
    listaf = []
    for i in oraciones :
        lista = re.split("[(, \-!?:).\";><1234567890]+" , i )
        listaf.extend(lista)
    return sorted(listaf)

def EliminarRepes(texto):
    final = []
    for i in texto:
        if not i in final:
            final.append(i)
    return final

def CrearDicc(palabras):
    dicc = {}
    for n in palabras:
        if n not in dicc :
            dicc[n] = 1
        else:
            dicc[n] += 1
    del dicc['']
    return dicc

def CantDePalabras(dicc):
    """no es lo mismo que usar len"""
    contador = 0
    for n in dicc :
        contador += 1
    return contador
def numero(mensaje):
    x = input(mensaje)
    while not x.isdigit():
        print("ingrese numero no letras")
        x = input(mensaje)
    return x


def palabra(mensaje):
    x = input(mensaje)
    while x.isdigit():
        print("no ingresar numeros")
        x = input(mensaje)
    return x

def usuarios_nombres(mensaje,mensajedos):
    seguir = True
    nombre = " "
    lista_con_nombres = []
    while seguir:
        personas = int(numero(mensaje))
        if personas <= 10:
            seguir = False
        else:
            print("La cantidad de jugadores permitida debe ser menor a 10 , ingrese nuevamente un valor adecuado")
    for nombre in range(personas):
        nombre = palabra(mensajedos)
        lista_con_nombres += [nombre]
    return lista_con_nombres

def l_random(lista):
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
