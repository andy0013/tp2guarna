def leer_archivo_entrada(file):
    registro=file.readline().rstrip()
    return registro

def leer_reemplazo(file):
    lista=file.readline().rstrip().split(",")
    if (lista==""):
        return True
    return False

def obtiene_lista_palabras(oracion):
    t = ""
    parametro = "<>;0123456789!?/\[]{}().,:\-\"\'"
    for registro in oracion :
        for c in registro:
            if not c in parametro:
                t += c.upper()
    lista = t.split(" ")
    return lista

def reemplaza_caracteres(oracion,file_reemplazo):

    salida=leer_reemplazo(file_reemplazo)
    while (salida==False):
        for char_a_reemplazar, reemplazo in enumerate(lista)
            if char_a_reemplazar in oracion:
                oracion.replace(char_a_reemplazar,reemplazo)
        salida=leer_reemplazo(file_reemplazo)

file_reemplazo=open("reemplazo.csv","r")

f=open("La araña negra - tomo 1.txt","r")
oracion=leer_archivo(f)

file=open("archivo_desordenado.txt","w")

f.close()
