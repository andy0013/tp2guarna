import re
import texto
import unicodedata

def elimina_tildes(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def obtiene_lista_palabras(oraciones):
    listaf = []
    for i in oraciones :
        lista = re.split("[(, \-!?:)\"\.;><1234567890]+" , i.upper())
        listaf.extend(lista)
    return sorted(listaf)

def eliminar_repetidas(texto):
    final = []
    for i in texto:
        if (len(i) >= 5):
            if not i in final:
                final.append(elimina_tildes(i))
    return sorted(final)

def crear_diccionario(validas, palabras):
    dicc = {}
    for n in validas:
        dicc[n] = 0
    for i in palabras:
        if i in dicc:
            dicc[i] += 1
    return dicc

def precondiciones():
    oraciones = texto.obtener_texto()
    palabrasEnTexto = obtiene_lista_palabras(oraciones)
    palabrasValidas = eliminar_repetidas(palabrasEnTexto)
    diccionario = crear_diccionario(palabrasValidas, palabrasEnTexto)
    print("#################################### El AHORCADO ################################")
    print("A continuacion se imprimira el diccionario de palabras y la frecuencia con la que aparecen en el texto")
    print("Las palabras se convirtieron a mayusculas y se le removieron los acentos para facilitar el juego")
    print(diccionario)
    print("#################################################################################")
    print("Cantidad de palabras en el diccionario: ", len(diccionario))
    return(diccionario)

precondiciones()
