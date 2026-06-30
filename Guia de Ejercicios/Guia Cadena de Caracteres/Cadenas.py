#01
def contar_vocales(cadena: str):
    """
    Cuenta la cantidad de cada vocal en una cadena.
    Retorna una lista de listas: [vocal, cantidad]
    """
    vocales = ["a", "e", "i", "o", "u"]
    resultado = [[v, 0] for v in vocales]

    cadena = cadena.lower()

    for c in cadena:
        for i in range(len(vocales)):
            if c == vocales[i]:
                resultado[i][1] += 1

    return resultado


# Ejemplo
print(contar_vocales("murcielaguito"))


#02
def primera_ocurrencia(cadena: str, caracter: str) -> int:
    """
    Devuelve el índice de la primera aparición del caracter.
    Si no está, devuelve -1.
    """
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1


# Ejemplo
print(primera_ocurrencia("hola mundo", "m"))


#03
def es_palindromo(cadena: str) -> bool:
    """
    Retorna True si la cadena es palíndromo, False en caso contrario.
    """
    cadena = cadena.lower()
    return cadena == cadena[::-1]


# Ejemplo
print(es_palindromo("neuquen"))  # True


#04
def eliminar_repetidos_consecutivos(cadena: str) -> str:
    """
    Elimina caracteres repetidos consecutivos.
    Ej: "Hooola" -> "Hola"
    """
    if len(cadena) == 0:
        return ""

    resultado = cadena[0]

    for i in range(1, len(cadena)):
        if cadena[i] != cadena[i - 1]:
            resultado += cadena[i]

    return resultado


# Ejemplo
print(eliminar_repetidos_consecutivos("Hooola"))


#05
def eliminar_vocales(cadena: str) -> str:
    """
    Elimina todas las vocales de una cadena.
    """
    vocales = "aeiouAEIOU"
    resultado = ""

    for c in cadena:
        if c not in vocales:
            resultado += c

    return resultado


# Ejemplo
print(eliminar_vocales("Hola"))


#06
def contar_subcadena(cadena: str, subcadena: str) -> int:
    """
    Cuenta cuántas veces aparece una subcadena dentro de una cadena.
    """
    contador = 0
    n = len(subcadena)

    for i in range(len(cadena) - n + 1):
        if cadena[i:i+n] == subcadena:
            contador += 1

    return contador


# Ejemplo
print(contar_subcadena("El pan del panadero", "pan"))