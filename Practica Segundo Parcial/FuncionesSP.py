"""
Módulo de funciones para la gestión y procesamiento de datos de estudiantes.
Cumple con los requerimientos del parcial de programación.
"""
import json
import csv

# ==========================================
# 1. FUNCIONES DE VALIDACIÓN (Nota 4)
# ==========================================

def validar_legajo(valor: str) -> int | None:
    """Valida que el legajo sea un número entero positivo."""
    try:
        legajo = int(valor)
        if legajo > 0:
            return legajo
    except ValueError:
        pass
    return None

def validar_ape_nom(valor: str) -> str | None:
    """Valida que el apellido y nombre sea alfabético (permite espacios)."""
    # Quitamos espacios para verificar si el resto son solo letras
    if valor.strip() and valor.replace(" ", "").isalpha():
        return valor.strip()
    return None

def validar_genero(valor: str) -> str | None:
    """Valida que el género sea 'F', 'M' o 'X'."""
    genero = valor.strip().upper()
    if genero in ['F', 'M', 'X']:
        return genero
    return None

def validar_nota(valor: str) -> int | None:
    """Valida que la nota sea un número entero entre 1 y 10."""
    try:
        nota = int(valor)
        if 1 <= nota <= 10:
            return nota
    except ValueError:
        pass
    return None


# ==========================================
# 2. FUNCIONES DEL MENÚ (Notas 2 y 5)
# ==========================================

def opcion_1_leer_json(nombre_archivo: str = "data_pp.json") -> list:
    """Lee el archivo JSON inicial y devuelve la lista de estudiantes."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print(f"\n[ÉXITO] Archivo '{nombre_archivo}' cargado correctamente.")
            return datos.get("estudiantes", [])
    except FileNotFoundError:
        print(f"\n[ERROR] No se encontró el archivo '{nombre_archivo}'.")
        return []
    except json.JSONDecodeError:
        print("\n[ERROR] El archivo JSON tiene un formato inválido.")
        return []

def opcion_2_cargar_estudiante(lista_estudiantes: list) -> None:
    """Solicita y valida los datos de un nuevo estudiante para agregarlo a la lista."""
    print("\n--- Alta de Nuevo Estudiante ---")
    
    # Validar Legajo
    while True:
        entrada = input("Ingrese Legajo (entero): ")
        legajo = validar_legajo(entrada)
        if legajo is not None:
            # Validar que no se repita el legajo
            repetido = False
            for est in lista_estudiantes:
                if est["legajo"] == legajo:
                    repetido = True
                    break
            if not repetido:
                break
            print("[ERROR] El legajo ya existe. Ingrese otro.")
        else:
            print("[ERROR] Legajo inválido. Debe ser un número entero.")

    # Validar Apellido y Nombre
    while True:
        entrada = input("Ingrese Apellido y Nombre (solo letras): ")
        ape_nom = validar_ape_nom(entrada)
        if ape_nom is not None:
            break
        print("[ERROR] Nombre inválido. No debe contener números ni símbolos.")

    # Validar Género
    while True:
        entrada = input("Ingrese Género (F / M / X): ")
        genero = validar_genero(entrada)
        if genero is not None:
            break
        print("[ERROR] Género inválido. Opciones válidas: F, M, X.")

    # Validar Primer Parcial
    while True:
        entrada = input("Ingrese Nota Primer Parcial (1-10): ")
        pp = validar_nota(entrada)
        if pp is not None:
            break
        print("[ERROR] Nota inválida. Debe ser un entero entre 1 y 10.")

    # Validar Segundo Parcial
    while True:
        entrada = input("Ingrese Nota Segundo Parcial (1-10): ")
        sp = validar_nota(entrada)
        if sp is not None:
            break
        print("[ERROR] Nota inválida. Debe ser un entero entre 1 y 10.")

    # Crear diccionario e insertar (promedio inicializado en 0)
    nuevo_estudiante = {
        "legajo": legajo,
        "ape_nom": ape_nom,
        "genero": genero,
        "pp": pp,
        "sp": sp,
        "prom": 0.0
    }
    lista_estudiantes.append(nuevo_estudiante)
    print(f"\n[ÉXITO] Estudiante {ape_nom} cargado correctamente.")

def mostrar_un_elemento(estudiante: dict) -> None:
    """Muestra los datos de un único estudiante en formato de fila."""
    promedio = estudiante.get("prom", 0.0)
    print(f"{estudiante['legajo']:<8} | {estudiante['ape_nom']:<20} | {estudiante['genero']:<6} | {estudiante['pp']:<10} | {estudiante['sp']:<11} | {promedio:<8.2f}")

def opcion_3_mostrar_todos(lista_estudiantes: list) -> None:
    """Recorre y muestra todos los estudiantes cargados (Nota 5)."""
    if not lista_estudiantes:
        print("\nNo hay estudiantes para mostrar.")
        return
    
    print("\n" + "="*70)
    print(f"{'LEGAJO':<8} | {'APELLIDO Y NOMBRE':<20} | {'GÉNERO':<6} | {'1° PARCIAL':<10} | {'2° PARCIAL':<11} | {'PROMEDIO':<8}")
    print("="*70)
    for estudiante in lista_estudiantes:
        mostrar_un_elemento(estudiante)
    print("="*70)

def opcion_4_calcular_promedios(lista_estudiantes: list) -> None:
    """Calcula el promedio (float) de las notas de cada estudiante."""
    for estudiante in lista_estudiantes:
        # Se calcula el promedio simple de ambos parciales
        promedio = (estudiante["pp"] + estudiante["sp"]) / 2.0
        # Guardamos el promedio bajo la clave 'prom' (o 'promedio' según consistencia de datos)
        estudiante["prom"] = round(promedio, 2)
    print("\n[ÉXITO] Promedios calculados y actualizados para todos los estudiantes.")

def opcion_5_ordenar_por_promedio_desc(lista_estudiantes: list) -> None:
    """Muestra los estudiantes ordenados por promedio de forma DESCENDENTE usando Bubble Sort."""
    lista_copia = lista_estudiantes.copy()
    n = len(lista_copia)
    
    # Ordenamiento de burbuja descendente por la clave 'prom'
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_copia[j]["prom"] < lista_copia[j + 1]["prom"]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                
    print("\n--- Estudiantes Ordenados por Promedio (Descendente) ---")
    opcion_3_mostrar_todos(lista_copia)

def opcion_6_mostrar_mayor_promedio(lista_estudiantes: list) -> None:
    """Busca y muestra al o los estudiantes con el promedio más alto."""
    if not lista_estudiantes:
        return

    # Encontrar el valor máximo de promedio
    mayor_promedio = lista_estudiantes[0]["prom"]
    for estudiante in lista_estudiantes:
        if estudiante["prom"] > mayor_promedio:
            mayor_promedio = estudiante["prom"]

    print(f"\n--- Estudiante(s) con Mayor Promedio ({mayor_promedio:.2f}) ---")
    print("\n" + "="*70)
    print(f"{'LEGAJO':<8} | {'APELLIDO Y NOMBRE':<20} | {'GÉNERO':<6} | {'1° PARCIAL':<10} | {'2° PARCIAL':<11} | {'PROMEDIO':<8}")
    print("="*70)
    for estudiante in lista_estudiantes:
        if estudiante["prom"] == mayor_promedio:
            mostrar_un_elemento(estudiante)
    print("="*70)

def opcion_7_buscar_por_legajo(lista_estudiantes: list) -> None:
    """Busca un estudiante por su número de legajo y lo muestra."""
    entrada = input("\nIngrese el legajo del estudiante a buscar: ")
    legajo_buscado = validar_legajo(entrada)
    
    if legajo_buscado is None:
        print("[ERROR] Legajo inválido.")
        return

    encontrado = None
    for estudiante in lista_estudiantes:
        if estudiante["legajo"] == legajo_buscado:
            encontrado = estudiante
            break

    if encontrado:
        print("\n--- Estudiante Encontrado ---")
        print("\n" + "="*70)
        print(f"{'LEGAJO':<8} | {'APELLIDO Y NOMBRE':<20} | {'GÉNERO':<6} | {'1° PARCIAL':<10} | {'2° PARCIAL':<11} | {'PROMEDIO':<8}")
        print("="*70)
        mostrar_un_elemento(encontrado)
        print("="*70)
    else:
        print(f"\n[INFO] No se encontró ningún estudiante con el legajo {legajo_buscado}.")

def opcion_8_exportar_json(lista_estudiantes: list, nombre_archivo: str = "data_sp.json") -> None:
    """Exporta la lista actual con promedios incluidos a un nuevo archivo JSON."""
    estructura_salida = {"estudiantes": lista_estudiantes}
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(estructura_salida, archivo, indent=2, ensure_ascii=False)
        print(f"\n[ÉXITO] Datos exportados correctamente a '{nombre_archivo}'.")
    except Exception as e:
        print(f"\n[ERROR] No se pudo exportar a JSON: {e}")

def opcion_9_exportar_csv(lista_estudiantes: list, nombre_archivo: str = "data_sp.csv") -> None:
    """Exporta la lista actual con promedios incluidos a un archivo CSV."""
    if not lista_estudiantes:
        print("\nNo hay datos para exportar.")
        return
        
    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            # Tomamos las llaves del primer diccionario como encabezados
            campos = lista_estudiantes[0].keys()
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            escritor.writeheader()
            escritor.writerows(lista_estudiantes)
        print(f"\n[ÉXITO] Datos exportados correctamente a '{nombre_archivo}'.")
    except Exception as e:
        print(f"\n[ERROR] No se pudo exportar a CSV: {e}")