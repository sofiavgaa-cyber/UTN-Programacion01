# Ingreso de datos
estacion = input("Ingrese la estación del año: ").lower()
destino = input("Ingrese el destino: ").lower()

# Evaluación con match
match estacion:
    case "invierno":
        if destino == "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")

    case "verano":
        if destino == "mar del plata" or destino == "cataratas":
            print("Se viaja")
        else:
            print("No se viaja")

    case "otoño":
        print("Se viaja")

    case "primavera":
        if destino != "bariloche":
            print("Se viaja")
        else:
            print("No se viaja")

    case _:
        print("Estación inválida")