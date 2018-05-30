def procesa_archivo_entrada(file,file2):

    for registro in file:
       if not registro.isspace():
            file2.write(registro)
    file2.seek(0)

def leer_archivo_entrada(file):

    registro=file.readline().rstrip("\n\s").lstrip("\n\s")
    return registro

def leer_reemplazo(file):
    lista=file.readline().rstrip().split(",")
    if (not lista):
        return False
    return lista

def obtiene_lista_palabras_validas(oracion):
    t = ""
    parametro = "<>;0123456789!?/\[]{}().,:\-\"\''"
    for registro in oracion :
        for c in registro:
            if not c in parametro:
                t += c.upper()
    lista = t.split(" ")
    return lista

def reemplaza_caracteres(oracion,file_reemplazo):

    lista=leer_reemplazo(file_reemplazo)
    while (lista != ['']):
        char_a_reemplazar,reemplazo=lista
        char_a_reemplazar=str(char_a_reemplazar)
        if char_a_reemplazar in oracion:
            oracion.replace(char_a_reemplazar,reemplazo)
        lista=leer_reemplazo(file_reemplazo)
    return oracion

file_reemplazo=open("reemplazo.csv","r",encoding='latin-1')
f=open("La araña negra - tomo 1.txt","r",encoding='latin-1')
file2=open("archivo_desordenado.txt","w")
file3=open("tmp.txt","r+")

def procesa_archivo(f,file2,file3,file_reemplazo):
    procesa_archivo_entrada(f,file3)
    oracion=leer_archivo_entrada(file3)

    while(oracion!=""):
        oracion=reemplaza_caracteres(oracion,file_reemplazo)
        lista=obtiene_lista_palabras_validas(oracion)
        for palabra in lista:
            file2.write(palabra+ "\n")
        oracion=leer_archivo_entrada(file3)

procesa_archivo(f,file2,file3,file_reemplazo)


file_reemplazo.close()
f.close()
file2.close
