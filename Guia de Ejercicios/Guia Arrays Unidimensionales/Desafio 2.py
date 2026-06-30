# --------------------------------------------------
# FUNCIONES
# --------------------------------------------------

def productos_en_comun(usuario1:list, usuario2:list) -> list:
    """
    Retorna los productos comprados por ambos usuarios.
    """
    comunes = []

    for producto in usuario1:
        if producto in usuario2 and producto not in comunes:
            comunes.append(producto)

    return comunes


def productos_exclusivos(usuario1:list, usuario2:list) -> list:
    """
    Retorna los productos que están en usuario1
    pero no en usuario2.
    """
    exclusivos = []

    for producto in usuario1:
        if producto not in usuario2:
            exclusivos.append(producto)

    return exclusivos


def catalogo_total(usuario1:list, usuario2:list) -> list:
    """
    Retorna la unión de ambas listas sin repetir elementos.
    """
    catalogo = usuario1.copy()

    for producto in usuario2:
        if producto not in catalogo:
            catalogo.append(producto)

    return catalogo


def recomendar_productos(usuario1:list, usuario2:list):
    """
    Genera recomendaciones para ambos usuarios.
    """
    recomendaciones_u1 = productos_exclusivos(usuario2, usuario1)
    recomendaciones_u2 = productos_exclusivos(usuario1, usuario2)

    return recomendaciones_u1, recomendaciones_u2


def mostrar_lista(titulo:str, lista:list):
    """
    Muestra una lista con formato.
    """
    print(f"\n{titulo}")

    if len(lista) == 0:
        print("No hay elementos.")
    else:
        for elemento in lista:
            print(f"- {elemento}")


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

usuario_1 = [
    "Notebook",
    "Mouse",
    "Teclado",
    "Auriculares",
    "Monitor"
]

usuario_2 = [
    "Monitor",
    "Impresora",
    "Mouse",
    "Webcam",
    "Parlantes"
]

comunes = productos_en_comun(usuario_1, usuario_2)

exclusivos_u1 = productos_exclusivos(
    usuario_1,
    usuario_2
)

exclusivos_u2 = productos_exclusivos(
    usuario_2,
    usuario_1
)

catalogo = catalogo_total(
    usuario_1,
    usuario_2
)

recomendacion_u1, recomendacion_u2 = (
    recomendar_productos(usuario_1, usuario_2)
)

# --------------------------------------------------
# SALIDAS
# --------------------------------------------------

mostrar_lista(
    "PRODUCTOS EN COMÚN",
    comunes
)

mostrar_lista(
    "PRODUCTOS EXCLUSIVOS DEL USUARIO 1",
    exclusivos_u1
)

mostrar_lista(
    "PRODUCTOS EXCLUSIVOS DEL USUARIO 2",
    exclusivos_u2
)

mostrar_lista(
    "CATÁLOGO TOTAL",
    catalogo
)

mostrar_lista(
    "RECOMENDACIONES PARA USUARIO 1",
    recomendacion_u1
)

mostrar_lista(
    "RECOMENDACIONES PARA USUARIO 2",
    recomendacion_u2
)