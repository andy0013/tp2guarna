import configuracion

def remueve_valores_de_lista(lista, val):
        """remueve valores pasados por parametro de una lista"""
        while val in lista:
            lista.remove(val)

def procesa_archivo_entrada(fichero_entrada,fichero_temporal):
    """ Esta funcion quita los renglones en blanco de los archivos, ya que si no no los podia leer sin que parezca un EOF"""

    for registro in fichero_entrada:
       if not registro.isspace():
            fichero_temporal.write(registro)
    fichero_temporal.seek(0)

def leer_archivo_entrada(fichero_temporal):
    """Le el archivo de entrada y devuelve un registro"""

    registro=fichero_temporal.readline().rstrip("\n").lstrip("\n")
    return registro

def leer_reemplazo(fichero_reemplazo):
    """Esta funcion lee los registros del archivo reemplazo.csv para reemplazar los valores en el texto"""
    lista=fichero_reemplazo.readline().rstrip().split(",")
    if (not lista):
        return False
    return lista

def obtiene_lista_palabras_validas(oracion):
    """Esta funcion genera palabras validas funciona como complementos del archivo reemplazo.csv, ya que no hay que
    reemplazar nada"""

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
    """Reemplaza strings del archivo reemplazo.csv en el texto"""
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
    """Esta es una funcion que recorre un archivo y si el registro coincide con valor devuelve true. Se usa para eliminar
    duplicados"""
    filename.seek(0)
    for registro in filename:
        if registro==valor:
            return True
    return False

def elimina_duplicados_y_ordena(fichero_desordenado,fichero_salida):
    """Elimina las palabras duplicadas de un archivo y las ordena alfabeticamente.
    Segun lo respondido por la catedra las palabras si se pueden subir a memoria y ordenar"""
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
    """funcion que procesa cada archivo de entrada."""

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

def grabar_nuevo(fileout,valor):
    fileout.write(valor+"\n")

def merge_files(filein1,filein2,fileout):
    """Proceso de merge de los archivos de entrada"""

    fsalida=open(fileout,"w+",encoding="utf8")
    fentrada1=open(filein1,"r",encoding="utf8")
    fentrada2=open(filein2,"r",encoding="utf8")

    palabra1=leer_archivo_entrada(fentrada1)
    palabra2=leer_archivo_entrada(fentrada2)

    while (palabra1 and palabra2):

        if (palabra1==palabra2):
            grabar_nuevo(fsalida,palabra1)
            grabar_nuevo(fsalida,palabra2)
        elif (palabra1 > palabra2):
            grabar_nuevo(fsalida,palabra1)
            grabar_nuevo(fsalida,palabra2)
        elif (palabra2 > palabra1):
            grabar_nuevo(fsalida,palabra2)
            grabar_nuevo(fsalida,palabra1)

        palabra1=leer_archivo_entrada(fentrada1)
        palabra2=leer_archivo_entrada(fentrada2)

    while(palabra1):
        grabar_nuevo(fsalida,palabra1)
        palabra1=leer_archivo_entrada(fentrada1)

    while(palabra2):
        grabar_nuevo(fsalida,palabra2)
        palabra2=leer_archivo_entrada(fentrada2)


    fentrada1.close()
    fentrada2.close()
    fsalida.close()


#-----------------------------------------------------------------------------------------------------------------#

file_reemplazo=open("reemplazo.csv","r+",encoding="utf8")

print("Procesando archivo1.txt...")
procesa_archivo("archivo1.txt",file_reemplazo)

print("Procesando archivo2.txt...")
procesa_archivo("archivo2.txt",file_reemplazo)

print("Procesando archivo3.txt...")
procesa_archivo("archivo3.txt",file_reemplazo)

merge_files("archivo1.txt_out","archivo2.txt_out","fsalida_merge1.txt")
merge_files("fsalida_merge1.txt","archivo3.txt_out","palabras.txt")

print("Procesando palabras.txt...")
filein=open("palabras.txt","r")
elimina_duplicados_y_ordena(filein,"palabras.txt_out")

filein.close()
file_reemplazo.close()
