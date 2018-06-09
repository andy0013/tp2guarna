import preparacion_juego
import nueva_partida
import configuracion

def datos_jugador(jugador,jugadores,resumen=False):
    """Esta funcion muestra los datos acumulados de los jugadores y genera un resumen para mostrar al final de la partida.
    Realizada por Pablo Arias."""

    palabra=jugadores[jugador][0]
    aciertos=jugadores[jugador][1]
    desaciertos=jugadores[jugador][2]
    puntaje=jugadores[jugador][3]

    if (resumen):
        print("Las estadisticas del jugador {0} son: ".format(jugador))
        print("Palabra a adivinar {0},{1} aciertos, {2} desaciertos y un puntaje de {3}".format(palabra,aciertos,desaciertos,puntaje))
        print("\n")
    else:
        print("Es el turno del jugador {0}: ".format(jugador))
        print("{0} aciertos, {1} desaciertos y un puntaje de {2}".format(aciertos,desaciertos,puntaje))
        print("\n")
    return palabra

def incrementar_desaciertos(jugador,jugadores,puntosDesacierto=1):
    """Esta funcion se utiliza para incrementar los desaciertos. realizada por Pablo Arias"""
    jugadores[jugador][2]+=puntosDesacierto
    return jugadores[jugador][2]

def suma_aciertos(jugador,jugadores):
    """Esta funcion incrementa los aciertos. realizada por Pablo Arias"""
    jugadores[jugador][1]+=1

def resta_puntos(jugador,jugadores):
    """Esta funcion se utiliza para restar puntos a los jugadores.Realizada por Pablo Arias."""
    puntaje=jugadores[jugador][3]

    if (puntaje >= 2):
        jugadores[jugador][3]-=2
    elif (puntaje == 1):
        jugadores[jugador][3]-=1

def suma_puntos(jugador,jugadores,puntos=1):
    """Esta funcion se utiliza para sumar puntos a los jugadores puede ser un punto o 30 se pasa por parametro
    Realizada por Pablo Arias."""
    jugadores[jugador][3]+=puntos

def acumula_valores(jugadores,acumulados):
    """esta funcion acumula en cada partida los valores de jugadores, para pasarlos al modulo nueva_partida para que imprima
    los valores.Realizado por Pablo Arias."""

    for jugador in jugadores:
        acumulados[jugador][0]+=1
        acumulados[jugador][1]+=jugadores[jugador][1]
        acumulados[jugador][2]+=jugadores[jugador][2]
        acumulados[jugador][3]+=jugadores[jugador][3]

def letras_por_jugador(jugadores):
    """Esta funcion usa un diccionario-> diccionario-> lista para guardar las posiciones de las letras
    de la palabra que tiene que adivinar. hay que tener en cuenta que las letras se pueden repetir y se
    deben almacenar todas las posiciones. Realizado por Pablo Arias"""

    diccionario={}

    for jugador in jugadores.keys():

        if jugador not in diccionario.keys():
            diccionario[jugador]={}

            palabra=jugadores[jugador][0]

        for idx,letra in enumerate(palabra):

            if letra not in diccionario[jugador].keys():
                diccionario[jugador][letra]=[]

            diccionario[jugador][letra].append(idx)

    return diccionario


def mostrar_posicion_marcar_letra(idx,jugador,jugadores,diccionarioJugador,listaLetrasArriesgadas,listaLetrasAcertadas,letra):
    """Esta funcion muestra la posicion de la letra adivinada o va acumulando los intentos fallidos.
    devuelve true cuando se adivino la palabra. Realizada por Pablo Arias."""

    for posicionLetra in diccionarioJugador[jugador][letra]:
        if letra not in listaLetrasAcertadas[idx]:
            suma_aciertos(jugador,jugadores)
            suma_puntos(jugador,jugadores,PUNTOS_ACIERTOS)
        listaLetrasAcertadas[idx][posicionLetra]=letra

    if letra not in listaLetrasAcertadas[idx]:
        listaLetrasArriesgadas[idx].append(letra)

    print("Palabra a adivinar: {0}  lista de letras Fallidas: {1}".format(listaLetrasAcertadas[idx],listaLetrasArriesgadas[idx]))
    print("\n\n")

    if (listaLetrasAcertadas[idx].count("_")==0):
        return True

    return False

def mostrar_estado_actual(idx,listaLetrasAcertadas,listaLetrasArriesgadas):
    """Muestra el estado actual de las letras adivinadas y letras fallidas. Realizado por Pablo Arias."""
    print("Palabra a adivinar: {0}  lista de letras Fallidas: {1}".format(listaLetrasAcertadas[idx],listaLetrasArriesgadas[idx]))

def init_listas(turnos,jugadores,listaLetrasArriesgadas,listaLetrasAcertadas):
    """Iniciliza las listas que muestra los aciertos y desaciertos de las letras ingresadas. Realizada por Pablo Arias"""

    for item in jugadores.keys():
        listaLetrasArriesgadas.append([])

    for turno in turnos:
        longitud_palabra=len(jugadores[turno][0])
        laux=[]
        for item in range(longitud_palabra):
            laux.append("_")

        listaLetrasAcertadas.append(laux)

def actualiza_jugadores(jugadores,turnos,acumulados):
    """Esta funcion actualiza la estructura de datos jugadores cuando se juegan mas de una partida. Realizdo por pablo Arias."""
    listaDePalabrasAAdivinar=preparacion_juego.generar_lista_de_palabras_a_adivinar(turnos)

    i=0
    for jugador in jugadores:
        jugadores[jugador][0]=listaDePalabrasAAdivinar[i]
        jugadores[jugador][1]=0
        jugadores[jugador][2]=0
        jugadores[jugador][3]=acumulados[jugador][3]
        i+=1

def archivardatos (archivo, nombreDeJugador, totalDeAciertos,  totalDeDesaciertos, puntajeTotal, palabras):
    return archivo.write(nombreDeJugador + "," + totalDeAciertos +","+ totalDeDesaciertos + "," + puntajeTotal + "," + palabras + "\n")

"""-------------------------------------------Fin de funciones-----------------------------------------------"""

"""Me respondieron de la catedra que los intentos no se deben tener encuenta"""

"""
estructuras de datos
Representan nombre,palabra a adivinar,aciertos,desaciertos,puntaje
jugadores={'juan':['abc',0,0,0],'pedro':['def',0,0,0]}

turnos=['pedro','juan']

Representan nombre,cantidad de partidas totales,aciertos totales,desaciertos totales,puntaje total
acumulados={'juan':[0,0,0,0],'pedro':[0,0,0,0]}
"""
MAX_DESACIERTOS=configuracion.diccionario_configuracion['MAX_DESACIERTOS']
PUNTOS_ACIERTOS=configuracion.diccionario_configuracion['PUNTOS_ACIERTOS']
PUNTOS_DESACIERTOS=configuracion.diccionario_configuracion['PUNTOS_DESACIERTOS']
PUNTOS_ADIVINA=configuracion.diccionario_configuracion['PUNTOS_ADIVINA']

salir=False

archivo11 = open('partida.csv', "w")
palabrasUsadas = {}

jugadores,turnos,acumulados=preparacion_juego.preparacion_juego()

while (salir != True):

    diccionarioJugador={}
    listaLetrasArriesgadas=[]
    listaLetrasAcertadas=[]
    ganoEljugador=False
    desaciertos=0

    init_listas(turnos,jugadores,listaLetrasArriesgadas,listaLetrasAcertadas)

    diccionarioJugador=letras_por_jugador(jugadores)

    while(len(turnos) != 0):

        for idx,jugador in enumerate(turnos):
            palabraAAdivinar=datos_jugador(jugador,jugadores)
            mostrar_estado_actual(idx,listaLetrasAcertadas,listaLetrasArriesgadas)

            letra=input("Ingrese una letra:")
            letra=letra.upper()
            while (len(letra) > 1 or not letra.isalpha()):
                letra=input("Ingrese una letra:")
                letra=letra.upper()

            if letra in palabraAAdivinar:
                """Esta funcion ademas de insertar las letras en las posiciones incrementa los aciertos y el puntaje"""
                ganoEljugador=mostrar_posicion_marcar_letra(idx,jugador,jugadores,diccionarioJugador,listaLetrasArriesgadas,listaLetrasAcertadas,letra)

                if (ganoEljugador):
                    suma_puntos(jugador,jugadores,PUNTOS_ADIVINA)
                    turnos=[]
                    break
            else:
                print("La letra {0} no se encuentra en la palabra a adivinar".format(letra))
                print("\n")
                listaLetrasArriesgadas[idx].append(letra)
                desaciertos=incrementar_desaciertos(jugador,jugadores,PUNTOS_DESACIERTOS)
                resta_puntos(jugador,jugadores)

            if (desaciertos==MAX_DESACIERTOS):
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

    for jugador in jugadores:
        if not jugador in palabrasUsadas:
            palabrasUsadas[jugador] = jugadores[jugador][0]
        else:
            palabrasUsadas[jugador] += (" " + jugadores[jugador][0])

    while True:
        nuevaPartida=input("Quiere jugar una nueva partida?\n")

        if nuevaPartida in ["s","S","si","SI"]:
            acumula_valores(jugadores,acumulados)
            turnos=nueva_partida.nueva_partida(acumulados)
            actualiza_jugadores(jugadores,turnos,acumulados)
            break
        elif nuevaPartida in ["n","N","no","NO"]:
            for jugador in jugadores:
                archivardatos(archivo11, jugador, str(jugadores[jugador][1]), str(jugadores[jugador][2]),
                              str(jugadores[jugador][3]), str(palabrasUsadas[jugador]))
            print("gracias por volar con LOS Nocheros!!!!")
            salir=True
            break
        else:
            print("Ingrese una opcion valida(si/no)\n")



