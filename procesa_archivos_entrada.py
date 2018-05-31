
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

file_reemplazo=open("reemplazo.csv","r",encoding="utf8")
fichero_entrada=open("La araña negra - tomo 1.txt","r")
fichero_desordenado=open("archivo_desordenado.txt","r+",encoding="utf8")
fichero_temporal=open("tmp.txt","r+",encoding="latin1")

def procesa_archivo(fichero_entrada,fichero_desordenado,fichero_temporal,file_reemplazo):
    procesa_archivo_entrada(fichero_entrada,fichero_temporal)
    oracion=leer_archivo_entrada(fichero_temporal)

    while(oracion!=""):
        oracion=reemplaza_caracteres(oracion,file_reemplazo)
        lista=obtiene_lista_palabras_validas(oracion)
        for palabra in lista:
            fichero_desordenado.write(palabra+"\n")
        oracion=leer_archivo_entrada(fichero_temporal)

procesa_archivo(fichero_entrada,fichero_desordenado,fichero_temporal,file_reemplazo)


file_reemplazo.close()
fichero_entrada.close()
fichero_desordenado.close
fichero_temporal.close()
