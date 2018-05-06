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

l_oraciones = texto.obtener_texto()
PalabrasEnTexto = Palabras(l_oraciones)
PalabrasValidas= EliminarRepes(PalabrasEnTexto)
Dicc = CrearDicc(PalabrasEnTexto)
print(PalabrasEnTexto)
print(PalabrasValidas)
print(Dicc)
print("Cant. de palabras en diccionario: ", CantDePalabras(Dicc))
