import json
import csv

# ==========================================
# VALIDACIONES (Nota 4)
# ==========================================

def validar_genero(genero: str) -> bool:
    """Valida que el género sea 'F', 'M' o 'X'."""
    return genero.upper() in ['F', 'M', 'X']

def validar_legajo(legajo: str) -> bool:
    """Valida que el legajo sea numérico entero positivo."""
    return legajo.isdigit() and int(legajo) > 0

def validar_nombre_apellido(nombre: str) -> bool:
    """Valida que el nombre y apellido sea alfabético (incluyendo espacios)."""
    # Reemplazamos espacios para verificar que el resto sean letras
    return nombre.replace(" ", "").isalpha()

def validar_nota(nota: str) -> bool:
    """Valida que la nota sea un entero entre 1 y 10."""
    if nota.isdigit():
        num = int(nota)
        return 1 <= num <= 10
    return False


# ==========================================
# FUNCIONES DE CARGA Y PROCESAMIENTO
# ==========================================

def leer_json(nombre_archivo: str) -> list:
    """Ítem 1: Lee el archivo JSON y devuelve la lista de estudiantes."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            data = json.load(archivo)
            return data.get("estudiantes", [])
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
        return []

def cargar_estudiante_manual() -> dict:
    """Ítem 2: Realiza la carga de un estudiante validando cada dato."""
    print("\n--- Carga de Nuevo Estudiante ---")
    
    legajo = input("Ingrese Legajo: ")
    while not validar_legajo(legajo):
        legajo = input("Legajo inválido. Ingrese un número entero positivo: ")
        
    ape_nom = input("Ingrese Apellido y Nombre: ")
    while not validar_nombre_apellido(ape_nom):
        ape_nom = input("Nombre inválido. Use solo letras y espacios: ")
        
    genero = input("Ingrese Género (F/M/X): ")
    while not validar_genero(genero):
        genero = input("Género inválido. Ingrese F, M o X: ")
        
    pp = input("Nota Primer Parcial (1-10): ")
    while not validar_nota(pp):
        pp = input("Nota inválida. Ingrese un entero de 1 a 10: ")
        
    sp = input("Nota Segundo Parcial (1-10): ")
    while not validar_nota(sp):
        sp = input("Nota inválida. Ingrese un entero de 1 a 10: ")

    return {
        "legajo": int(legajo),
        "ape_nom": ape_nom,
        "genero": genero.upper(),
        "pp": int(pp),
        "sp": int(sp),
        "prom": 0.0
    }


# ==========================================
# FUNCIONES DE MOSTRAR (Nota 5)
# ==========================================

def mostrar_un_estudiante(estudiante: dict):
    """Muestra los datos en formato de fila de un solo estudiante."""
    # Se formatea dinámicamente incluyendo el promedio si ya fue calculado
    promedio = estudiante.get('prom', 0.0)
    print(f"{estudiante['legajo']:<8} | {estudiante['ape_nom']:<20} | {estudiante['genero']:<6} | {estudiante['pp']:<6} | {estudiante['sp']:<6} | {promedio:<6.2f}")

def mostrar_estudiantes(lista_estudiantes: list):
    """Ítem 3: Recorre y muestra todos los estudiantes usando mostrar_un_estudiante."""
    if not lista_estudiantes:
        print("No hay estudiantes cargados.")
        return
    
    print(f"\n{'Legajo':<8} | {'Apellido y Nombre':<20} | {'Género':<6} | {'PP':<6} | {'SP':<6} | {'Prom':<6}")
    print("-" * 60)
    for estudiante in lista_estudiantes:
        mostrar_un_estudiante(estudiante)


# ==========================================
# CÁLCULOS, ORDENAMIENTO Y BÚSQUEDA
# ==========================================

def calcular_promedios(lista_estudiantes: list):
    """Ítem 4: Calcula el promedio (float) de cada estudiante en la lista."""
    for estudiante in lista_estudiantes:
        promedio = (estudiante['pp'] + estudiante['sp']) / 2
        estudiante['prom'] = round(promedio, 2)
    print("Promedios calculados con éxito.")

def ordenar_por_promedio_desc(lista_estudiantes: list) -> list:
    """Ítem 5: Ordena la lista de estudiantes por promedio de forma DESC (Bubble Sort adaptado)."""
    lista_copia = lista_estudiantes.copy()
    n = len(lista_copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j]['prom'] < lista_copia[j + 1]['prom']:
                # Intercambio
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia

def mostrar_mayor_promedio(lista_estudiantes: list):
    """Ítem 6: Busca y muestra al o los estudiantes con el promedio más alto."""
    if not lista_estudiantes:
        return
    
    # Encontrar el valor máximo
    max_promedio = lista_estudiantes[0]['prom']
    for estudiante in lista_estudiantes:
        if estudiante['prom'] > max_promedio:
            max_promedio = estudiante['prom']
            
    print(f"\n--- Estudiante(s) con mayor promedio ({max_promedio}) ---")
    print(f"{'Legajo':<8} | {'Apellido y Nombre':<20} | {'Género':<6} | {'PP':<6} | {'SP':<6} | {'Prom':<6}")
    print("-" * 60)
    
    for estudiante in lista_estudiantes:
        if estudiante['prom'] == max_promedio:
            mostrar_un_estudiante(estudiante)

def buscar_por_legajo(lista_estudiantes: list):
    """Ítem 7: Busca un estudiante por legajo e imprime sus datos."""
    legajo_buscar = input("Ingrese el legajo del estudiante a buscar: ")
    if not legajo_buscar.isdigit():
        print("Legajo inválido.")
        return
    
    legajo_buscar = int(legajo_buscar)
    encontrado = False
    
    for estudiante in lista_estudiantes:
        if estudiante['legajo'] == legajo_buscar:
            print(f"\n{'Legajo':<8} | {'Apellido y Nombre':<20} | {'Género':<6} | {'PP':<6} | {'SP':<6} | {'Prom':<6}")
            print("-" * 60)
            mostrar_un_estudiante(estudiante)
            encontrado = True
            break
            
    if not encontrado:
        print(f"No se encontró ningún estudiante con el legajo {legajo_buscar}.")


# ==========================================
# EXPORTACIÓN DE ARCHIVOS
# ==========================================

def exportar_a_json(lista_estudiantes: list, nombre_archivo: str):
    """Ítem 8: Exporta la lista actual con sus promedios a un archivo JSON."""
    data = {"estudiantes": lista_estudiantes}
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)
    print(f"Datos exportados correctamente a {nombre_archivo}")

def exportar_a_csv(lista_estudiantes: list, nombre_archivo: str):
    """Ítem 9: Exporta la lista actual con sus promedios a un archivo CSV."""
    if not lista_estudiantes:
        return
    
    # Obtenemos los encabezados basados en las llaves del diccionario
    campos = list(lista_estudiantes[0].keys())
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_estudiantes)
    print(f"Datos exportados correctamente a {nombre_archivo}")