# ============================================
# PARCIAL PROGRAMACIÓN I
# UTN FRA
# Autor: Sofia Candela Vega
# Fecha: 19-05
# ============================================

CANTIDAD_ESTUDIANTES = 30

# =====================================================
# VALIDACIONES
# =====================================================

def validar_legajo(legajo: str) -> bool:
    """
    Valida que el legajo sea numérico entero.
    """
    return legajo.isdigit()


def validar_nombre(nombre: str) -> bool:
    """
    Valida que el apellido y nombre contenga
    únicamente letras y espacios.
    """
    nombre = nombre.replace(" ", "")
    return nombre.isalpha()


def validar_genero(genero: str) -> bool:
    """
    Valida que el género sea F, M o X.
    """
    return genero.upper() in ["F", "M", "X"]


def validar_nota(nota: str) -> bool:
    """
    Valida que la nota sea un entero entre 1 y 10.
    """
    if nota.isdigit():
        nota = int(nota)
        return 1 <= nota <= 10

    return False


# =====================================================
# INGRESOS DE DATOS
# =====================================================

def pedir_legajo() -> int:
    """
    Solicita y valida un legajo.
    """
    while True:
        legajo = input("Ingrese legajo: ")

        if validar_legajo(legajo):
            return int(legajo)

        print("Error. Legajo inválido.")


def pedir_nombre() -> str:
    """
    Solicita y valida apellido y nombre.
    """
    while True:
        nombre = input("Ingrese apellido y nombre: ")

        if validar_nombre(nombre):
            return nombre.title()

        print("Error. Nombre inválido.")


def pedir_genero() -> str:
    """
    Solicita y valida género.
    """
    while True:
        genero = input("Ingrese género (F/M/X): ").upper()

        if validar_genero(genero):
            return genero

        print("Error. Género inválido.")


def pedir_nota(mensaje: str) -> int:
    """
    Solicita y valida una nota.
    """
    while True:
        nota = input(mensaje)

        if validar_nota(nota):
            return int(nota)

        print("Error. Nota inválida.")


# =====================================================
# MOSTRAR DATOS
# =====================================================

def mostrar_estudiante(indice: int,
                        lista_legajos: list,
                        lista_nombres: list,
                        lista_generos: list,
                        lista_parcial_1: list,
                        lista_parcial_2: list,
                        lista_promedios: list):
    """
    Muestra un estudiante.
    """

    print(
        f"{lista_legajos[indice]:<8}"
        f"{lista_nombres[indice]:<25}"
        f"{lista_generos[indice]:<5}"
        f"{lista_parcial_1[indice]:<8}"
        f"{lista_parcial_2[indice]:<8}"
        f"{lista_promedios[indice]:.2f}"
    )


def mostrar_todos(lista_legajos: list,
                  lista_nombres: list,
                  lista_generos: list,
                  lista_parcial_1: list,
                  lista_parcial_2: list,
                  lista_promedios: list):
    """
    Recorre todos los estudiantes y llama
    a mostrar_estudiante().
    """

    print("\nLEGAJO  NOMBRE                   GEN  P1      P2      PROM")
    print("-" * 65)

    for i in range(len(lista_legajos)):
        mostrar_estudiante(
            i,
            lista_legajos,
            lista_nombres,
            lista_generos,
            lista_parcial_1,
            lista_parcial_2,
            lista_promedios
        )


# =====================================================
# PROMEDIOS
# =====================================================

def calcular_promedio(nota_1: int, nota_2: int) -> float:
    """
    Calcula el promedio de dos notas.
    """
    return (nota_1 + nota_2) / 2


def generar_promedios(lista_parcial_1: list,
                      lista_parcial_2: list) -> list:
    """
    Genera la lista de promedios.
    """

    lista_promedios = []

    for i in range(len(lista_parcial_1)):
        promedio = calcular_promedio(
            lista_parcial_1[i],
            lista_parcial_2[i]
        )

        lista_promedios.append(promedio)

    return lista_promedios


# =====================================================
# ORDENAMIENTO
# =====================================================

def ordenar_estudiantes(lista_legajos: list,
                        lista_nombres: list,
                        lista_generos: list,
                        lista_parcial_1: list,
                        lista_parcial_2: list,
                        lista_promedios: list,
                        orden: str):
    """
    Ordena todas las listas paralelas según
    el promedio.

    orden = ASC o DESC
    """

    cantidad = len(lista_promedios)

    for i in range(cantidad - 1):

        for j in range(i + 1, cantidad):

            if (
                (orden == "ASC" and lista_promedios[i] > lista_promedios[j])
                or
                (orden == "DESC" and lista_promedios[i] < lista_promedios[j])
            ):

                lista_promedios[i], lista_promedios[j] = lista_promedios[j], lista_promedios[i]

                lista_legajos[i], lista_legajos[j] = lista_legajos[j], lista_legajos[i]

                lista_nombres[i], lista_nombres[j] = lista_nombres[j], lista_nombres[i]

                lista_generos[i], lista_generos[j] = lista_generos[j], lista_generos[i]

                lista_parcial_1[i], lista_parcial_1[j] = lista_parcial_1[j], lista_parcial_1[i]

                lista_parcial_2[i], lista_parcial_2[j] = lista_parcial_2[j], lista_parcial_2[i]


# =====================================================
# OPCIONES DEL MENÚ
# =====================================================

def cargar_datos(lista_legajos: list,
                 lista_nombres: list,
                 lista_generos: list,
                 lista_parcial_1: list,
                 lista_parcial_2: list):
    """
    Carga los datos de los estudiantes.
    """

    for i in range(CANTIDAD_ESTUDIANTES):

        print(f"\nESTUDIANTE {i+1}")

        lista_legajos.append(pedir_legajo())
        lista_nombres.append(pedir_nombre())
        lista_generos.append(pedir_genero())
        lista_parcial_1.append(pedir_nota("Primer parcial: "))
        lista_parcial_2.append(pedir_nota("Segundo parcial: "))

    print("\nCarga finalizada.")


def mostrar_mejores_promedios(lista_legajos: list,
                              lista_nombres: list,
                              lista_generos: list,
                              lista_parcial_1: list,
                              lista_parcial_2: list,
                              lista_promedios: list):
    """
    Muestra el/los estudiantes con mayor promedio.
    """

    mayor = max(lista_promedios)

    print(f"\nMayor promedio: {mayor:.2f}\n")

    for i in range(len(lista_promedios)):

        if lista_promedios[i] == mayor:

            mostrar_estudiante(
                i,
                lista_legajos,
                lista_nombres,
                lista_generos,
                lista_parcial_1,
                lista_parcial_2,
                lista_promedios
            )


def buscar_por_legajo(lista_legajos: list,
                      lista_nombres: list,
                      lista_generos: list,
                      lista_parcial_1: list,
                      lista_parcial_2: list,
                      lista_promedios: list):
    """
    Busca estudiante por legajo.
    """

    legajo_buscado = int(input("Ingrese legajo a buscar: "))

    encontrado = False

    for i in range(len(lista_legajos)):

        if lista_legajos[i] == legajo_buscado:

            mostrar_estudiante(
                i,
                lista_legajos,
                lista_nombres,
                lista_generos,
                lista_parcial_1,
                lista_parcial_2,
                lista_promedios
            )

            encontrado = True

    if not encontrado:
        print("Legajo inexistente.")


def mostrar_menu():
    """
    Muestra menú principal.
    """

    print("\n===== MENÚ =====")
    print("1- Cargar datos")
    print("2- Mostrar estudiantes")
    print("3- Calcular promedios")
    print("4- Mostrar ordenados por promedio DESC")
    print("5- Mostrar mayor promedio")
    print("6- Buscar por legajo")
    print("7- Salir")

    return int(input("Opción: "))


# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

lista_legajos = []
lista_nombres = []
lista_generos = []
lista_parcial_1 = []
lista_parcial_2 = []
lista_promedios = []

datos_cargados = False
promedios_generados = False

while True:

    opcion = mostrar_menu()

    match opcion:

        case 1:

            cargar_datos(
                lista_legajos,
                lista_nombres,
                lista_generos,
                lista_parcial_1,
                lista_parcial_2
            )

            datos_cargados = True

        case 2:

            if datos_cargados:

                if not promedios_generados:
                    lista_promedios = [0] * len(lista_legajos)

                mostrar_todos(
                    lista_legajos,
                    lista_nombres,
                    lista_generos,
                    lista_parcial_1,
                    lista_parcial_2,
                    lista_promedios
                )

            else:
                print("Debe cargar los datos primero.")

        case 3:

            if datos_cargados:

                lista_promedios = generar_promedios(
                    lista_parcial_1,
                    lista_parcial_2
                )

                promedios_generados = True

                print("Promedios calculados.")

            else:
                print("Debe cargar los datos primero.")

        case 4:

            if datos_cargados and promedios_generados:

                ordenar_estudiantes(
                    lista_legajos,
                    lista_nombres,
                    lista_generos,
                    lista_parcial_1,
                    lista_parcial_2,
                    lista_promedios,
                    "DESC"
                )

                mostrar_todos(
                    lista_legajos,
                    lista_nombres,
                    lista_generos,
                    lista_parcial_1,
                    lista_parcial_2,
                    lista_promedios
                )

            else:
                print("Debe cargar datos y calcular promedios.")

        case 5:

            if datos_cargados and promedios_generados:

                mostrar_mejores_promedios(
                    lista_legajos,
                    lista_nombres,
                    lista_generos,
                    lista_parcial_1,
                    lista_parcial_2,
                    lista_promedios
                )

            else:
                print("Debe cargar datos y calcular promedios.")

        case 6:

            if datos_cargados and promedios_generados:

                buscar_por_legajo(
                    lista_legajos,
                    lista_nombres,
                    lista_generos,
                    lista_parcial_1,
                    lista_parcial_2,
                    lista_promedios
                )

            else:
                print("Debe cargar datos y calcular promedios.")

        case 7:

            print("Fin del programa.")
            break

        case _:

            print("Opción inválida.")

