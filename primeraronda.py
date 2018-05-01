def datos_jugador(jugador,jugadores):
    """Esta funcion muestra los datos acumulados de los jugadores"""
    palabra=jugadores[jugador][0]
    aciertos=jugadores[jugador][1]
    desaciertos=jugadores[jugador][2]
    puntaje=jugadores[jugador][3]

    print("el jugador {0} tiene {1} aciertos, {2} desaciertos, {3} intentos y un puntaje de {4}".format(jugador,aciertos,desaciertos,intentos,puntaje))
    return palabra

def incrementar_desaciertos(jugador,jugadores):
    """Esta funcion se utiliza para incrementar los desaciertos"""
    jugadores[jugador][2]+=1
    return jugadores[jugador][2]

def suma_aciertos(jugador,jugadores):
    jugadores[jugador][1]+=1

def resta_puntos(jugador,jugadores):
    """Esta funcion se utiliza para restar puntos a los jugadores"""
    puntaje=jugadores[jugador][3]

    if (puntaje > 2):
        jugadores[jugador][3]-=2
    elif (puntaje == 1):
        jugadores[jugador][3]-=1

def suma_puntos(jugador,jugadores,puntos):
    """Esta funcion se utiliza para sumar puntos a los jugadores puede ser un punto o 30 se pasa por parametro"""
    jugadores[jugador][3]+=puntos

def acumula_valores(jugadores,acumulados):
    """esta funcion acumula en cada partida los valores de jugadores se la paso a ignacio para que imprima los valores"""

    for jugador in jugadores:
        acumulados[jugador][0]+=1
        acumulados[jugador][1]+=jugadores[jugador][1]
        acumulados[jugador][2]+=jugadores[jugador][2]
        acumulados[jugador][3]+=jugadores[jugador][3]

def letrasPorJugador(jugadores):
    """Esta funcion usa un diccionario-> diccionario-> lista para guardar las posiciones de las letras
    de la palabra que tiene que adivinar. hay que tener en cuenta que las letras se pueden repetir y se
    deben almacenar todas las posiciones"""

    diccionario={}

    for jugador in jugadores.keys():

        if jugador not in diccionario.keys():
            diccionario[jugador]={}

            palabraAAdivinar=jugadores[jugador][0]

        for idx,letra in enumerate(palabraAAdivinar):

            if letra not in diccionario[jugador].keys():
                diccionario[jugador][letra]=[]

            diccionario[jugador][letra].append(idx)

    return diccionario

def mostrar_posicion_marcar_letra(jugador,diccionarioJugador,letra):
    """Esta funcion muestra la posicion de la letra adivinada y las va eliminando del diccionario
    cuando no quedan mas letras en el diccionario es que se adivino la palabra"""

    if letra in diccionarioJugador[jugador].keys():
        string="la letra {0} se encuentra en las posiciones: ".format(letra)

        for posicion in diccionarioJugador[jugador][letra]:
            string+="{0} ".format(posicion)

        print(string)

        del diccionarioJugador[jugador][letra]

    else:
        if (len(diccionarioJugador[jugador]) == 0):
            return True
        else:
            print("ya habias elegido la letra {0} perdiste un intento".format(letra))
            return False

"""-------------------------------------------Fin de funciones-----------------------------------------------"""


"""
Estas estructuras de datos jugadores y turnos son las que espero me envie andy e ignacio de las ramas 2 y 4
se supone que los nombres no se repiten, yo agregaria esa verificacion en las primeras ramas cuando se cargan
los nombres.
Representan nombre,palabra a adivinar,aciertos,desaciertos,puntaje
Me respondieron de la catedra que los intentos no se deben tener encuenta"""

jugadores={'juan':['testing',0,0,0],'pedro':['escarapela',0,0,0]}
turnos=['pedro','juan']

"""Esta estructura acumula los valores cantidad de partidas,aciertos,desaciertos,puntaje General"""
acumulados={'juan':[0,0,0,0],'pedro':[0,0,0,0]}

diccionarioJugador={}
ganoEljugador=False
desaciertos=0

salir=False

while (salir != True):

    diccionarioJugador=letrasPorJugador(jugadores)

    while(len(turnos) != 0):

        for idx,jugador in enumerate(turnos):
            palabraAAdivinar=datos_jugador(jugador,jugadores)

            letra=input("Ingrese una letra:")

            if letra in palabraAAdivinar:
                ganoEljugador=mostrar_posicion_marcar_letra(jugador,diccionarioJugador,letra)

                if (ganoEljugador):
                    suma_puntos(jugador,jugadores,30)
                    turnos=[]
                    break

                suma_puntos(jugador,jugadores,1)
                suma_aciertos(jugador,jugadores)

            else:
                desaciertos=incrementar_desaciertos(jugador,jugadores)
                resta_puntos(jugador,jugadores)

            if (desaciertos==7):
                del turnos[idx]
                continue

    if(ganoEljugador):
        print("El jugador {0} gano la partida".format(jugador))
    else:
        print("Gano la maquina")

    for jugador in jugadores.keys():
         datos_jugador(jugador,jugadores)

    nuevaPartida=input("Quiere jugar una nueva partida?")

    if nuevaPartida in ["s","S","si","SI"]:
        acumula_valores(jugadores,acumulados)
        print(acumulados)
        print("juega nueva partida")
        """nueva_partida(jugadores,acumulados)"""

    else:
        print("gracias por volar con LOS Nocheros")
        salir=True


