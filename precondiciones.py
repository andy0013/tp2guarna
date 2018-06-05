import procesa_archivos_entrada

def crea_diccionario_de_palabras(filename):

    diccionario={}

    for item in filename:

        key=len(item)
        if not key in diccionario.keys():
            diccionario=[]

        diccionario[key].append(item)

    print("A continuacion se imprimiran por cada longitud de palabra las palabras que hay en el diccionario de palabras")
    print(diccionario.items())

filename=open("palabras.txt","r",encoding="utf8")
crea_diccionario_de_palabras()
