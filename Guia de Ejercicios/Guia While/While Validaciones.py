#01
clave_correcta = "python123"

clave = input("Ingrese la clave: ")

while clave != clave_correcta:
    print("Clave incorrecta.")
    clave = input("Ingrese la clave nuevamente: ")

print("Acceso permitido.")


#02
clave_correcta = "python123"

intentos = 0

while intentos < 3:
    clave = input("Ingrese la clave: ")

    if clave == clave_correcta:
        print("Acceso permitido.")
        break

    intentos += 1

    if intentos < 3:
        print("Clave incorrecta. Intentos restantes:", 3 - intentos)

if intentos == 3 and clave != clave_correcta:
    print("Acceso denegado.")


#03
nota = int(input("Ingrese una nota (1-10): "))

while nota < 1 or nota > 10:
    print("Error. La nota debe estar entre 1 y 10.")
    nota = int(input("Ingrese una nota (1-10): "))

print("Nota válida:", nota)


#04
color = input("Ingrese un color: ").lower()

while color != "rojo" and color != "verde" and color != "azul":
    print("Color inválido.")
    color = input("Ingrese Rojo, Verde o Azul: ").lower()

print("Color válido:", color)


#Integrador Validaciones
# APELLIDO

apellido = input("Ingrese apellido: ")

while apellido.isalpha() == False:
    print("Error. Debe contener solo letras.")
    apellido = input("Ingrese apellido: ")

# EDAD

edad = int(input("Ingrese edad (18 a 90): "))

while edad < 18 or edad > 90:
    print("Edad inválida.")
    edad = int(input("Ingrese edad (18 a 90): "))

# ESTADO CIVIL

estado_civil = input(
    "Ingrese estado civil (soltero, casado, divorciado, viudo): "
).lower()

while (
    estado_civil != "soltero"
    and estado_civil != "casado"
    and estado_civil != "divorciado"
    and estado_civil != "viudo"
):
    print("Estado civil inválido.")
    estado_civil = input(
        "Ingrese estado civil (soltero, casado, divorciado, viudo): "
    ).lower()

# LEGAJO

legajo = int(input("Ingrese número de legajo (1000-9999): "))

while legajo < 1000 or legajo > 9999:
    print("Legajo inválido.")
    legajo = int(input("Ingrese número de legajo (1000-9999): "))

# MOSTRAR DATOS

print("\nDATOS INGRESADOS")
print("Apellido:", apellido)
print("Edad:", edad)
print("Estado civil:", estado_civil)
print("Legajo:", legajo)

