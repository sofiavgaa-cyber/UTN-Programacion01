import json

# ==========================================
# VALIDACIONES
# ==========================================

def es_numero_entero(cadena):
    """
    Verifica si una cadena es numérica usando los valores ASCII del '0' al '9'.
       
    Parametros:
    cadena (str): La cadena a validar.

    Retorna:
    bool: True si la cadena es un número entero, False en caso contrario.
    """
    if len(cadena) == 0:
        return False
    
    for caracter in cadena:
        codigo = ord(caracter)
        # ASCII, los caracteres '0' al '9' son del 48 al 57
        if codigo < 48 or codigo > 57:
            return False
    return True

def es_letra_o_espacio(cadena):
    """
    Verifica si la cadena tiene letras (mayús/minús) o espacios usando ASCII.

    Parametros:
    cadena (str): La cadena a validar.

    Retorna:
    bool: True si la cadena tiene solo letras o espacios, False en caso contrario.
    """
    if len(cadena) == 0:
        return False
        
    for caracter in cadena:
        codigo = ord(caracter)
        # Espacio en blanco (32)
        # Mayúsculas 'A'-'Z' (65-90)
        # Minúsculas 'a'-'z' (97-122)
        # Caracteres especiales del español como la 'ñ' (241), 'Ñ' (209) o vocales con tilde
        es_letra_base = (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122)
        es_espacio = (codigo == 32)
        es_tilde_o_ñ = (codigo == 241 or codigo == 209 or codigo == 225 or codigo == 233 or codigo == 237 or codigo == 243 or codigo == 250)
        
        if not (es_letra_base or es_espacio or es_tilde_o_ñ):
            return False
    return True

def convertir_a_mayuscula(caracter):
    """
    Convierte una letra minúscula a mayúscula restando la distancia ASCII (32).
    
    Parametros:
    caracter (str): El carácter a convertir.

    Retorna:
    str: El carácter en mayúscula si era minúscula, o el mismo carácter si no lo era.
    """
    codigo = ord(caracter)
    # Si está entre 'a' (97) y 'z' (122), le restamos 32 para pasar a 'A'-'Z'
    if codigo >= 97 and codigo <= 122:
        return chr(codigo - 32)
    return caracter

def validar_genero(genero):
    """
    Valida que el género sea F, M o X.
    
    Parametros:
    genero (str): El género a validar.

    Retorna:
    bool: True si el género es válido, False en caso contrario.
    """
    if genero == "F" or genero == "M" or genero == "X":
        return True
    return False

def validar_legajo(legajo_str):
    """
    Valida que el legajo sea un número entero positivo.
   
    Parametros:
    legajo_str (str): El legajo a validar.

    Retorna:
    bool: True si el legajo es válido, False en caso contrario.
    """
    return es_numero_entero(legajo_str)

def validar_nombre_apellido(texto):
    """
    Valida que el texto sea alfabético con espacios.
    
    Parametros:
    texto (str): El texto a validar.

    Retorna:
    bool: True si el texto es válido, False en caso contrario.
    """
    return es_letra_o_espacio(texto)

def validar_nota(nota_str):
    """
    Valida que la nota sea un entero entre 1 y 10.

    Parametros:
    nota_str (str): La nota a validar.

    Retorna:
    bool: True si la nota es válida, False en caso contrario.
    """
    if es_numero_entero(nota_str):
        nota_int = int(nota_str)
        if nota_int >= 1 and nota_int <= 10:
            return True
    return False


# ==========================================
# FUNCIONES DE CARGA Y PROCESAMIENTO
# ==========================================

def pedir_genero():
    """
    Pide al usuario que ingrese un género válido (F, M o X) y lo valida.
    
    Parametros:
    None
    
    Retorna:
    str: El género ingresado y validado.
    """
    entrada = input("Ingrese Género (F/M/X): ")
    genero = ""
    if len(entrada) > 0:
        genero = convertir_a_mayuscula(entrada[0])
        
    while not validar_genero(genero):
        entrada = input("Error. Ingrese Género válido (F/M/X): ")
        if len(entrada) > 0:
            genero = convertir_a_mayuscula(entrada[0])
    return genero

def pedir_legajo():
    """
    Pide al usuario que ingrese un legajo válido y lo valida.

    Parametros:
    None

    Retorna:
    int: El legajo ingresado y validado.
    """
    legajo = input("Ingrese Legajo (entero): ")
    while not validar_legajo(legajo):
        legajo = input("Error. Ingrese un Legajo válido (solo números): ")
    return int(legajo)

def pedir_nombre_apellido():
    """
    Pide al usuario que ingrese un nombre y apellido válidos y los valida.

    Parametros:
    None

    Retorna:
    str: El nombre y apellido ingresados y validados.
    """
    nombre = input("Ingrese Apellido y Nombre: ")
    while not validar_nombre_apellido(nombre):
        nombre = input("Error. Ingrese Apellido y Nombre válido (solo letras): ")
    return nombre

def pedir_nota(mensaje):
    """
    Pide al usuario que ingrese una nota válida (1-10) y la valida.

    Parametros:
    mensaje (str): El mensaje a mostrar al usuario para solicitar la nota.

    Retorna:
    int: La nota ingresada y validada.
    """ 
    nota = input(mensaje)
    while not validar_nota(nota):
        nota = input("Error. " + mensaje)
    return int(nota)

def cargar_estudiante_manual(lista_estudiantes):
    """
    Realiza la carga de un estudiante validando cada dato.

    Parametros:
    lista_estudiantes (list): La lista donde se almacenarán los estudiantes.
    
    Retorna:
    None
    """
    print("\n--- Carga de Nuevo Estudiante ---")
    legajo = pedir_legajo()
    nombre = pedir_nombre_apellido()
    genero = pedir_genero()
    nota_1 = pedir_nota("Ingrese Nota del Primer Parcial: ")
    nota_2 = pedir_nota("Ingrese Nota del Segundo Parcial: ")
    
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
# FUNCIONES DE MOSTRAR Y ORDENAR
# ==========================================

def mostrar_un_elemento(estudiante):
    """
    Muestra los datos de un solo estudiante.
    
    Parametros:
    estudiante (dict): Diccionario con los datos del estudiante.
    
    Retorna:
    None
    """
    legajo = estudiante["legajo"]
    nombre = estudiante["apellido_nombre"]
    genero = estudiante["genero"]
    n1 = estudiante["nota_p1"]
    n2 = estudiante["nota_p2"]
    
    # Comprobamos de manera simple si ya se le asignó la clave promedio
    if "promedio" in estudiante:
        prom = estudiante["promedio"]
        print(f"Legajo: {legajo:<6} | Nombre: {nombre:<20} | Género: {genero} | P1: {n1:<2} | P2: {n2:<2} | Promedio: {prom:.2f}")
    else:
        print(f"Legajo: {legajo:<6} | Nombre: {nombre:<20} | Género: {genero} | P1: {n1:<2} | P2: {n2:<2} | Promedio: -")

def mostrar_todos_los_elementos(lista_estudiantes):
    """
    Recorre la lista llamando internamente a la función individual.
    
    Parametros:
    lista_estudiantes (list): Lista de estudiantes a mostrar.
    
    Retorna:
    None
    """
    if len(lista_estudiantes) == 0:
        print("No hay estudiantes para mostrar.")
    else:
        print("\n--- Lista de Estudiantes ---")
        for estudiante in lista_estudiantes:
            mostrar_un_elemento(estudiante)


# ==========================================
# FUNCIONES DE CÁLCULO Y BÚSQUEDA
# ==========================================

def calcular_todos_los_promedios(lista_estudiantes):
    """
    Calcula y guarda el promedio.
    
    Parametros:
    lista_estudiantes (list): Lista de estudiantes a procesar.
    
    Retorna:
    None
    """
    for estudiante in lista_estudiantes:
        n1 = estudiante["nota_p1"]
        n2 = estudiante["nota_p2"]
        estudiante["promedio"] = (n1 + n2) / 2
    print("Promedios calculados correctamente para todos los estudiantes.")

def ordenar_estudiantes_por_promedio_desc(lista_estudiantes):
    """
    Ordena la lista de manera DESC usando el método Burbuja.

    Parametros:
    lista_estudiantes (list): Lista de estudiantes a ordenar.

    Retorna:
    None
    """
    for estudiante in lista_estudiantes:
        if "promedio" not in estudiante:
            print("Error: Primero debes calcular los promedios (Opción 4).")
            return
            
    # Hacemos una copia superficial usando rebanado de lista tradicional (lista[:])
    lista_ordenada = lista_estudiantes[:]
    n = len(lista_ordenada)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]["promedio"] < lista_ordenada[j+1]["promedio"]:
                aux = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j+1]
                lista_ordenada[j+1] = aux
                
    print("\n--- Estudiantes Ordenados por Promedio (Descendente) ---")
    for estudiante in lista_ordenada:
        mostrar_un_elemento(estudiante)

def mostrar_mayor_promedio(lista_estudiantes):
    """
    Busca el mayor promedio.
    
    Parametros:
    lista_estudiantes (list): Lista de estudiantes a procesar.
    
    Retorna:
    None
    """
    for estudiante in lista_estudiantes:
        if "promedio" not in estudiante:
            print("Error: Primero debes calcular los promedios (Opción 4).")
            return

    # Buscar la nota máxima
    mayor_promedio = -1.0
    for estudiante in lista_estudiantes:
        if estudiante["promedio"] > mayor_promedio:
            mayor_promedio = estudiante["promedio"]
            
    print(f"\n--- Estudiante(s) con Mayor Promedio ({mayor_promedio:.2f}) ---")
    for estudiante in lista_estudiantes:
        if estudiante["promedio"] == mayor_promedio:
            mostrar_un_elemento(estudiante)

def buscar_por_legajo(lista_estudiantes):
    """
    Busca un estudiante específico usando su legajo.
    
    Parametros:
    lista_estudiantes (list): Lista de estudiantes a procesar.
    
    Retorna:
    None
    """
    legajo_buscar = pedir_legajo()
    encontrado = False
    
    for estudiante in lista_estudiantes:
        if estudiante["legajo"] == legajo_buscar:
            print("\nEstudiante Encontrado:")
            mostrar_un_elemento(estudiante)
            encontrado = True
            break 
            
    if not encontrado:
        print(f"No se encontró ningún estudiante con el legajo {legajo_buscar}.")


# ==========================================
# FUNCIONES DE EXPORTACIÓN
# ==========================================

def leer_json(nombre_archivo):
    """
    Carga el archivo JSON usando la librería.
    
    Parametros:
    nombre_archivo (str): Nombre del archivo JSON a leer.
    
    Retorna:
    list: Lista de estudiantes cargada desde el archivo, o lista vacía si no existe.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lista = json.load(archivo)
            print(f"Datos cargados exitosamente desde {nombre_archivo}.")
            return lista
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. Se iniciará con lista vacía.")
        return []

def exportar_json(nombre_archivo, lista_estudiantes):
    """
    Exporta la estructura a JSON formateado.
    
    Parametros:
    nombre_archivo (str): Nombre del archivo JSON a crear.
    lista_estudiantes (list): Lista de estudiantes a exportar.
    
    Retorna:
    None
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista_estudiantes, archivo, indent=4, ensure_ascii=False)
    print(f"Datos exportados correctamente a {nombre_archivo}.")

def exportar_csv(nombre_archivo, lista_estudiantes):
    """
    Genera el archivo de texto como CSV con los datos de los estudiantes.
    
    Parametros:
    nombre_archivo (str): Nombre del archivo CSV a crear.
    lista_estudiantes (list): Lista de estudiantes a exportar.
    
    Retorna:
    None
    """
    if len(lista_estudiantes) == 0:
        print("No hay datos para exportar.")
        return
        
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("legajo,apellido_nombre,genero,nota_p1,nota_p2,promedio\n")
        
        for est in lista_estudiantes:
            legajo = est["legajo"]
            nombre = est["apellido_nombre"]
            genero = est["genero"]
            n1 = est["nota_p1"]
            n2 = est["nota_p2"]
            prom = est["promedio"] if "promedio" in est else ""
                
            archivo.write(f"{legajo},{nombre},{genero},{n1},{n2},{prom}\n")
            
    print(f"Datos exportados correctamente a {nombre_archivo}.")