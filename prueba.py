def leer_reemplazo(fichero_reemplazo):
    lista=fichero_reemplazo.readline().rstrip().split(",")
    if (not lista):
        return False
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

file=open("prueba.txt","r")
fichero_reemplazo=open("reemplazo2.csv","r")
fichero_salida=open("salida.txt","w+")

oracion=file.readline().rstrip()
while (oracion!=""):
    texto=reemplaza_caracteres(oracion,fichero_reemplazo)
    fichero_salida.write(texto+"\n")
    oracion=file.readline().rstrip()


