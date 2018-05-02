import random

def cantidad_de_personas_nombres(mensaje,mensajedos):
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
        """Porque no usar append"""
        lista_con_nombres += [nombre]
    return lista_con_nombres

def darlistanombresrandom(lista):
    random.shuffle(lista,random.random)
    print("el orden de juego sera:")
    for nombre in range(len(lista)):
        print(nombre+1 , lista[nombre])
    return lista

def lista_de_las_palabras_con_su_longitud(texto):
    texto1 = texto.split()
    palabra_y_longitud = []
    palabras_y_numero_letras = {}
    for palabras in texto1:
        valor = len(palabras)
        palabras_y_numero_letras[palabras] = valor
    palabra_y_longitud = palabras_y_numero_letras.items()
    return palabra_y_longitud

def cantidaddeletras(mensaje,mensaje2):
    seguir = True
    while seguir:
        letrasenpalabra = int(input(mensaje))
        if letrasenpalabra >= 5:
            seguir = False
        else:
            print(mensaje2)
    return letrasenpalabra

def darlistadepalabrasentextoconletrapedida(lista_palabras_en_texto,numero_de_letras):
    palabras_en_el_texto = []
    for palabras in lista_palabras_en_texto:
        if palabras[1] == numero_de_letras:
            palabras_en_el_texto += [palabras[0]]
    return palabras_en_el_texto

#solo me falta terminar la funcion de abajo,para que arme un diccionario con clave(nombre de jugador) = valor(palabra asignada a adivinar)
def asignarpalabraacadajugador(lista_de_nombres_random,listadepalasconletra):
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

