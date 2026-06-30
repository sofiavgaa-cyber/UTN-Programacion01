import json
import csv

# =========================
# VALIDACIONES
# =========================

def validar_legajo(valor):
    return isinstance(valor, int) and valor > 0


def validar_nombre(valor):
    return isinstance(valor, str) and valor.replace(" ", "").isalpha()


def validar_genero(valor):
    return valor in ["F", "M", "X"]


def validar_nota(valor):
    return isinstance(valor, int) and 1 <= valor <= 10


def validar_promedio(valor):
    return isinstance(valor, float) and 1.0 <= valor <= 10.0


# =========================
# CARGA / LECTURA
# =========================

def leer_json(ruta):
    with open(ruta, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["estudiantes"]


# =========================
# MOSTRAR
# =========================

def mostrar_estudiante(est):
    print(f"""
Legajo: {est['legajo']}
Nombre: {est['ape_nom']}
Género: {est['genero']}
Parcial 1: {est['pp']}
Parcial 2: {est['sp']}
Promedio: {est.get('prom', 'Sin calcular')}
""")


def mostrar_todos(lista):
    for est in lista:
        mostrar_estudiante(est)


# =========================
# PROMEDIO
# =========================

def calcular_promedio_estudiante(est):
    prom = (est["pp"] + est["sp"]) / 2
    return round(prom, 2)


def cargar_promedios(lista):
    for est in lista:
        est["prom"] = calcular_promedio_estudiante(est)


# =========================
# ORDENAMIENTO
# =========================

def ordenar_por_promedio(lista):
    return sorted(lista, key=lambda x: x["prom"], reverse=True)


# =========================
# BUSQUEDA
# =========================

def buscar_por_legajo(lista, legajo):
    for est in lista:
        if est["legajo"] == legajo:
            return est
    return None


# =========================
# EXPORTAR
# =========================

def exportar_json(lista, ruta):
    with open(ruta, "w", encoding="utf-8") as file:
        json.dump({"estudiantes": lista}, file, indent=4, ensure_ascii=False)


def exportar_csv(lista, ruta):
    campos = ["legajo", "ape_nom", "genero", "pp", "sp", "prom"]

    with open(ruta, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista)


import funciones as f

ARCHIVO_JSON = "data_sp.json"
ARCHIVO_JSON_SALIDA = "data_sp_out.json"
ARCHIVO_CSV = "data_sp.csv"

estudiantes = []
datos_cargados = False


def menu():
    print("""
======== MENU ========
1. Leer archivo JSON
2. Cargar datos manualmente (opcional)
3. Mostrar estudiantes
4. Calcular promedios
5. Ordenar por promedio (DESC)
6. Mejor promedio
7. Buscar por legajo
8. Exportar JSON
9. Exportar CSV
10. Salir
======================
""")


while True:
    menu()
    op = input("Ingrese opción: ")

    # 1 - Leer JSON
    if op == "1":
        estudiantes = f.leer_json(ARCHIVO_JSON)
        datos_cargados = True
        print("Datos cargados correctamente.")

    # 2 - Carga manual (opcional, básica)
    elif op == "2":
        estudiantes = []
        n = int(input("Cantidad de estudiantes: "))

        for _ in range(n):
            legajo = int(input("Legajo: "))
            nombre = input("Apellido y nombre: ")
            genero = input("Género (F/M/X): ")
            pp = int(input("Nota parcial 1: "))
            sp = int(input("Nota parcial 2: "))

            estudiantes.append({
                "legajo": legajo,
                "ape_nom": nombre,
                "genero": genero,
                "pp": pp,
                "sp": sp
            })

        datos_cargados = True

    # control de acceso
    elif op in ["3","4","5","6","7","8","9"] and not datos_cargados:
        print("Primero debe cargar los datos (opción 1).")
        continue

    # 3 - Mostrar
    elif op == "3":
        f.mostrar_todos(estudiantes)

    # 4 - Promedios
    elif op == "4":
        f.cargar_promedios(estudiantes)
        print("Promedios calculados.")

    # 5 - Ordenar
    elif op == "5":
        f.cargar_promedios(estudiantes)
        estudiantes = f.ordenar_por_promedio(estudiantes)
        f.mostrar_todos(estudiantes)

    # 6 - Mejor promedio
    elif op == "6":
        f.cargar_promedios(estudiantes)
        mejor = max(estudiantes, key=lambda x: x["prom"])
        f.mostrar_estudiante(mejor)

    # 7 - Buscar
    elif op == "7":
        leg = int(input("Ingrese legajo: "))
        est = f.buscar_por_legajo(estudiantes, leg)
        if est:
            f.mostrar_estudiante(est)
        else:
            print("No encontrado.")

    # 8 - Exportar JSON
    elif op == "8":
        f.exportar_json(estudiantes, ARCHIVO_JSON_SALIDA)
        print("Exportado a JSON.")

    # 9 - Exportar CSV
    elif op == "9":
        f.exportar_csv(estudiantes, ARCHIVO_CSV)
        print("Exportado a CSV.")

    # 10 - Salir
    elif op == "10":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")