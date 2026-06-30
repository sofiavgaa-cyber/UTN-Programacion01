# Contadores y acumuladores

contador_punto1 = 0

contador_condicion_punto2 = 0
contador_no_ia = 0

# Máximo masculino

mayor_edad_masculino = None
nombre_masculino_mayor = ""
tecnologia_masculino_mayor = ""

# Bucle principal (10 empleados)

contador = 0

while contador < 10:

    print(f"\nEMPLEADO {contador + 1}")

    # -------------------------
    # VALIDACIÓN NOMBRE
    # -------------------------

    nombre = input("Ingrese nombre: ")

    while nombre.isalpha() == False:
        print("Error. Ingrese solo letras.")
        nombre = input("Ingrese nombre: ")

    # -------------------------
    # VALIDACIÓN EDAD
    # -------------------------

    edad = int(input("Ingrese edad (18 o más): "))

    while edad < 18:
        print("Error. Debe ser mayor o igual a 18.")
        edad = int(input("Ingrese edad: "))

    # -------------------------
    # VALIDACIÓN GÉNERO
    # -------------------------

    genero = input(
        "Ingrese género (Masculino/Femenino/Otro): "
    ).lower()

    while (
        genero != "masculino"
        and genero != "femenino"
        and genero != "otro"
    ):
        print("Género inválido.")
        genero = input(
            "Ingrese género (Masculino/Femenino/Otro): "
        ).lower()

    # -------------------------
    # VALIDACIÓN TECNOLOGÍA
    # -------------------------

    tecnologia = input(
        "Ingrese tecnología (IA/RVRA/IOT): "
    ).upper()

    while (
        tecnologia != "IA"
        and tecnologia != "RVRA"
        and tecnologia != "IOT"
    ):
        print("Tecnología inválida.")
        tecnologia = input(
            "Ingrese tecnología (IA/RVRA/IOT): "
        ).upper()

    # =====================================================
    # PUNTO 1
    # Masculinos que votaron IOT o IA
    # Edad entre 25 y 50
    # =====================================================

    if (
        genero == "masculino"
        and (tecnologia == "IOT" or tecnologia == "IA")
        and edad >= 25
        and edad <= 50
    ):
        contador_punto1 += 1

    # =====================================================
    # PUNTO 2
    # % que NO votaron IA
    # género distinto de femenino
    # edad entre 33 y 40
    # =====================================================

    if (
        genero != "femenino"
        and edad >= 33
        and edad <= 40
    ):

        contador_condicion_punto2 += 1

        if tecnologia != "IA":
            contador_no_ia += 1

    # =====================================================
    # PUNTO 3
    # Masculino de mayor edad
    # =====================================================

    if genero == "masculino":

        if (
            mayor_edad_masculino is None
            or edad > mayor_edad_masculino
        ):
            mayor_edad_masculino = edad
            nombre_masculino_mayor = nombre
            tecnologia_masculino_mayor = tecnologia

    contador += 1

# =====================================================
# CÁLCULO DEL PORCENTAJE
# =====================================================

if contador_condicion_punto2 > 0:
    porcentaje_no_ia = (
        contador_no_ia * 100
        / contador_condicion_punto2
    )
else:
    porcentaje_no_ia = 0

# =====================================================
# INFORME FINAL
# =====================================================

print("\n========================")
print("RESULTADOS")
print("========================")

print(
    "1) Masculinos que votaron IA o IOT y tienen entre 25 y 50 años:",
    contador_punto1
)

print(
    "2) Porcentaje que NO votó IA:",
    porcentaje_no_ia,
    "%"
)

if mayor_edad_masculino is not None:
    print(
        "3) Masculino de mayor edad:",
        nombre_masculino_mayor
    )
    print(
        "   Tecnología elegida:",
        tecnologia_masculino_mayor
    )
else:
    print("3) No se ingresaron empleados masculinos.")