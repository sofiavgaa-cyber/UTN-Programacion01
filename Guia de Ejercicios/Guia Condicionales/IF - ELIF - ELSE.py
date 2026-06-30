#01
# Ingreso de la altura del jugador en centímetros
altura = int(input("Ingrese la altura del jugador (cm): "))

# Determinación de la posición
if altura < 160:
    posicion = "Base"
elif altura <= 179:
    posicion = "Escolta"
elif altura <= 199:
    posicion = "Alero"
else:
    posicion = "Ala-Pívot o Pívot"

# Mostrar resultado
print(f"La posición del jugador es: {posicion}")


#02
import random

# Generar una nota aleatoria entre 1 y 10 inclusive
nota = random.randint(1, 10)

# Evaluar la nota
if nota >= 6:
    print(f"Promoción directa, la nota es {nota}")
elif nota >= 4:
    print(f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es {nota}")

