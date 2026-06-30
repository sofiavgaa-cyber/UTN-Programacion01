import random


# ---------------------------------------------------------
# INGRESO DE MATRIZ
# ---------------------------------------------------------
def cargar_matriz(n, m):
    matriz = []

    for i in range(n):
        fila = []
        for j in range(m):
            num = int(input(f"Ingrese valor [{i}][{j}]: "))
            fila.append(num)
        matriz.append(fila)

    return matriz


# ---------------------------------------------------------
# GENERAR MATRIZ ALEATORIA
# ---------------------------------------------------------
def generar_matriz(n, m):
    matriz = []

    for _ in range(n):
        fila = [random.randint(1, 50) for _ in range(m)]
        matriz.append(fila)

    return matriz


# ---------------------------------------------------------
# MOSTRAR MATRIZ
# ---------------------------------------------------------
def mostrar_matriz(matriz):
    print("\nMatriz:")
    for fila in matriz:
        print(fila)


# ---------------------------------------------------------
# DETECTAR SECUENCIAS DE PARES EN UNA FILA
# ---------------------------------------------------------
def secuencias_pares_fila(fila):
    secuencias = []
    actual = []

    for num in fila:
        if num % 2 == 0:
            actual.append(num)
        else:
            if len(actual) >= 2:
                secuencias.append(actual)
            actual = []

    # verificar última secuencia
    if len(actual) >= 2:
        secuencias.append(actual)

    return secuencias


# ---------------------------------------------------------
# ANALIZAR MATRIZ COMPLETA
# ---------------------------------------------------------
def analizar_matriz(matriz):
    todas_secuencias = []

    for fila in matriz:
        secuencias = secuencias_pares_fila(fila)
        todas_secuencias.extend(secuencias)

    return todas_secuencias


# ---------------------------------------------------------
# MOSTRAR RESULTADOS
# ---------------------------------------------------------
def mostrar_resultados(secuencias):
    if len(secuencias) == 0:
        print("\n❌ NO EXISTEN NÚMEROS CONSECUTIVOS PARES")
        return

    print("\n✅ EXISTEN NÚMEROS CONSECUTIVOS PARES")

    print(f"\n📊 Cantidad de secuencias: {len(secuencias)}")

    # secuencia más corta
    mas_corta = min(secuencias, key=len)

    # secuencia más larga
    mas_larga = max(secuencias, key=len)

    print(f"\n🔹 Secuencia más corta ({len(mas_corta)} elementos): {mas_corta}")
    print(f"🔹 Secuencia más larga ({len(mas_larga)} elementos): {mas_larga}")


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------
def main():

    print("=== DETECTOR DE SECUENCIAS DE PARES ===")

    n = int(input("Ingrese número de filas: "))
    m = int(input("Ingrese número de columnas: "))

    print("\n1 - Ingresar matriz manualmente")
    print("2 - Generar matriz aleatoria")

    opcion = input("Opción: ")

    if opcion == "1":
        matriz = cargar_matriz(n, m)
    else:
        matriz = generar_matriz(n, m)

    mostrar_matriz(matriz)

    secuencias = analizar_matriz(matriz)

    mostrar_resultados(secuencias)


# ---------------------------------------------------------
# EJECUCIÓN
# ---------------------------------------------------------
main()