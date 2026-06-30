import random


# ---------------------------------------------------------
# GENERAR LEGAJOS
# ---------------------------------------------------------
def generar_legajos(cantidad):
    legajos = set()

    while len(legajos) < cantidad:
        legajos.add(random.randint(1000, 9999))

    return list(legajos)


# ---------------------------------------------------------
# MOSTRAR MATRIZ
# ---------------------------------------------------------
def mostrar_matriz(matriz):
    print("\nRecaudación (líneas x coches):\n")

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:10.2f}", end="")
        print()


# ---------------------------------------------------------
# VALIDAR LEGAJO
# ---------------------------------------------------------
def validar_legajo(legajo, legajos):
    return legajo in legajos


# ---------------------------------------------------------
# VALIDAR OPCIÓN ENTERA
# ---------------------------------------------------------
def validar_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print("❌ Fuera de rango.")
        except:
            print("❌ Ingreso inválido.")


# ---------------------------------------------------------
# VALIDAR RECAUDACIÓN
# ---------------------------------------------------------
def validar_recaudacion():
    while True:
        try:
            valor = float(input("Ingrese recaudación: "))
            if valor >= 0:
                return valor
            else:
                print("❌ No se permiten valores negativos.")
        except:
            print("❌ Valor inválido.")


# ---------------------------------------------------------
# CARGAR RECAUDACIÓN
# ---------------------------------------------------------
def cargar_recaudacion(matriz, legajos, acumulado_por_chofer):
    legajo = int(input("Ingrese su legajo: "))

    if not validar_legajo(legajo, legajos):
        print("❌ Legajo inexistente.")
        return

    linea = validar_entero("Ingrese línea (0-2): ", 0, 2)
    coche = validar_entero("Ingrese coche (0-4): ", 0, 4)
    monto = validar_recaudacion()

    matriz[linea][coche] += monto

    # acumulado por chofer (opcional)
    acumulado_por_chofer[legajo] = acumulado_por_chofer.get(legajo, 0) + monto

    print("✅ Recaudación registrada correctamente.")


# ---------------------------------------------------------
# RECAUDACIÓN POR LÍNEA
# ---------------------------------------------------------
def recaudacion_por_linea(matriz):
    print("\n📊 Recaudación por línea:")

    for i in range(len(matriz)):
        total = sum(matriz[i])
        print(f"Línea {i}: ${total:.2f}")


# ---------------------------------------------------------
# RECAUDACIÓN POR COCHES
# ---------------------------------------------------------
def recaudacion_por_coche(matriz):
    coche = validar_entero("Seleccione coche (0-4): ", 0, 4)

    total = 0
    for i in range(len(matriz)):
        total += matriz[i][coche]

    print(f"\n🚍 Recaudación total del coche {coche}: ${total:.2f}")


# ---------------------------------------------------------
# TOTAL GENERAL
# ---------------------------------------------------------
def recaudacion_total(matriz):
    total = 0
    for fila in matriz:
        total += sum(fila)

    print(f"\n💰 Recaudación total general: ${total:.2f}")


# ---------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------
def main():

    lineas = 3
    coches = 5

    matriz_recaudacion = [[0 for _ in range(coches)] for _ in range(lineas)]

    legajos = generar_legajos(15)
    acumulado_por_chofer = {}

    print("=== SISTEMA DE RECAUDACIÓN DE COLECTIVOS ===")
    print("\nLegajos generados:")
    print(legajos)

    while True:
        print("\n1 - Cargar recaudación")
        print("2 - Mostrar matriz de recaudación")
        print("3 - Recaudación por línea")
        print("4 - Recaudación por coche")
        print("5 - Recaudación total")
        print("6 - Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            cargar_recaudacion(matriz_recaudacion, legajos, acumulado_por_chofer)

        elif opcion == "2":
            mostrar_matriz(matriz_recaudacion)

        elif opcion == "3":
            recaudacion_por_linea(matriz_recaudacion)

        elif opcion == "4":
            recaudacion_por_coche(matriz_recaudacion)

        elif opcion == "5":
            recaudacion_total(matriz_recaudacion)

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


# ---------------------------------------------------------
# EJECUCIÓN
# ---------------------------------------------------------
main()