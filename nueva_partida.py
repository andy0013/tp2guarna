import random

def ordenarPorPuntaje(acumulados):
    """ Esta funcion ordena por puntaje y a los jugadores que tienen igual puntaje los ordena aleatoriamente
    para los turnos de la partida. Realizada por Ignacio Liñeira Saavedra"""

    acumulados2 = []
    for key, value in acumulados.items():
        temp = [key,value[3]]
        acumulados2.append(temp)
        """The built-in sorted() function is guaranteed to be stable
        https://docs.python.org/3/library/functions.html#sorted"""
    random.shuffle(acumulados2)
    turnos = sorted(acumulados2, key = lambda x: x[1],reverse=True)
    return turnos

def nueva_partida(acumulados):
    """Esta funcion es llamada desde primeraronda para que imprima los acumulados y devuelva los nuevos turnos,
    para cada nueva partida. Realizada por Ignacio Liñeira Saavedra"""
    lista=ordenarPorPuntaje(acumulados)
    turnos=[]
    for jugador in lista:
        jugador=jugador[0]
        partidasTotal=acumulados[jugador][0]
        aciertosTotal=acumulados[jugador][1]
        desaciertosTotal=acumulados[jugador][2]
        puntajeTotal=acumulados[jugador][3]
        print("el jugador {0} tiene un puntaje Total de {1} tiene un Total de {2} partidas jugadas, un Total de {3} de aciertos y un Total de {4} desaciertos".format(jugador,puntajeTotal,partidasTotal,aciertosTotal,desaciertosTotal))
        turnos.append(jugador)
    return turnos
