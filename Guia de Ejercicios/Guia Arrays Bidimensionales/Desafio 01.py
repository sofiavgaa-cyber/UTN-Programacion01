from random import sample


# --------------------------------------------------------
# Función: mostrar_matriz
# Descripción: Muestra la matriz de forma ordenada.
# Parámetros:
#   matriz -> matriz a mostrar
# Retorna:
#   Nada
# --------------------------------------------------------
def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:4}", end="")
        print()


# --------------------------------------------------------
# Función: calcular_constante_magica
# Descripción: Calcula la constante mágica para una
#              matriz de orden n.
# Parámetros:
#   n -> tamaño de la matriz
# Retorna:
#   Constante mágica
# --------------------------------------------------------
def calcular_constante_magica(n):
    return n * ((n ** 2) + 1) // 2


# --------------------------------------------------------
# Función: verificar_cuadrado_magico
# Descripción: Verifica si una matriz es un cuadrado mágico.
# Parámetros:
#   matriz -> matriz a analizar
# Retorna:
#   True si es mágico, False caso contrario
# --------------------------------------------------------
def verificar_cuadrado_magico(matriz):

    n = len(matriz)
    constante = calcular_constante_magica(n)

    # Verificar filas
    for fila in matriz:
        if sum(fila) != constante:
            return False

    # Verificar columnas
    for columna in range(n):
        suma_columna = 0

        for fila in range(n):
            suma_columna += matriz[fila][columna]

        if suma_columna != constante:
            return False

    # Diagonal principal
    suma_diag_principal = 0

    for i in range(n):
        suma_diag_principal += matriz[i][i]

    if suma_diag_principal != constante:
        return False

    # Diagonal secundaria
    suma_diag_secundaria = 0

    for i in range(n):
        suma_diag_secundaria += matriz[i][n - 1 - i]

    if suma_diag_secundaria != constante:
        return False

    return True


# --------------------------------------------------------
# Función: cargar_matriz
# Descripción: Permite ingresar una matriz validando:
#              - Valores entre 1 y n²
#              - Sin repetidos
# Parámetros:
#   n -> tamaño de la matriz
# Retorna:
#   Matriz cargada
# --------------------------------------------------------
def cargar_matriz(n):

    matriz = []
    numeros_usados = []

    for fila in range(n):

        fila_actual = []

        for columna in range(n):

            while True:

                numero = int(input(
                    f"Ingrese valor [{fila}][{columna}] "
                    f"(1 a {n**2}): "
                ))

                if numero < 1 or numero > n ** 2:
                    print("Error. Número fuera de rango.")
                elif numero in numeros_usados:
                    print("Error. El número ya fue ingresado.")
                else:
                    numeros_usados.append(numero)
                    fila_actual.append(numero)
                    break

        matriz.append(fila_actual)

    return matriz


# --------------------------------------------------------
# Función: generar_matriz_aleatoria
# Descripción: Genera una matriz aleatoria con valores
#              del 1 al n² sin repetir.
# Parámetros:
#   n -> tamaño de la matriz
# Retorna:
#   Matriz aleatoria
# --------------------------------------------------------
def generar_matriz_aleatoria(n):

    numeros = sample(range(1, n ** 2 + 1), n ** 2)

    matriz = []
    indice = 0

    for i in range(n):

        fila = []

        for j in range(n):
            fila.append(numeros[indice])
            indice += 1

        matriz.append(fila)

    return matriz


# --------------------------------------------------------
# Programa Principal
# --------------------------------------------------------

print("=== VERIFICADOR DE CUADRADO MÁGICO ===")

while True:
    n = int(input("Ingrese el orden de la matriz (n >= 3): "))

    if n >= 3:
        break

    print("Error. El tamaño mínimo es 3.")

print("\n1 - Ingresar matriz manualmente")
print("2 - Generar matriz aleatoria")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    matriz = cargar_matriz(n)
else:
    matriz = generar_matriz_aleatoria(n)

print("\nMATRIZ INGRESADA:")
mostrar_matriz(matriz)

constante = calcular_constante_magica(n)

print(f"\nConstante mágica esperada: {constante}")

if verificar_cuadrado_magico(matriz):
    print("\n✅ La matriz ES un cuadrado mágico.")
else:
    print("\n❌ La matriz NO es un cuadrado mágico.")