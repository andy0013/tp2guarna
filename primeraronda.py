def datos_jugador(lista):

    nombre=lista[0]
    palabraAdivinar=lista[1]
    aciertos=lista[2]
    desaciertos=lista[3]
    puntaje=lista[4]

    print ("El nombre del jugador es {0} y la cantidad de aciertos es {1}, de desaciertos{2} y el puntaje total hasta el momento es {3}".format(nombre,aciertos,desaciertos,puntaje))
    return palabraAdivinar

def incrementar_desaciertos(turnoActual,turnos):
    turnos[turnoActual][3]+=1
    return turnos[turnoActual][3]


"""nombre,palabra a adivinar,aciertos,desaciertos,intentos,puntaje"""
turnos=[['juan','testing',0,0,0,0],['pedro','escarapela',0,0,0,0]]

salir=False

while (salir != True):

    ronda=turnos[:]

    while(len(ronda) != 0)

        for idx,juagador in enumerate(ronda):
            palabraAAdinar=datos_jugador(jugador)

            letra=input("Ingrese una letra:")

            if letra in palabraAAdinar:
                mostrar_posicion(letra,palabraAAdinar)

            else:
                desaciertos=incrementar_desaciertos(idx,turnos)

            if (desaciertos==7):
                del ronda[idx]
                continue



