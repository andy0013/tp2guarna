import re
import texto
import unicodedata

def elimina_tildes(s):
    """Elimina las tildes de un string. Realizada por Leandro"""
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def obtiene_lista_palabras(oraciones):
    """Obtiene una lista de palabras del texto suministrado por la catedra. Realizada por Leandro"""
    listaf = []
    for i in oraciones :
        lista = re.split("[(, \-!?:)\"\.;><1234567890]+" , i.upper())
        listaf.extend(lista)
    return sorted(listaf)

def eliminar_repetidas(lista):
    """Elimina las palabras repetidas. Realizada por Leandro"""
    final = []
    for i in lista:
        if not i in final:
            final.append(elimina_tildes(i))
    return sorted(final)

def crear_diccionario(validas, palabras):
    """Crea un diccionario a partir de la lista de palbras y la frecuenccia de dichas palabras. Realizada por Leandro."""
    diccionario = {}
    for n in validas:
        diccionario[n] = 0
    for i in palabras:
        if i in diccionario:
            diccionario[i] += 1
    del diccionario['']
    return diccionario

def precondiciones():
    """Devuelve una lista de palabras en mayusculas y sin acentos. Realizada por Leandro"""
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
    return(list(diccionario.keys()))

print(precondiciones())
