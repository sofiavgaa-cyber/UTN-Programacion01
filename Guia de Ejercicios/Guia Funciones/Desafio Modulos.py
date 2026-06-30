#01
def validate_number(numero, minimo, maximo):
    """
    Valida si un número está dentro de un rango.
    Retorna True si es válido, False en caso contrario.
    """

    return minimo <= numero <= maximo


def validate_length(cadena, minimo, maximo):
    """
    Valida la longitud de una cadena.
    Retorna True si la longitud está dentro del rango.
    """

    longitud = len(cadena)

    return minimo <= longitud <= maximo


#02
from Validate import validate_number
from Validate import validate_length


def get_int(mensaje, mensaje_error, minimo, maximo, reintentos):

    while reintentos > 0:

        dato = input(mensaje)

        if dato.lstrip("-").isdigit():

            numero = int(dato)

            if validate_number(numero, minimo, maximo):
                return numero

        print(mensaje_error)
        reintentos -= 1

    return None


def get_float(mensaje, mensaje_error, minimo, maximo, reintentos):

    while reintentos > 0:

        dato = input(mensaje)

        try:
            numero = float(dato)

            if validate_number(numero, minimo, maximo):
                return numero

        except ValueError:
            pass

        print(mensaje_error)
        reintentos -= 1

    return None


def get_string(mensaje, mensaje_error, minimo, maximo, reintentos):

    while reintentos > 0:

        cadena = input(mensaje)

        if validate_length(cadena, minimo, maximo):
            return cadena

        print(mensaje_error)
        reintentos -= 1

    return None


#03
from Input import get_int
from Input import get_float
from Input import get_string


numero_entero = get_int(
    "Ingrese un entero entre 1 y 100: ",
    "Dato inválido.",
    1,
    100,
    3
)

print("Entero:", numero_entero)


numero_float = get_float(
    "Ingrese un decimal entre 0 y 10: ",
    "Dato inválido.",
    0,
    10,
    3
)

print("Float:", numero_float)


nombre = get_string(
    "Ingrese su nombre: ",
    "Longitud inválida.",
    3,
    20,
    3
)

print("Cadena:", nombre)