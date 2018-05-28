def leer_archivo_configuracion(file):

    diccionario={'MAX_USUARIOS': 10,'LONG_PALABRA_MIN':5,'MAX_DESACIERTOS':7,'PUNTOS_ACIERTOS':2,'PUNTOS_DESACIERTOS':1,'PUNTOS_ADIVINA':30}

    registro=file.readline()

    while (registro):
        lista=registro.rstrip().split(" ")
        if lista==[""]:
            return diccionario
        key=lista[0]
        value=lista[1]
        diccionario[key]=value
        registro=file.readline()

    return diccionario

file=open("configuracion.txt","r")
diccionario_configuracion=leer_archivo_configuracion(file)


