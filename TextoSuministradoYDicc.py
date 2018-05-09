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
        if not i in final:
            final.append(elimina_tildes(i))
    final.remove('')
    return final

def CrearDicc(palabras):
    dicc = {}
    for n in palabras:
        if not n in dicc :
            dicc[n] = 1
        else:
            dicc[n] += 1
    del dicc['']
    del dicc["A"]
    return dicc

def CantDePalabras(dicc):
    contador = len(dicc)
    return contador

l_oraciones = texto.obtener_texto()
PalabrasEnTexto = Palabras(l_oraciones)
PalabrasValidas = EliminarRepes(PalabrasEnTexto)
Dicc = CrearDicc(PalabrasEnTexto)
print(Dicc)
print("Cant. de palabras en diccionario: ", CantDePalabras(Dicc))