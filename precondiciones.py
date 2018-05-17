import texto
import unicodedata

def elimina_tildes(s):
    """Elimina las tildes de un string. Realizada por Leandro"""
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def obtiene_lista_palabras(oraciones):
    """Obtiene una lista de palabras del texto suministrado por la catedra. Realizada por Leandro"""
    t = ""
    parametro = "<>;0123456789!?/\[]{}().,:\-\"\'"
    for oracion in oraciones :
        for c in oracion:
            if not c in parametro:
                t += c.upper()
    lista = t.split(" ")
    return sorted(lista)

def eliminar_repetidas(lista):
    """Elimina las palabras repetidas. Realizada por Leandro"""
    final = []
    for i in lista:
        laux=elimina_tildes(i)
        if not laux in final:
            final.append(laux)
    return sorted(final)

def frecuencia_de_palabras(palabras):
    """Crea un diccionario a partir de la lista de palbras y la frecuenccia de dichas palabras. Realizada por Leandro."""
    diccionario = {}

    for i in palabras:
        if i not in diccionario.keys():
            diccionario[i]=0
        diccionario[i] += 1
    del diccionario['']
    return diccionario

def precondiciones():
    """Devuelve una lista de palabras en mayusculas y sin acentos. Realizada por Leandro"""
    oraciones = texto.obtener_texto()
    palabrasEnTexto = obtiene_lista_palabras(oraciones)
    diccionario = frecuencia_de_palabras(palabrasEnTexto)
    listaSinRepetidas=eliminar_repetidas(palabrasEnTexto)
    print("#################################### El AHORCADO ################################")
    print("A continuacion se imprimira el diccionario de palabras y la frecuencia con la que aparecen en el texto")
    print("Las palabras se convirtieron a mayusculas y se le removieron los acentos para facilitar el juego")
    laux=sorted(diccionario.items(),key=lambda x:x[0])
    for tupla in laux:
        print(tupla)

    print("#################################################################################")
    print("Cantidad de palabras en el diccionario: ", len(diccionario))
    return listaSinRepetidas

