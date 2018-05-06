def datos_jugador(jugador,jugadores,resumen=False):
    """Esta funcion muestra los datos acumulados de los jugadores"""
    palabra=jugadores[jugador][0]
    aciertos=jugadores[jugador][1]
    desaciertos=jugadores[jugador][2]
    puntaje=jugadores[jugador][3]

    if (resumen):
        print("Las estadisticas del jugador {0} son: ".format(jugador))
        print("{0} aciertos, {1} desaciertos y un puntaje de {2}".format(aciertos,desaciertos,puntaje))
        print("\n")
    else:
        print("Es el turno del jugador {0}: ".format(jugador))
        print("{0} aciertos, {1} desaciertos y un puntaje de {2}".format(aciertos,desaciertos,puntaje))
        print("\n")
    return palabra

def incrementar_desaciertos(jugador,jugadores):
    """Esta funcion se utiliza para incrementar los desaciertos"""
    jugadores[jugador][2]+=1
    return jugadores[jugador][2]

def suma_aciertos(jugador,jugadores):
    """Esta funcion incrementa los aciertos"""
    jugadores[jugador][1]+=1

def resta_puntos(jugador,jugadores):
    """Esta funcion se utiliza para restar puntos a los jugadores"""
    puntaje=jugadores[jugador][3]

    if (puntaje >= 2):
        jugadores[jugador][3]-=2
    elif (puntaje == 1):
        jugadores[jugador][3]-=1

def suma_puntos(jugador,jugadores,puntos=1):
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


def mostrar_posicion_marcar_letra(idx,jugador,jugadores,diccionarioJugador,listaLetrasArriesgadas,listaLetrasAcertadas,letra):
    """Esta funcion muestra la posicion de la letra adivinada y las va eliminando del diccionario
    cuando no quedan mas letras en el diccionario es que se adivino la palabra"""

    for posicionLetra in diccionarioJugador[jugador][letra]:
        if letra not in listaLetrasAcertadas[idx]:
            listaLetrasAcertadas[idx][posicionLetra]=letra
            suma_aciertos(jugador,jugadores)
            suma_puntos(jugador,jugadores)

    if letra not in listaLetrasAcertadas[idx]:
        listaLetrasArriesgadas[idx].append(letra)

    print("Palabra a adivinar: {0}  lista de letras Fallidas: {1}".format(listaLetrasAcertadas[idx],listaLetrasArriesgadas[idx]))
    print("\n\n")

    if (listaLetrasAcertadas[idx].count("_")==0):
        return True

    return False

def mostrar_estado_actual(idx,listaLetrasAcertadas,listaLetrasArriesgadas):

    print("Palabra a adivinar: {0}  lista de letras Fallidas: {1}".format(listaLetrasAcertadas[idx],listaLetrasArriesgadas[idx]))

def init_listas(turnos,jugadores,listaLetrasArriesgadas,listaLetrasAcertadas):
    """Iniciliza las listas que muestra los aciertos y desaciertos de las letras ingresadas"""
    laux=[]
    for item in jugadores.keys():
        listaLetrasArriesgadas.append([])

    for turno in turnos:
        longitud_palabra=len(jugadores[turno][0])
        laux=[]
        for item in range(longitud_palabra):
            laux.append("_")

        listaLetrasAcertadas.append(laux)


"""-------------------------------------------Fin de funciones-----------------------------------------------"""

"""
Estas estructuras de datos jugadores y turnos son las que espero me envie andy e ignacio de las ramas 2 y 4
se supone que los nombres no se repiten, yo agregaria esa verificacion en las primeras ramas cuando se cargan
los nombres.
Representan nombre,palabra a adivinar,aciertos,desaciertos,puntaje
Me respondieron de la catedra que los intentos no se deben tener encuenta"""

jugadores={'juan':['abc',0,0,0],'pedro':['def',0,0,0]}
turnos=['pedro','juan']

"""Esta estructura acumula los valores cantidad de partidas,aciertos,desaciertos,puntaje General"""
acumulados={'juan':[0,0,0,0],'pedro':[0,0,0,0]}

salir=False

while (salir != True):

    diccionarioJugador={}
    listaLetrasArriesgadas=[]
    listaLetrasAcertadas=[]
    ganoEljugador=False
    desaciertos=0

    init_listas(turnos,jugadores,listaLetrasArriesgadas,listaLetrasAcertadas)

    diccionarioJugador=letrasPorJugador(jugadores)

    while(len(turnos) != 0):

        for idx,jugador in enumerate(turnos):
            palabraAAdivinar=datos_jugador(jugador,jugadores)
            mostrar_estado_actual(idx,listaLetrasAcertadas,listaLetrasArriesgadas)
            letra=input("Ingrese una letra:")

            while (len(letra) > 1 or not letra.isalpha()):
                letra=input("Ingrese una letra:")

            if letra in palabraAAdivinar:
                """Esta funcion ademas de insertar las letras en las posiciones incrementa los aciertos y el puntaje"""
                ganoEljugador=mostrar_posicion_marcar_letra(idx,jugador,jugadores,diccionarioJugador,listaLetrasArriesgadas,listaLetrasAcertadas,letra)

                if (ganoEljugador):
                    suma_puntos(jugador,jugadores,30)
                    turnos=[]
                    break
            else:
                print("La letra {0} no se encuentra en la palabra a adivinar".format(letra))
                print("\n")
                listaLetrasArriesgadas[idx].append(letra)
                desaciertos=incrementar_desaciertos(jugador,jugadores)
                resta_puntos(jugador,jugadores)

            if (desaciertos==7):
                del turnos[idx]
                del listaLetrasArriesgadas[idx]
                del listaLetrasAcertadas[idx]
                continue

    if(ganoEljugador):
        print("El jugador {0} gano la partida".format(jugador))
    else:
        print("Gano la maquina")

    for jugador in jugadores.keys():
         datos_jugador(jugador,jugadores,True)

    while True:
        nuevaPartida=input("Quiere jugar una nueva partida?\n")

        if nuevaPartida in ["s","S","si","SI"]:
            acumula_valores(jugadores,acumulados)
            print("aca se llama a nueva partida")
            break
        elif nuevaPartida in ["n","N","no","NO"]:
            print("gracias por volar con LOS Nocheros!!!!")
            salir=True
            break
        else:
            print("Ingrese una opcion valida(si/no)\n")



