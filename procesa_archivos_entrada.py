import configuracion

def remueve_valores_de_lista(lista, val):
        while val in lista:
            lista.remove(val)

def procesa_archivo_entrada(fichero_entrada,fichero_temporal):

    for registro in fichero_entrada:
       if not registro.isspace():
            fichero_temporal.write(registro)
    fichero_temporal.seek(0)

def leer_archivo_entrada(fichero_temporal):

    registro=fichero_temporal.readline().rstrip("\n").lstrip("\n")
    return registro

def leer_reemplazo(fichero_reemplazo):
    lista=fichero_reemplazo.readline().rstrip().split(",")
    if (not lista):
        return False
    return lista

def obtiene_lista_palabras_validas(oracion):
    t = ""
    parametro = "ªº\_!?¡¿#*=<>;0123456789!?/\[]{}().,:\-\"\''"
    for registro in oracion:
        for c in registro:
            if not c in parametro:
                t += c
            else:
                 t +=' '
    t=t.upper()
    lista = t.split(" ")
    remueve_valores_de_lista(lista,"")
    return lista

def reemplaza_caracteres(oracion,fichero_reemplazo):
    fichero_reemplazo.seek(0)
    oracion_final=oracion
    lista=leer_reemplazo(fichero_reemplazo)
    while (lista!=['']):
        char_a_reemplazar,reemplazo=lista
        char_a_reemplazar=str(char_a_reemplazar)
        if char_a_reemplazar in oracion_final:
            oracion_final=oracion_final.replace(char_a_reemplazar,reemplazo)
        lista=leer_reemplazo(fichero_reemplazo)
    return oracion_final

def recorre_archivo(filename,valor):
    filename.seek(0)
    for registro in filename:
        if registro==valor:
            return True
    return False

def elimina_duplicados_y_ordena(fichero_desordenado,fichero_salida):
    fsalida=open(fichero_salida,"w+",encoding="utf8")
    fichero_desordenado.seek(0)

    for registro in fichero_desordenado:
        if (not recorre_archivo(fsalida,registro)):
            fsalida.write(registro)

    fsalida.seek(0)
    lista=fsalida.readlines();
    lista.sort()

    fsalida.close()
    fsalida=open(fichero_salida,"w+",encoding="utf8")

    for item in lista:
        fsalida.write(item)

    fsalida.close()

def procesa_archivo(fichero_entrada,file_reemplazo):

    fichero_salida=fichero_entrada + "_out"
    fichero_entrada=open(fichero_entrada,"r+",encoding="utf8")
    fichero_desordenado=open("archivo_desordenado.txt","w+",encoding="utf8")
    fichero_temporal=open("tmp.txt","w+",encoding="utf8")

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

def merge_files(filein,fileout):
    fsalida=open(fileout,"w+",encoding="utf8")
    fsalida.close()

    fsalida=open(fileout,"a",encoding="utf8")
    fentrada=open(filein,"r",encoding="utf8")

    for item in fentrada:
        fsalida.write(item)

    fentrada.close()
    fsalida.close()


#-----------------------------------------------------------------------------------------------------------------#

file_reemplazo=open("reemplazo.csv","r+",encoding="utf8")

print("Procesando archivo1.txt...")
procesa_archivo("archivo1.txt",file_reemplazo)

print("Procesando archivo2.txt...")
procesa_archivo("archivo2.txt",file_reemplazo)

print("Procesando archivo3.txt...")
procesa_archivo("archivo3.txt",file_reemplazo)

merge_files("archivo1.txt_out","palabras.txt")
merge_files("archivo2.txt_out","palabras.txt")
merge_files("archivo3.txt_out","palabras.txt")

print("Procesando palabras.txt...")
filein=open("palabras.txt","r")
elimina_duplicados_y_ordena(filein,"palabras.txt_out")

filein.close()
file_reemplazo.close()
