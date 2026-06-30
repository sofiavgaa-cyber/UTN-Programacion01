def es_alfabetica(cadena: str) -> bool:
    """
    Verifica si la cadena contiene solo letras (A-Z, a-z).
    """
    if len(cadena) == 0:
        return False

    for c in cadena:
        if not ((65 <= ord(c) <= 90) or (97 <= ord(c) <= 122)):
            return False

    return True

def es_entero(cadena: str) -> bool:
    """
    Verifica si la cadena es un entero válido (+/- opcional).
    """
    if len(cadena) == 0:
        return False

    i = 0

    if cadena[0] == '+' or cadena[0] == '-':
        if len(cadena) == 1:
            return False
        i = 1

    for j in range(i, len(cadena)):
        if not (48 <= ord(cadena[j]) <= 57):
            return False

    return True

def es_decimal(cadena: str) -> bool:
    """
    Verifica si la cadena es un número decimal válido.
    """
    if len(cadena) == 0:
        return False

    i = 0
    punto = False

    if cadena[0] == '+' or cadena[0] == '-':
        if len(cadena) == 1:
            return False
        i = 1

    for j in range(i, len(cadena)):
        c = cadena[j]

        if c == '.':
            if punto:
                return False
            punto = True
        else:
            if not (48 <= ord(c) <= 57):
                return False

    return True

def clave_segura(cadena: str) -> bool:
    """
    Valida contraseña con:
    - mayúscula
    - minúscula
    - número
    - mínimo 8 caracteres
    """
    if len(cadena) < 8:
        return False

    may = False
    min = False
    num = False

    for c in cadena:
        if 65 <= ord(c) <= 90:
            may = True
        elif 97 <= ord(c) <= 122:
            min = True
        elif 48 <= ord(c) <= 57:
            num = True

    return may and min and num

def es_palindromo(cadena: str) -> bool:
    """
    Verifica palíndromo ignorando mayúsculas.
    """
    i = 0
    j = len(cadena) - 1

    while i < j:
        c1 = cadena[i]
        c2 = cadena[j]

        # pasar a minúscula manualmente
        if 65 <= ord(c1) <= 90:
            c1 = chr(ord(c1) + 32)
        if 65 <= ord(c2) <= 90:
            c2 = chr(ord(c2) + 32)

        if c1 != c2:
            return False

        i += 1
        j -= 1

    return True

def validar_email(cadena: str) -> bool:
    """
    Valida formato de email básico.
    """
    arroba = 0
    pos_arroba = -1

    for i in range(len(cadena)):
        if cadena[i] == "@":
            arroba += 1
            pos_arroba = i

    if arroba != 1:
        return False

    if pos_arroba <= 0 or pos_arroba >= len(cadena) - 1:
        return False

    punto = False
    pos_punto = -1

    for i in range(pos_arroba + 1, len(cadena)):
        if cadena[i] == ".":
            punto = True
            pos_punto = i

    if not punto:
        return False

    if len(cadena) - pos_punto - 1 < 2:
        return False

    return True

def contar_vocales_consonantes(cadena: str):
    """
    Retorna (vocales, consonantes)
    """
    vocales = "aeiouAEIOU"
    v = 0
    c = 0

    for ch in cadena:
        if (65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122):
            if ch in vocales:
                v += 1
            else:
                c += 1

    return v, c

def validar_telefono(cadena: str) -> bool:
    """
    Valida número de teléfono de 10 dígitos.
    """
    if len(cadena) != 10:
        return False

    if cadena[0] == '0':
        return False

    for c in cadena:
        if not (48 <= ord(c) <= 57):
            return False

    return True