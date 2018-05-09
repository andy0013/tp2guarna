import re
import texto
import unicodedata

def elimina_tildes(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def Palabras(oraciones):
    listaf = []
    for i in oraciones :
        lista = re.split("[(, \-!?:)\".;><1234567890]+" , i.upper())
        listaf.extend(lista)
    return sorted(listaf)

def EliminarRepes(texto):
    final = []
    for i in texto:
        if (len(i) >= 5):
            if not i in final:
                final.append(elimina_tildes(i))
    return sorted(final)

def CrearDicc(validas, palabras):
    dicc = {}
    for n in validas:
        dicc[n] = 0
    for i in palabras:
        if i in dicc:
            dicc[i] += 1
    return dicc

def CantDePalabras(dicc):
    contador = len(dicc)
    return contador

l_oraciones = texto.obtener_texto()
PalabrasEnTexto = Palabras(l_oraciones)
PalabrasValidas = EliminarRepes(PalabrasEnTexto)
Dicc = CrearDicc(PalabrasValidas, PalabrasEnTexto)
print(PalabrasEnTexto)
print(PalabrasValidas)
print(Dicc)
print("Cant. de palabras en diccionario: ", CantDePalabras(Dicc))