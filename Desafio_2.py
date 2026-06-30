# ==========================================
# GESTIÓN DE RECAUDACIONES - EMPRESA DE COLECTIVOS
# ==========================================
#
# La empresa posee:
# - 3 líneas
# - 5 coches por línea
# - 15 choferes con legajos precargados
#
# Funcionalidades:
# 1. Cargar recaudación
# 2. Mostrar recaudación por coche y línea
# 3. Mostrar recaudación por línea
# 4. Mostrar recaudación por coche
# 5. Mostrar recaudación total
# 6. Salir
#
# ==========================================

# ---------------------------
# DATOS PRECARGADOS
# ---------------------------

# Matriz de recaudaciones
# Filas = Líneas
# Columnas = Coches
recaudaciones = [
    [0, 0, 0, 0, 0],  # Línea 1
    [0, 0, 0, 0, 0],  # Línea 2
    [0, 0, 0, 0, 0]   # Línea 3
]

# Legajos precargados
legajos = [
    1025, 1348, 1567, 1789, 2014,
    2235, 2456, 2678, 2891, 3012,
    3245, 3467, 3689, 3890, 4123
]


# ---------------------------
# FUNCIONES DE VALIDACIÓN
# ---------------------------

def validar_legajo(legajos):
    """
    Solicita un número de legajo y verifica
    que exista dentro de la lista de legajos.

    Retorna:
        int -> legajo válido
    """

    while True:
        legajo = int(input("Ingrese su número de legajo: "))

        if legajo in legajos:
            return legajo

        print("ERROR. El legajo no existe.")


def validar_linea():
    """
    Solicita una línea válida.

    Líneas disponibles:
    1, 2 y 3

    Retorna:
        int -> índice de línea (0 a 2)
    """

    while True:
        linea = int(input("Ingrese línea (1-3): "))

        if 1 <= linea <= 3:
            return linea - 1

        print("ERROR. Línea inválida.")


def validar_coche():
    """
    Solicita un coche válido.

    Coches disponibles:
    1 al 5

    Retorna:
        int -> índice de coche (0 a 4)
    """

    while True:
        coche = int(input("Ingrese coche (1-5): "))

        if 1 <= coche <= 5:
            return coche - 1

        print("ERROR. Coche inválido.")


def validar_recaudacion():
    """
    Solicita el monto de recaudación.

    No permite valores negativos.

    Retorna:
        float -> recaudación válida
    """

    while True:
        monto = float(input("Ingrese recaudación: $"))

        if monto >= 0:
            return monto

        print("ERROR. No se permiten valores negativos.")


# ---------------------------
# FUNCIONES PRINCIPALES
# ---------------------------

def cargar_recaudacion(recaudaciones, legajos):
    """
    Permite registrar una recaudación.

    Pasos:
    1. Validar legajo.
    2. Seleccionar línea.
    3. Seleccionar coche.
    4. Ingresar monto.
    5. Acumular la recaudación.
    """

    print("\n--- CARGA DE RECAUDACIÓN ---")

    validar_legajo(legajos)

    linea = validar_linea()
    coche = validar_coche()

    monto = validar_recaudacion()

    recaudaciones[linea][coche] += monto

    print("Recaudación registrada correctamente.")


def mostrar_recaudaciones(recaudaciones):
    """
    Muestra una matriz con la recaudación
    acumulada de cada coche por línea.
    """

    print("\n--- RECAUDACIÓN POR LÍNEA Y COCHE ---")

    print("\tC1\tC2\tC3\tC4\tC5")

    for i in range(len(recaudaciones)):
        print(f"L{i+1}", end="\t")

        for j in range(len(recaudaciones[i])):
            print(recaudaciones[i][j], end="\t")

        print()


def mostrar_recaudacion_lineas(recaudaciones):
    """
    Calcula y muestra la recaudación total
    de cada línea.
    """

    print("\n--- RECAUDACIÓN POR LÍNEA ---")

    for i in range(len(recaudaciones)):
        total_linea = sum(recaudaciones[i])

        print(f"Línea {i+1}: ${total_linea:.2f}")


def mostrar_recaudacion_coche(recaudaciones):
    """
    Permite seleccionar un coche y calcula
    cuánto recaudó considerando todas
    las líneas.
    """

    print("\n--- RECAUDACIÓN POR COCHE ---")

    coche = validar_coche()

    total_coche = 0

    for linea in range(len(recaudaciones)):
        total_coche += recaudaciones[linea][coche]

    print(f"Total recaudado por el coche {coche+1}: ${total_coche:.2f}")


def mostrar_recaudacion_total(recaudaciones):
    """
    Calcula y muestra la recaudación total
    general de la empresa.
    """

    total = 0

    for fila in recaudaciones:
        total += sum(fila)

    print("\n--- RECAUDACIÓN TOTAL ---")
    print(f"Total general: ${total:.2f}")


# ---------------------------
# MENÚ
# ---------------------------

def menu():
    """
    Muestra el menú principal y devuelve
    la opción elegida por el usuario.
    """

    print("\n==============================")
    print(" EMPRESA DE COLECTIVOS ")
    print("==============================")
    print("1. Cargar planilla de recaudación")
    print("2. Mostrar recaudación por coche y línea")
    print("3. Mostrar recaudación por línea")
    print("4. Mostrar recaudación por coche")
    print("5. Mostrar recaudación total")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    return opcion


# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------

while True:

    opcion = menu()

    match opcion:

        case 1:
            cargar_recaudacion(recaudaciones, legajos)

        case 2:
            mostrar_recaudaciones(recaudaciones)

        case 3:
            mostrar_recaudacion_lineas(recaudaciones)

        case 4:
            mostrar_recaudacion_coche(recaudaciones)

        case 5:
            mostrar_recaudacion_total(recaudaciones)

        case 6:
            print("Programa finalizado.")
            break

        case _:
            print("Opción inválida.")