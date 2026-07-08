import json

# ==========================================
# VALIDACIONES (Nota 4)
# ==========================================

def validar_genero(genero):
    """Valida que el género sea F, M o X."""
    if genero == "F" or genero == "M" or genero == "X":
        return True
    return False

def validar_legajo(legajo_str):
    """Valida que el legajo sea un número entero positivo."""
    if legajo_str.isdigit():
        return True
    return False

def validar_nombre_apellido(texto):
    """Valida que el texto no esté vacío y contenga letras o espacios."""
    if len(texto) == 0:
        return False
    for caracter in texto:
        # Permitimos letras y espacios
        if not (caracter.isalpha() or caracter == " "):
            return False
    return True

def validar_nota(nota_str):
    """Valida que la nota sea un entero entre 1 y 10."""
    if nota_str.isdigit():
        nota_int = int(nota_str)
        if nota_int >= 1 and nota_int <= 10:
            return True
    return False


# ==========================================
# FUNCIONES DE CARGA Y PROCESAMIENTO
# ==========================================

def pedir_genero():
    genero = input("Ingrese Género (F/M/X): ").upper()
    while not validar_genero(genero):
        genero = input("Error. Ingrese Género válido (F/M/X): ").upper()
    return genero

def pedir_legajo():
    legajo = input("Ingrese Legajo (entero): ")
    while not validar_legajo(legajo):
        legajo = input("Error. Ingrese un Legajo válido (solo números): ")
    return int(legajo)

def pedir_nombre_apellido():
    nombre = input("Ingrese Apellido y Nombre: ")
    while not validar_nombre_apellido(nombre):
        nombre = input("Error. Ingrese Apellido y Nombre válido (solo letras): ")
    return nombre

def pedir_nota(mensaje):
    nota = input(mensaje)
    while not validar_nota(nota):
        nota = input("Error. " + mensaje)
    return int(nota)

def cargar_estudiante_manual(lista_estudiantes):
    """Ítem 2: Realiza la carga de un estudiante validando cada dato."""
    print("\n--- Carga de Nuevo Estudiante ---")
    legajo = pedir_legajo()
    nombre = pedir_nombre_apellido()
    genero = pedir_genero()
    nota_1 = pedir_nota("Ingrese Nota del Primer Parcial (1-10): ")
    nota_2 = pedir_nota("Ingrese Nota del Segundo Parcial (1-10): ")
    
    nuevo_estudiante = {
        "legajo": legajo,
        "apellido_nombre": nombre,
        "genero": genero,
        "nota_p1": nota_1,
        "nota_p2": nota_2
    }
    
    lista_estudiantes.append(nuevo_estudiante)
    print("Estudiante cargado con éxito.")


# ==========================================
# FUNCIONES DE MOSTRAR (Nota 5)
# ==========================================

def mostrar_un_elemento(estudiante):
    """Muestra los datos de un solo estudiante."""
    legajo = estudiante["legajo"]
    nombre = estudiante["apellido_nombre"]
    genero = estudiante["genero"]
    n1 = estudiante["nota_p1"]
    n2 = estudiante["nota_p2"]
    
    # Si ya se calculó el promedio, lo mostramos; si no, ponemos un guión
    if "promedio" in estudiante:
        prom = estudiante["promedio"]
        print(f"Legajo: {legajo:<6} | Nombre: {nombre:<20} | Género: {genero} | P1: {n1:<2} | P2: {n2:<2} | Promedio: {prom:.2f}")
    else:
        print(f"Legajo: {legajo:<6} | Nombre: {nombre:<20} | Género: {genero} | P1: {n1:<2} | P2: {n2:<2} | Promedio: -")

def mostrar_todos_los_elementos(lista_estudiantes):
    """Ítem 3: Recorre la lista y llama a la función de mostrar un elemento."""
    if len(lista_estudiantes) == 0:
        print("No hay estudiantes para mostrar.")
    else:
        print("\n--- Lista de Estudiantes ---")
        for estudiante in lista_estudiantes:
            mostrar_un_elemento(estudiante)


# ==========================================
# LOGICA DEL NEGOCIO (Items 4, 5, 6, 7)
# ==========================================

def calcular_promedio_estudiante(nota1, nota2):
    """Calcula el promedio matemático simple."""
    return (nota1 + nota2) / 2

def calcular_todos_los_promedios(lista_estudiantes):
    """Ítem 4: Calcula y agrega la clave promedio a cada diccionario."""
    for estudiante in lista_estudiantes:
        n1 = estudiante["nota_p1"]
        n2 = estudiante["nota_p2"]
        prom = calcular_promedio_estudiante(n1, n2)
        estudiante["promedio"] = prom
    print("Promedios calculados correctamente para todos los estudiantes.")

def ordenar_estudiantes_por_promedio_desc(lista_estudiantes):
    """Ítem 5: Ordena la lista de manera DESCENDENTE usando método Burbuja manual."""
    # Primero nos aseguramos que todos tengan el promedio calculado
    for estudiante in lista_estudiantes:
        if "promedio" not in estudiante:
            print("Error: Primero debes calcular los promedios (Opción 4).")
            return
            
    # Hacemos una copia de la lista para no alterar el orden original si no se desea
    lista_ordenada = []
    for est in lista_estudiantes:
        lista_ordenada.append(est)
        
    n = len(lista_ordenada)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]["promedio"] < lista_ordenada[j+1]["promedio"]:
                # Intercambio manual básico
                aux = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j+1]
                lista_ordenada[j+1] = aux
                
    print("\n--- Estudiantes Ordenados por Promedio (Descendente) ---")
    for estudiante in lista_ordenada:
        mostrar_un_elemento(estudiante)

def mostrar_mayor_promedio(lista_estudiantes):
    """Ítem 6: Busca el mayor promedio y muestra al o los estudiantes que lo tengan."""
    for estudiante in lista_estudiantes:
        if "promedio" not in estudiante:
            print("Error: Primero debes calcular los promedios (Opción 4).")
            return

    # 1. Encontrar el número del mayor promedio
    mayor_promedio = -1.0
    for estudiante in lista_estudiantes:
        if estudiante["promedio"] > mayor_promedio:
            mayor_promedio = estudiante["promedio"]
            
    # 2. Recorrer y mostrar los que coincidan usando las funciones del ítem 3
    print(f"\n--- Estudiante(s) con Mayor Promedio ({mayor_promedio:.2f}) ---")
    for estudiante in lista_estudiantes:
        if estudiante["promedio"] == mayor_promedio:
            mostrar_un_elemento(estudiante)

def buscar_por_legajo(lista_estudiantes):
    """Ítem 7: Busca un estudiante por su legajo único."""
    legajo_buscar = pedir_legajo()
    encontrado = False
    
    for estudiante in lista_estudiantes:
        if estudiante["legajo"] == legajo_buscar:
            print("\nEstudiante Encontrado:")
            mostrar_un_elemento(estudiante)
            encontrado = True
            break # Salimos del bucle si lo encontramos ya que el legajo es único
            
    if not encontrado:
        print(f"No se encontró ningún estudiante con el legajo {legajo_buscar}.")


# ==========================================
# MANEJO DE ARCHIVOS (Items 1, 8, 9)
# ==========================================

def leer_json(nombre_archivo):
    """Ítem 1: Lee el archivo JSON."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lista = json.load(archivo)
            print(f"Datos cargados exitosamente desde {nombre_archivo}.")
            return lista
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. Se iniciará con lista vacía.")
        return []

def exportar_json(nombre_archivo, lista_estudiantes):
    """Ítem 8: Exporta la lista actual a un archivo JSON."""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista_estudiantes, archivo, indent=4, ensure_ascii=False)
    print(f"Datos exportados correctamente a {nombre_archivo}.")

def exportar_csv(nombre_archivo, lista_estudiantes):
    """Ítem 9: Exporta la lista actual a un archivo CSV de forma manual."""
    if len(lista_estudiantes) == 0:
        print("No hay datos para exportar.")
        return
        
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # Escribimos los encabezados primero
        archivo.write("legajo,apellido_nombre,genero,nota_p1,nota_p2,promedio\n")
        
        # Recorremos y escribimos cada fila
        for est in lista_estudiantes:
            legajo = est["legajo"]
            nombre = est["apellido_nombre"]
            genero = est["genero"]
            n1 = est["nota_p1"]
            n2 = est["nota_p2"]
            
            # Validamos si tiene promedio calculado para escribirlo
            if "promedio" in est:
                prom = est["promedio"]
            else:
                prom = ""
                
            archivo.write(f"{legajo},{nombre},{genero},{n1},{n2},{prom}\n")
            
    print(f"Datos exportados correctamente a {nombre_archivo}.")