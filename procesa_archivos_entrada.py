
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
    parametro = "!?¡¿<>;0123456789!?/\[]{}().,:\-\"\''"
    for registro in oracion:
        for c in registro:
            if not c in parametro:
                t += c.upper()
    lista = t.split(" ")
    try:
        lista.remove("")
        lista.remove(",")
    except Exception:
        pass
    return lista

def reemplaza_caracteres(oracion,fichero_reemplazo):
    fichero_reemplazo.seek(0)
    lista=leer_reemplazo(fichero_reemplazo)
    while (lista != ['']):
        char_a_reemplazar,reemplazo=lista
        char_a_reemplazar=str(char_a_reemplazar)
        if char_a_reemplazar in oracion:
            oracion=oracion.replace(char_a_reemplazar,reemplazo)
        lista=leer_reemplazo(fichero_reemplazo)
    return oracion

file_reemplazo=open("reemplazo.csv","r",encoding="latin1")

def procesa_archivo(fichero_entrada,file_reemplazo):

    fichero_salida=fichero_entrada + "_out"
    fichero_salida=open(fichero_salida,"w+")
    fichero_entrada=open(fichero_entrada,"r")
    fichero_desordenado=open("archivo_desordenado.txt","w+",encoding="latin1")
    fichero_temporal=open("tmp.txt","w+",encoding="latin1")

    procesa_archivo_entrada(fichero_entrada,fichero_temporal)
    oracion=leer_archivo_entrada(fichero_temporal)

    while(oracion!=""):
        oracion=reemplaza_caracteres(oracion,file_reemplazo)
        lista=obtiene_lista_palabras_validas(oracion)
        for palabra in lista:
            fichero_desordenado.write(palabra+"\n")
        oracion=leer_archivo_entrada(fichero_temporal)



    fichero_entrada.close()
    fichero_desordenado.close
    fichero_temporal.close()

#-----------------------------------------------------------------------------------------------------------------#

procesa_archivo("prueba.txt",file_reemplazo)
file_reemplazo.close()
