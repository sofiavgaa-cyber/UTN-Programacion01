"""
Biblioteca de funciones para la gestión y procesamiento de estudiantes.
Desarrollada de acuerdo a los requerimientos de la institución educativa.
"""

import json
import csv

# ==========================================
# 1. FUNCIONES DE VALIDACIÓN (Nota 4)
# ==========================================

def validar_legajo(valor: str) -> int | None:
    """
    Valida que el legajo sea un número entero positivo.
    Retorna el entero si es válido, de lo contrario None.
    """
    try:
        num = int(valor)
        if num > 0:
            return num
    except ValueError:
        pass
    return None

def validar_ape_nom(valor: str) -> str | None:
    """
    Valida que el apellido y nombre contenga solo letras y espacios.
    Retorna la cadena limpia si es válida, de lo contrario None.
    """
    nombre = valor.strip()
    if not nombre:
        return None
    # Validar que cada fragmento de la cadena contenga caracteres alfabéticos
    partes = nombre.split()
    for parte in partes:
        if not parte.isalpha():
            return None
    return nombre

def validar_genero(valor: str) -> str | None:
    """
    Valida que el género ingresado pertenezca a ['F', 'M', 'X'].
    Retorna el carácter en mayúscula si es válido, de lo contrario None.
    """
    genero = valor.strip().upper()
    if genero in ['F', 'M', 'X']:
        return genero
    return None

def validar_nota(valor: str) -> int | None:
    """
    Valida que la nota del parcial sea un número entero entre 1 y 10.
    Retorna el entero si es válido, de lo contrario None.
    """
    try:
        nota = int(valor)
        if 1 <= nota <= 10:
            return nota
    except ValueError:
        pass
    return None


# ==========================================
# 2. FUNCIONES DE RECORRIDO Y MUESTRA (Nota 5)
# ==========================================

def mostrar_un_elemento(estudiante: dict) -> None:
    """Muestra los datos tabulados de un solo estudiante."""
    print(f"Legajo: {estudiante['legajo']:<6} | "
          f"Nombre: {estudiante['ape_nom']:<18} | "
          f"Género: {estudiante['genero']:<2} | "
          f"P1: {estudiante['pp']:<2} | "
          f"P2: {estudiante['sp']:<2} | "
          f"Promedio: {estudiante['prom']:.2f}")

def recorrer_y_mostrar_elementos(lista_estudiantes: list) -> None:
    """Recorre la lista completa llamando internamente a mostrar_un_elemento."""
    print("\n" + "="*85)
    print(f"{'LISTADO DE ESTUDIANTES':^85}")
    print("="*85)
    for estudiante in lista_estudiantes:
        mostrar_un_elemento(estudiante)
    print("="*85)


# ==========================================
# 3. FUNCIONES ASOCIADAS AL MENÚ DE OPCIONES
# ==========================================

def cargar_desde_json(nombre_archivo: str = "data_pp.json") -> list:
    """Ítem 1: Lee el archivo JSON inicial y genera la lista de diccionarios."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            lista_estudiantes = []
            for est in datos.get("estudiantes", []):
                estudiante = {
                    "legajo": int(est.get("legajo")),
                    "ape_nom": str(est.get("ape_nom")),
                    "genero": str(est.get("genero")),
                    "pp": int(est.get("pp")),
                    "sp": int(est.get("sp")),
                    "prom": float(est.get("prom", 0.0))
                }
                lista_estudiantes.append(estudiante)
            print(f"\n[ÉXITO] Se cargaron {len(lista_estudiantes)} estudiantes desde '{nombre_archivo}'.")
            return lista_estudiantes
    except FileNotFoundError:
        print(f"\n[ERROR] No se encontró el archivo '{nombre_archivo}'. Cree el archivo o use carga manual.")
        return []
    except json.JSONDecodeError:
        print(f"\n[ERROR] Formato inválido en '{nombre_archivo}'.")
        return []

def realizar_carga_manual(lista_estudiantes: list) -> None:
    """Ítem 2: Realiza la carga de datos solicitando y validando cada campo individualmente."""
    print("\n--- Alta Manual de Estudiante ---")
    
    # Validar Legajo (evitando duplicados)
    while True:
        legajo_in = input("Ingrese Legajo (entero positivo): ")
        legajo = validar_legajo(legajo_in)
        if legajo is not None:
            duplicado = False
            for est in lista_estudiantes:
                if est["legajo"] == legajo:
                    duplicado = True
                    break
            if duplicado:
                print("[ERROR] Este número de legajo ya se encuentra registrado.")
            else:
                break
        else:
            print("[ERROR] Legajo inválido. Intente nuevamente.")

    # Validar Apellido y Nombre
    while True:
        ape_nom_in = input("Ingrese Apellido y Nombre (solo letras): ")
        ape_nom = validar_ape_nom(ape_nom_in)
        if ape_nom is not None:
            break
        print("[ERROR] El nombre solo debe contener letras y espacios.")

    # Validar Género
    while True:
        genero_in = input("Ingrese Género (F / M / X): ")
        genero = validar_genero(genero_in)
        if genero is not None:
            break
        print("[ERROR] Opción incorrecta. Elija F, M o X.")

    # Validar Primer Parcial
    while True:
        pp_in = input("Ingrese Nota Primer Parcial (1-10): ")
        pp = validar_nota(pp_in)
        if pp is not None:
            break
        print("[ERROR] La nota debe ser un número entero entre 1 y 10.")

    # Validar Segundo Parcial
    while True:
        sp_in = input("Ingrese Nota Segundo Parcial (1-10): ")
        sp = validar_nota(sp_in)
        if sp is not None:
            break
        print("[ERROR] La nota debe ser un número entero entre 1 y 10.")

    # Estructura del nuevo diccionario con promedio inicializado en 0
    nuevo_estudiante = {
        "legajo": legajo,
        "ape_nom": ape_nom,
        "genero": genero,
        "pp": pp,
        "sp": sp,
        "prom": 0.0
    }
    lista_estudiantes.append(nuevo_estudiante)
    print(f"\n[ÉXITO] Estudiante '{ape_nom}' agregado correctamente a la lista de memoria.")

def calcular_y_guardar_promedios(lista_estudiantes: list) -> None:
    """Ítem 4: Calcula el promedio aritmético y lo actualiza en la clave 'prom'."""
    for estudiante in lista_estudiantes:
        promedio = (estudiante["pp"] + estudiante["sp"]) / 2.0
        estudiante["prom"] = round(promedio, 2)
    print("\n[ÉXITO] Promedios calculados correctamente para todos los estudiantes.")

def ordenar_por_promedio_desc(lista_estudiantes: list) -> None:
    """Ítem 5: Ordena una copia de los estudiantes por promedio DESC mediante algoritmo de intercambio."""
    lista_ordenada = list(lista_estudiantes)
    n = len(lista_ordenada)
    # Implementación de ordenamiento Bubble Sort descendente
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]["prom"] < lista_ordenada[j + 1]["prom"]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                
    print("\n--- Estudiantes Ordenados por Promedio (Descendente) ---")
    recorrer_y_mostrar_elementos(lista_ordenada)

def mostrar_maximo_promedio(lista_estudiantes: list) -> None:
    """Ítem 6: Encuentra y muestra el o los estudiantes que poseen el mayor promedio registrado."""
    if not lista_estudiantes:
        return

    # Buscar el valor máximo
    max_prom = lista_estudiantes[0]["prom"]
    for est in lista_estudiantes:
        if est["prom"] > max_prom:
            max_prom = est["prom"]

    # Filtrar aquellos que igualen el promedio máximo
    mejores = []
    for est in lista_estudiantes:
        if est["prom"] == max_prom:
            mejores.append(est)

    print(f"\n--- Estudiante(s) con Máximo Promedio ({max_prom:.2f}) ---")
    recorrer_y_mostrar_elementos(mejores)

def buscar_por_legajo(lista_estudiantes: list) -> None:
    """Ítem 7: Busca un estudiante específico por su clave primaria legajo."""
    legajo_in = input("\nIngrese el número de legajo a buscar: ")
    legajo_buscado = validar_legajo(legajo_in)
    
    if legajo_buscado is None:
        print("[ERROR] Formato de legajo incorrecto.")
        return

    estudiante_encontrado = None
    for est in lista_estudiantes:
        if est["legajo"] == legajo_buscado:
            estudiante_encontrado = est
            break

    if estudiante_encontrado:
        print("\n--- Coincidencia Encontrada ---")
        recorrer_y_mostrar_elementos([estudiante_encontrado])
    else:
        print(f"[INFO] No se encontró ningún estudiante con el legajo {legajo_buscado}.")

def exportar_a_json(lista_estudiantes: list, nombre_archivo: str = "data_sp.json") -> None:
    """Ítem 8: Guarda los datos de la lista actual en formato JSON."""
    estructura_salida = {"estudiantes": lista_estudiantes}
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(estructura_salida, archivo, indent=4, ensure_ascii=False)
        print(f"\n[ÉXITO] Archivo JSON generado de manera exitosa: '{nombre_archivo}'.")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo JSON: {e}")

def exportar_a_csv(lista_estudiantes: list, nombre_archivo: str = "data_sp.csv") -> None:
    """Ítem 9: Guarda los datos de la lista actual en un archivo plano CSV."""
    if not lista_estudiantes:
        print("[ERROR] La lista se encuentra vacía.")
        return
    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            campos = ["legajo", "ape_nom", "genero", "pp", "sp", "prom"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(lista_estudiantes)
        print(f"\n[ÉXITO] Archivo CSV generado de manera exitosa: '{nombre_archivo}'.")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo CSV: {e}")

        """
Programa Principal que implementa el Menú interactivo por Consola.
Controla el flujo operativo y valida el estado inicial de la carga de datos.
"""

import funciones

def desplegar_menu():
    """Muestra de forma visual las opciones del menú."""
    print("\n" + "="*50)
    print(f"{'SISTEMA DE GESTIÓN DE ALUMNOS':^50}")
    print("="*50)
    print("1  - Leer datos desde 'data_pp.json'")
    print("2  - Realizar carga manual de un estudiante")
    print("3  - Mostrar todos los estudiantes registrados")
    print("4  - Calcular el promedio de cada estudiante")
    print("5  - Mostrar estudiantes ordenados por promedio (DESC)")
    print("6  - Mostrar el/los estudiante/s con mayor promedio")
    print("7  - Buscar y mostrar un estudiante por Legajo")
    print("8  - Exportar lista con promedios a JSON ('data_sp.json')")
    print("9  - Exportar lista con promedios a CSV ('data_sp.csv')")
    print("10 - Salir del sistema")
    print("="*50)

def main():
    lista_estudiantes = []
    # Bandera de control de validación previa (Nota 0)
    datos_cargados = False

    while True:
        desplegar_menu()
        opcion = input("Seleccione una opción (1-10): ").strip()

        # Validación Nota 0: Impedir acceso a los ítems del 3 al 9 si no hay registros
        if opcion in ["3", "4", "5", "6", "7", "8", "9"] and not datos_cargados:
            print("\n[ALERTA] Acceso Denegado. Primero debe cargar alumnos utilizando la Opción 1 o la Opción 2.")
            continue

        if opcion == "1":
            lista_estudiantes = funciones.cargar_desde_json("data_pp.json")
            if lista_estudiantes:
                datos_cargados = True
        elif opcion == "2":
            funciones.realizar_carga_manual(lista_estudiantes)
            datos_cargados = True
        elif opcion == "3":
            funciones.recorrer_y_mostrar_elementos(lista_estudiantes)
        elif opcion == "4":
            funciones.calcular_y_guardar_promedios(lista_estudiantes)
        elif opcion == "5":
            funciones.ordenar_por_promedio_desc(lista_estudiantes)
        elif opcion == "6":
            funciones.mostrar_maximo_promedio(lista_estudiantes)
        elif opcion == "7":
            funciones.buscar_por_legajo(lista_estudiantes)
        elif opcion == "8":
            funciones.exportar_a_json(lista_estudiantes, "data_sp.json")
        elif opcion == "9":
            funciones.exportar_a_csv(lista_estudiantes, "data_sp.csv")
        elif opcion == "10":
            print("\nCierre de sesión finalizado correctamente. ¡Éxitos!")
            break
        else:
            print("\n[ERROR] Entrada incorrecta. Por favor ingrese un número del 1 al 10.")

if __name__ == "__main__":
    main()