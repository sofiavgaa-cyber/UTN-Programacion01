def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    """
    Solicita y valida un número entero.

    Parámetros:
    mensaje: Mensaje a mostrar.
    mensaje_error: Mensaje de error.
    minimo: Valor mínimo permitido.
    maximo: Valor máximo permitido.
    reintentos: Cantidad de intentos.

    Retorna:
    El número validado o None si se agotaron los intentos.
    """

    while reintentos > 0:

        dato = input(mensaje)

        if dato.isdigit():

            numero = int(dato)

            if minimo <= numero <= maximo:
                return numero

        reintentos -= 1
        print(mensaje_error)

    return None


from Input import get_int
import random


def mostrar_elemento(eleccion:int) -> str:
    """
    Convierte una elección numérica en texto.

    Parámetro:
    eleccion: Número de elección.

    Retorna:
    Piedra, Papel o Tijera.
    """

    match eleccion:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"


def verificar_ganador_ronda(jugador:int, maquina:int) -> str:
    """
    Determina el ganador de una ronda.

    Parámetros:
    jugador: Elección del jugador.
    maquina: Elección de la máquina.

    Retorna:
    Jugador, Máquina o Empate.
    """

    if jugador == maquina:
        return "Empate"

    if (
        (jugador == 1 and maquina == 3)
        or (jugador == 2 and maquina == 1)
        or (jugador == 3 and maquina == 2)
    ):
        return "Jugador"

    return "Máquina"


def verificar_estado_partida(aciertos_jugador:int,
                             aciertos_maquina:int,
                             ronda_actual:int,
                             seguidas_jugador:int,
                             seguidas_maquina:int) -> bool:
    """
    Determina si la partida continúa.

    Retorna:
    True si sigue.
    False si termina.
    """

    # Dos victorias seguidas
    if seguidas_jugador == 2 or seguidas_maquina == 2:
        return False

    # Mejor de tres
    if ronda_actual >= 3 and aciertos_jugador != aciertos_maquina:
        return False

    return True


def verificar_ganador_partida(aciertos_jugador:int,
                              aciertos_maquina:int) -> str:
    """
    Determina el ganador final de la partida.

    Retorna:
    Jugador o Máquina.
    """

    if aciertos_jugador > aciertos_maquina:
        return "Jugador"

    return "Máquina"


def jugar_piedra_papel_tijera() -> str:
    """
    Ejecuta una partida completa.

    Retorna:
    Jugador o Máquina.
    """

    ronda = 0
    aciertos_jugador = 0
    aciertos_maquina = 0

    seguidas_jugador = 0
    seguidas_maquina = 0

    continuar = True

    print("\n=== PIEDRA PAPEL O TIJERA ===\n")

    while continuar:

        ronda += 1

        print(f"\n----- RONDA {ronda} -----")

        jugador = get_int(
            "1-Piedra | 2-Papel | 3-Tijera: ",
            "Error. Debe ingresar 1, 2 o 3.",
            1,
            3,
            3
        )

        if jugador is None:
            print("Se agotaron los intentos.")
            return "Máquina"

        maquina = random.randint(1, 3)

        print(f"Jugador eligió: {mostrar_elemento(jugador)}")
        print(f"Máquina eligió: {mostrar_elemento(maquina)}")

        ganador_ronda = verificar_ganador_ronda(
            jugador,
            maquina
        )

        print(f"Resultado: {ganador_ronda}")

        if ganador_ronda == "Jugador":

            aciertos_jugador += 1
            seguidas_jugador += 1
            seguidas_maquina = 0

        elif ganador_ronda == "Máquina":

            aciertos_maquina += 1
            seguidas_maquina += 1
            seguidas_jugador = 0

        else:

            seguidas_jugador = 0
            seguidas_maquina = 0

        print(
            f"Marcador -> Jugador: {aciertos_jugador} | "
            f"Máquina: {aciertos_maquina}"
        )

        continuar = verificar_estado_partida(
            aciertos_jugador,
            aciertos_maquina,
            ronda,
            seguidas_jugador,
            seguidas_maquina
        )

    ganador = verificar_ganador_partida(
        aciertos_jugador,
        aciertos_maquina
    )

    return ganador


# -------------------
# PROGRAMA PRINCIPAL
# -------------------

ganador = jugar_piedra_papel_tijera()

print("\n======================")
print(f"GANADOR FINAL: {ganador}")
print("======================")


