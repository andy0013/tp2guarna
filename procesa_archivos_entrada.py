
def leer_archivo_entrada(file):
    registro=file.readline().rstrip()
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

file_reemplazo=open("reemplazo.csv","r",encoding="utf8")
f=open("La araña negra - tomo 1.txt","r")
file2=open("archivo_desordenado.txt","w")

def procesa_archivo(f,file2,file_reemplazo):
    oracion=leer_archivo_entrada(f)

    while(oracion==""):
        oracion=reemplaza_caracteres(oracion,file_reemplazo)
        lista=obtiene_lista_palabras_validas(oracion)
        for palabra in lista:
            file2.write(palabra+ "\n")
        oracion=leer_archivo_entrada(f)

procesa_archivo(f,file2,file_reemplazo)


file_reemplazo.close()
f.close()
file2.close
