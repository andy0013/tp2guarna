import procesa_archivos_entrada
import configuracion

def imprimir_configuracion(diccionario):
    print("Los parametros de configuracion son los siguientes:\n")

    for tupla in diccionario.items():
        print(tupla)
    print("\n")

def crea_diccionario_de_palabras(filein):

    diccionario={}

    for item in filein:
        item=item.strip("\n")
        key=len(item)
        if not key in diccionario.keys():
            diccionario[key]=[]

        diccionario[key].append(item)

    print("A continuacion se imprimira el diccionario de palabras ordenada por su tamaño")
    listaAux=sorted(diccionario.items(),key=lambda x: x[0],reverse=False)
    acumulador=0
    for item in listaAux:
        print (item)
        acumulador+=len(item[1])

    print("Hay {0} palabras para elegir".format(acumulador))
    return diccionario

imprimir_configuracion(configuracion.diccionario_configuracion)
filename=open("palabras.txt_out","r",encoding="utf8")
diccionarioLongitudPalabras=crea_diccionario_de_palabras(filename)
filename.close()
