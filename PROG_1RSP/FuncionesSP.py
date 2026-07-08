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
        
        if not (es_letra_base or es_espacio or es_tilde_o_ñ): # Si no es letra, ni espacio, ni tilde, ni ñ, retorna False
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
        nota_int = int(nota_str) # Convertimos a entero para poder comparar
        if nota_int >= 1 and nota_int <= 10: # Validamos que esté entre 1 y 10
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
        genero = convertir_a_mayuscula(entrada[0]) # Toma solo el primer carácter y lo convierte a mayúscula
        
    while not validar_genero(genero): # Validamos el género ingresado
        entrada = input("Error. Ingrese Género válido (F/M/X): ")
        if len(entrada) > 0: # Toma solo el primer carácter y lo convierte a mayúscula
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
    legajo = input("Ingrese Legajo: ")
    while not validar_legajo(legajo): # Validamos que sea un número entero positivo
        legajo = input("Error. Ingrese un Legajo válido: ")
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
    while not validar_nombre_apellido(nombre): # Validamos que sea letra o espacios
        nombre = input("Error. Ingrese Apellido y Nombre válido ")
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
    while not validar_nota(nota): # Validamos que sea un número entero entre 1 y 10
        nota = input(mensaje) # Mostramos el mismo mensaje de solicitud en caso de error
    return int(nota)

def cargar_estudiantes(lista_estudiantes):
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
        "ape_nom": nombre,
        "genero": genero,
        "pp": nota_1,
        "sp": nota_2
    }
    # Agregamos el nuevo estudiante a la lista de estudiantes
    lista_estudiantes = lista_estudiantes + [nuevo_estudiante] 
    print("Estudiante cargado con éxito.")
    return lista_estudiantes


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
    nombre = estudiante["ape_nom"]
    genero = estudiante["genero"]
    n1 = estudiante["pp"]
    n2 = estudiante["sp"]
    
    # Comprobamos de manera simple si ya se le asignó la clave promedio.
    if "promedio" in estudiante:
        prom = estudiante["promedio"] 
        # Usa los modificadores de formato f-string (como :<6 o :<20) para alinear el texto a la izquierda con un ancho fijo de caracteres. 
        # Hace que la salida sea más legible y uniforme.
        print(f"Legajo: {legajo:<6} | Nombre: {nombre:<20} | Género: {genero} | P1: {n1:<2} | P2: {n2:<2} | Promedio: {prom:.2f}")
    else:
        print(f"Legajo: {legajo:<6} | Nombre: {nombre:<20} | Género: {genero} | P1: {n1:<2} | P2: {n2:<2} | Promedio: -")

def mostrar_todos_los_elementos(lista_estudiantes):
    """
    Recorre la lista completa de estudiantes y muestra los datos de cada uno.
    
    Parametros:
    lista_estudiantes (list): Lista de estudiantes a mostrar.
    
    Retorna:
    None
    """
    if len(lista_estudiantes) == 0: # Si la lista está vacía, muestra el mensaje
        print("No hay estudiantes para mostrar.")
    else:
        print("\n--- Lista de Estudiantes ---") 
        for estudiante in lista_estudiantes: # Recorre la lista y llama a la función mostrar_un_elemento para cada estudiante
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
    for estudiante in lista_estudiantes: # Recorre la lista y calcula el promedio de cada estudiante
        n1 = estudiante["pp"]
        n2 = estudiante["sp"]
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
    for estudiante in lista_estudiantes: # Recorre la lista y verifica si ya se calculó el promedio
        if "promedio" not in estudiante:
            print("Error: Primero debes calcular los promedios (Opción 4).")
            return
            
    # Hacemos una copia de la lista para no modificar la original y aplicamos el método de ordenamiento burbuja
    lista_ordenada = lista_estudiantes[:]
    n = len(lista_ordenada)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_ordenada[j]["promedio"] < lista_ordenada[j+1]["promedio"]: 
            # Comparamos los promedios de los estudiantes
                aux = lista_ordenada[j] # Intercambiamos los elementos si el promedio del estudiante actual es menor que el del siguiente
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
    for estudiante in lista_estudiantes: # Recorre la lista y verifica si ya se calculó el promedio
        if "promedio" not in estudiante: # Si no se ha calculado el promedio, muestra un mensaje de error y retorna
            print("Primero debes calcular los promedios.")
            return

    # Buscar la nota máxima
    mayor_promedio = -1.0 # Inicializamos con un valor bajo para asegurarnos de que cualquier promedio válido lo supere
    for estudiante in lista_estudiantes: # Recorre la lista y busca el mayor promedio
        if estudiante["promedio"] > mayor_promedio: # Actualiza el mayor promedio si encontramos uno más alto
            mayor_promedio = estudiante["promedio"]
            
    print(f"\n--- Estudiante(s) con Mayor Promedio ({mayor_promedio:.2f}) ---")
    for estudiante in lista_estudiantes: # Recorre la lista nuevamente y muestra todos los estudiantes que tengan el mayor promedio
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
    legajo_buscar = pedir_legajo() # Pide al usuario que ingrese un legajo válido y lo valida
    encontrado = False # Bandera para indicar si se encontró el estudiante o no
    
    for estudiante in lista_estudiantes: # Recorre la lista de estudiantes y compara el legajo ingresado con el legajo de cada estudiante
        if estudiante["legajo"] == legajo_buscar: # Si encontramos un estudiante con el legajo ingresado, mostramos sus datos y cambiamos la bandera a True
            print("\nEstudiante Encontrado:")
            mostrar_un_elemento(estudiante)
            encontrado = True # Cambiamos la bandera a True para indicar que se encontró el estudiante
            break 
            
    if not encontrado: # Si no se encontró ningún estudiante con el legajo ingresado, mostramos un mensaje indicando que no se encontró
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
    # Abrimos directamente el archivo asumiendo que ya existe en el directorio
    with open(nombre_archivo, "r", encoding="utf-8") as archivo: # UTF-8 es importante para soportar caracteres especiales como acentos y ñ
        # Abrimos el archivo en modo lectura y con codificación UTF-8 para soportar caracteres especiales
        lista = json.load(archivo) 
        # El método json.load() carga el contenido del archivo JSON y lo convierte en una lista de diccionarios de Python
        print(f"Datos cargados exitosamente desde {nombre_archivo}.")
        return lista

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
        # Whit open abre el archivo en modo escritura y con codificación UTF-8 para soportar caracteres especiales
        json.dump(lista_estudiantes, archivo, indent=4, ensure_ascii=False)
        # .dump() convierte la lista de estudiantes en formato JSON y la escribe en el archivo, 
        # con una indentación de 4 espacios para mejorar la legibilidad 
        # ensure_ascii=False para permitir caracteres especiales como acentos y ñ en el archivo JSON
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
    if len(lista_estudiantes) == 0: # Si la lista está vacía no tiene sentido crear un archivo CSV
        print("No hay datos para exportar.")
        return
        
    with open(nombre_archivo, "w", encoding="utf-8") as archivo: 
        # Abrimos el archivo en modo escritura y con codificación UTF-8 para soportar caracteres especiales
        # Escribimos la cabecera del archivo CSV
        archivo.write("legajo,ape_nom,genero,pp,sp,promedio\n") 
        # archivo.write() escribe la cadena en el archivo
        
        for est in lista_estudiantes: # Recorremos la lista de estudiantes y escribimos cada uno en el archivo CSV
            # Extraemos los datos del estudiante y los escribimos en el archivo CSV separados por comas
            legajo = est["legajo"]
            nombre = est["ape_nom"]
            genero = est["genero"]
            n1 = est["pp"]
            n2 = est["sp"]
            prom = est["prom"] if "prom" in est else ""
                
            archivo.write(f"{legajo},{nombre},{genero},{n1},{n2},{prom}\n")
            # Escribimos cada estudiante en una nueva línea del archivo CSV, usando f-strings para formatear la cadena
    print(f"Datos exportados correctamente a {nombre_archivo}.")