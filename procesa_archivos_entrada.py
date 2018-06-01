
def remueve_valores_de_lista(lista, val):
        while val in lista:
            lista.remove(val)

def procesa_archivo_entrada(fichero_entrada,fichero_temporal):

    for registro in fichero_entrada:
       if not registro.isspace():
            fichero_temporal.write(registro)
    fichero_temporal.seek(0)

def leer_archivo_entrada(fichero_temporal):

    registro=fichero_temporal.readline().rstrip("\n\s").lstrip("\n\s")
    return registro

def leer_reemplazo(fichero_reemplazo):
    lista=fichero_reemplazo.readline().rstrip().split(",")
    if (not lista):
        return False
    return lista

def obtiene_lista_palabras_validas(oracion):
    t = ""
    parametro = "!?¡¿#*=<>;0123456789!?/\[]{}().,:\-\"\''"
    for registro in oracion:
        for c in registro:
            if not c in parametro:
                t += c.upper()
    lista = t.split(" ")
    remueve_valores_de_lista(lista,"")
    return lista

def reemplaza_caracteres(oracion,fichero_reemplazo):
    fichero_reemplazo.seek(0)
    oracion_final=oracion
    lista=leer_reemplazo(fichero_reemplazo)
    while (lista != ['']):
        char_a_reemplazar,reemplazo=lista
        char_a_reemplazar=str(char_a_reemplazar)
        if char_a_reemplazar in oracion:
            oracion_final=oracion.replace(char_a_reemplazar,reemplazo)
        lista=leer_reemplazo(fichero_reemplazo)
    return oracion_final

def recorre_archivo(filename,valor):
    filename.seek(0)
    for registro in filename:
        if registro==valor:
            return True
    return False

def elimina_duplicados_y_ordena(fichero_desordenado,fichero_salida):
    fsalida=open(fichero_salida,"w+")
    fichero_desordenado.seek(0)

    for registro in fichero_desordenado:
        if (not recorre_archivo(fsalida,registro)):
            fsalida.write(registro)

    fsalida.seek(0)
    lista=fsalida.readlines();
    lista.sort()

    fsalida.close()
    fsalida=open(fichero_salida,"w+")

    for item in lista:
        fsalida.write(item)

def procesa_archivo(fichero_entrada,file_reemplazo):

    fichero_salida=fichero_entrada + "_out"
    fichero_entrada=open(fichero_entrada,"r+")
    fichero_desordenado=open("archivo_desordenado.txt","w+")
    fichero_temporal=open("tmp.txt","w+")

    procesa_archivo_entrada(fichero_entrada,fichero_temporal)
    oracion=leer_archivo_entrada(fichero_temporal)

    while(oracion!=""):
        oracion=reemplaza_caracteres(oracion,file_reemplazo)
        lista=obtiene_lista_palabras_validas(oracion)
        for palabra in lista:
            fichero_desordenado.write(palabra+"\n")
        oracion=leer_archivo_entrada(fichero_temporal)

    elimina_duplicados_y_ordena(fichero_desordenado,fichero_salida)

    fichero_entrada.close()
    fichero_desordenado.close
    fichero_temporal.close()



#-----------------------------------------------------------------------------------------------------------------#

file_reemplazo=open("reemplazo.csv","r+",encoding = "utf8")

procesa_archivo("prueba.txt",file_reemplazo)


file_reemplazo.close()
