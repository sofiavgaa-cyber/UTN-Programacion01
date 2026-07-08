# ==========================================
#  VALIDACIONES Y CARGA DE DATOS
# ==========================================
def cargar_datos(legajos, nombres, generos, notas_p1, notas_p2):
    """
    Carga los datos de los estudiantes manualmente, validando cada entrada.

    Parámetros:
    legajos (list): Lista donde se almacenarán los legajos de los estudiantes.
    nombres (list): Lista donde se almacenarán los nombres de los estudiantes.
    generos (list): Lista donde se almacenarán los géneros de los estudiantes.
    notas_p1 (list): Lista donde se almacenarán las notas del primer parcial.
    notas_p2 (list): Lista donde se almacenarán las notas del segundo parcial.
   
    Retorna:
    None: Esta función solo carga los datos en las listas proporcionadas y no retorna ningún valor.
    """
    for i in range(30):
        print("\nCargando datos del estudiante número", i + 1)
                
        legajo = input("Ingrese Legajo: ") # Pide el legajo al usuario
        while validar_legajo(legajo) == False: # Valida que el legajo sea un número entero mayor a 0
            print("El legajo debe ser un número entero mayor a 0.")
            legajo = input("Ingrese Legajo nuevamente: ")
        legajos[i] = int(legajo) # Asignación directa por índice
                
        nombre = input("Ingrese Apellido y Nombre: ") # Pide el nombre al usuario
        while validar_nombre(nombre) == False: # Valida que el nombre no esté vacío y contenga solo letras o espacios
            print("El nombre debe contener solo letras y espacios.")
            nombre = input("Ingrese Apellido y Nombre nuevamente: ")
        nombres[i] = nombre 
                
        genero = input("Ingrese Género (F / M / X): ") # Pide el género al usuario
        # Validamos pidiendo que sea exacto en mayúscula
        while validar_genero(genero) == False: # Valida que el género sea F, M o X
            print("Opciones válidas F, M o X.")
            genero = input("Ingrese Género nuevamente: ")
        generos[i] = genero
                
        n1 = input("Ingrese Nota del Primer Parcial: ") # Pide la nota del primer parcial al usuario
        while validar_nota(n1) == False: # Valida que la nota sea un número entero entre 1 y 10
            print("La nota debe ser un número entero entre 1 y 10.")
            n1 = input("Ingrese Nota 1 nuevamente: ")
        notas_p1[i] = int(n1)
                
        n2 = input("Ingrese Nota del Segundo Parcial: ") # Pide la nota del segundo parcial al usuario
        while validar_nota(n2) == False: # Valida que la nota sea un número entero entre 1 y 10
            print("La nota debe ser un número entero entre 1 y 10.")
            n2 = input("Ingrese Nota 2 nuevamente: ")
        notas_p2[i] = int(n2)

        # Pregunta al usuario si desea cargar más estudiante
        # Si ya cargamos el alumno 30, el bucle termina solo.
        # Si estamos antes del alumno 30, le preguntamos si quiere seguir.
        if i < 29:
            continuar = input("\n¿Desea cargar otro estudiante? (S/N): ")
            while continuar != "S" and continuar != "s" and continuar != "N" and continuar != "n":
                print("Opción inválida. Ingrese S para Sí o N para No.")
                continuar = input("¿Desea cargar otro estudiante? (S/N): ")
                    
        # Si el usuario responde N o n, rompemos el bucle for
        if continuar == "N" or continuar == "n":
            break

        print("\n¡Se cargaron los alumnos con éxito!")
        ya_hay_datos = True # Pone la bandera en True para permitir el uso de las demás opciones

def validar_legajo(legajo):
    """
    Valida que el legajo ingresado sea un número entero mayor a cero.
    
    Parámetros:
    legajo (str): Cadena de texto ingresada por el usuario.
    
    Retorna:
    bool: True si es válido (solo números y > 0), False en caso contrario.
    """
    if legajo == "": # Si el usuario no escribe nada, no es válido
        return False
        
    # Recorre caracter por caracter para ver si son todos números
    for caracter in legajo:
        if caracter < "0" or caracter > "9":
            return False # Si encuentra algo que no es número, devuelve falso
            
    # Si pasa el bucle, lo convierte a entero y ve si es mayor a cero
    legajo_entero = int(legajo)
    if legajo_entero > 0:  
        return True
    else:
        return False

def validar_nombre(nombre):
    """
    Valida que el nombre no esté vacío y contenga solo letras o espacios.
    
    Parámetros:
    nombre (str): Cadena de texto con el nombre/apellido.
    
    Retorna:
    bool: True si contiene solo letras y espacios, False de lo contrario.
    """
    if nombre == "": # Valida que no este vacío
        return False
        
    # Verifica que sean solo letras o espacios
    for caracter in nombre:
        # Chequeamos si NO es una letra (tanto minúscula como mayúscula) y tampoco un espacio
        if not ((caracter >= "a" and caracter <= "z") or (caracter >= "A" and caracter <= "Z") or caracter == " "):
            return False
            
    return True

def validar_genero(genero):
    """
    Valida que el género ingresado sea una de las opciones permitidas (F, M o X).
    
    Parámetros:
    genero (str): Carácter o texto de género ingresado.
    
    Retorna:
    bool: True si coincide con 'F', 'M' o 'X' (sin importar minúsculas), False si no.
    """
    # Solo acepta las letras exactas 
    if genero == "F" or genero == "M" or genero == "X" :
        return True
    else:
        return False

def validar_nota(nota):
    """
    Valida que la nota ingresada sea un número entero entre 1 y 10.
    
    Parámetros:
    nota (str): Cadena de texto con la nota.
    
    Retorna:
    bool: True si es un número entero entre 1 y 10, False de lo contrario.
    """
    if nota == "": # Valida que no este vacío
        return False
        
    # Primero ve si es un número entero
    for caracter in nota:
        if caracter < "0" or caracter > "9":
            return False
            
    nota_entera = int(nota) # Valida que esté entre 1 y 10
    if nota_entera >= 1 and nota_entera <= 10:
        return True
    else:
        return False


# ==========================================
#  FUNCIONES PARA MOSTRAR 
# ==========================================

def mostrar_un_elemento(legajo, nombre, genero, n1, n2, promedio): # Muestra un solo estudiante, con o sin promedio
    """"
    Muestra la información de un solo estudiante.
    
    Parámetros:
    legajo (int): Número de legajo del estudiante.
    nombre (str): Nombre y apellido del estudiante.
    genero (str): Género del estudiante.
    n1 (int): Nota del primer parcial.
    n2 (int): Nota del segundo parcial.
    promedio (float): Promedio del estudiante.
    
    Retorna:
    None: Esta función solo muestra la información y no retorna ningún valor. 
    """
    if promedio == None: # La función recibe None si no hay promedio calculado, para no mostrarlo
        print(f" {legajo:<10} | {nombre:<18} | {genero:^8} | {n1:^11} | {n2:^11}") #Se usa f-strings con modificadores de formato para mantener la tabla alineada
    else: # Si hay promedio, lo muestra
       print(f" {legajo:<10} | {nombre:<18} | {genero:^8} | {n1:^11} | {n2:^11} | {promedio:^10}")
    # :<10 y :<18 alinean el texto a la izquierda reservando un ancho fijo de 10 y 18 caracteres.
    # :^11 centra el texto dentro de un espacio reservado de 11 caracteres para que coincida con los datos.

def recorrer_y_mostrar_elementos(legajos, nombres, generos, nota_p1, nota_p2, promedios): # Muestra todos los estudiantes, con o sin promedio
    """
    Recorre las listas de estudiantes y muestra la información de cada uno.

    Parámetros:
    legajos (list): Lista de legajos de los estudiantes.
    nombres (list): Lista de nombres de los estudiantes.
    generos (list): Lista de géneros de los estudiantes.
    nota_p1 (list): Lista de notas del primer parcial.
    nota_p2 (list): Lista de notas del segundo parcial.
    promedios (list): Lista de promedios de los estudiantes.

    Retorna:
    None: Esta función solo muestra la información y no retorna ningún valor.
    """
    print("\n--- LISTA DE ESTUDIANTES ---")
    if len(promedios) == 0:
        print(f" {'LEGAJO':<10} | {'NOMBRE Y APELLIDO':<18} | {'GÉNERO':<8} | {'PARCIAL 1':^11} | {'PARCIAL 2':^11}")
    else:
        print(f" {'LEGAJO':<10} | {'NOMBRE Y APELLIDO':<18} | {'GÉNERO':<8} | {'PARCIAL 1':^11} | {'PARCIAL 2':^11} | {'PROMEDIO':^10}")
    print("-" * 78)

    cantidad = len(legajos) # Averigua cuántos elementos hay en la lista de legajos (todas las listas tienen la misma cantidad)
    for i in range(cantidad): 
        # Si el legajo es None, significa que no hay alumno cargado en esta posición; nos saltamos el print
        if legajos[i] is None:
            continue
        if len(promedios) == 0: # Verifica si la lista de promedios está vacía, para no mostrarla
            prom = None
        else:
            prom = promedios[i]
        mostrar_un_elemento(legajos[i], nombres[i], generos[i], nota_p1[i], nota_p2[i], prom)
    print("-----------------------------\n")


# ==========================================
#  PROCESAMIENTO DE DATOS Y ENTRADAS
# ==========================================

def calcular_promedios(nota_p1, nota_p2, promedios):
    """
    Calcula los promedios de los estudiantes a partir de sus notas del primer y segundo parcial.

    Parámetros:
    nota_p1 (list): Lista de notas del primer parcial.
    nota_p2 (list): Lista de notas del segundo parcial.
    promedios (list): Lista donde se almacenarán los promedios calculados.

    Retorna:
    None: Esta función solo calcula y almacena los promedios en la lista promedios.
    """
    # Vacia la lista de promedios antes de calcularlos
    for i in range(len(nota_p1)):
        # Si la posición está vacía, no calculamos nada y saltamos a la siguiente
        if nota_p1[i] is None or nota_p2[i] is None:
            continue
        resultado = (nota_p1[i] + nota_p2[i]) / 2
        promedios[i] = resultado  # Asignación algorítmica directa por índice
    print("\nPromedios calculados correctamente.")


# ==========================================
#  ORDENAMIENTO Y BÚSQUEDA
# ==========================================

def ordenar_por_promedio_descendente(legajos, nombres, generos, nota_p1, nota_p2, promedios):
    """
    Ordena las listas de estudiantes en orden descendente según sus promedios utilizando el algoritmo de burbuja.

    Parámetros:
    legajos (list): Lista de legajos de los estudiantes.
    nombres (list): Lista de nombres de los estudiantes.
    generos (list): Lista de géneros de los estudiantes.
    nota_p1 (list): Lista de notas del primer parcial.
    nota_p2 (list): Lista de notas del segundo parcial.
    promedios (list): Lista de promedios de los estudiantes.

    Retorna:
    None: Esta función solo ordena las listas y no retorna ningún valor.
    """
    n = len(promedios) # Guarda la cantidad de elementos en la lista de promedios para usarla en los bucles
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Caso 1: Si el elemento de la derecha es None, ya está en la posición correcta (abajo/al final). 
            # No hacemos nada y continuamos.
            if promedios[j + 1] is None:
                continue
                
            # Caso 2: Si el elemento actual es None pero el de la derecha tiene nota, 
            # forzamos el intercambio para mandar el None hacia el final.
            elif promedios[j] is None:
                intercambiar = True
                
            # Caso 3: Ambos tienen notas válidas, comparamos numéricamente de forma normal.
            else:
                intercambiar = promedios[j] < promedios[j + 1]

            # Si se cumple la condición de intercambio, movemos todas las listas paralelas
            if intercambiar:
             # Intercambio manual usando variables auxiliares una por una
                aux_prom = promedios[j]          #  Guarda el promedio actual en el auxiliar
                promedios[j] = promedios[j + 1]  #  Copia el promedio de al lado en la posición actual (pisando el viejo)
                promedios[j + 1] = aux_prom      #  Recupera el promedio viejo desde el auxiliar y lo ponemos al lado
                
                aux_leg = legajos[j]             #  Como son listas paralelas, hacemos lo mismo con todas las demás listas para mantener el orden correcto
                legajos[j] = legajos[j + 1]
                legajos[j + 1] = aux_leg
                
                aux_nom = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux_nom
                
                aux_gen = generos[j]
                generos[j] = generos[j + 1]
                generos[j + 1] = aux_gen
                
                aux_n1 = nota_p1[j]
                nota_p1[j] = nota_p1[j + 1]
                nota_p1[j + 1] = aux_n1
                
                aux_n2 = nota_p2[j]
                nota_p2[j] = nota_p2[j + 1]
                nota_p2[j + 1] = aux_n2
                
    print("\nAlumnos ordenados de Mayor a Menor promedio.")

def mostrar_estudiantes_con_mayor_promedio(legajos, nombres, generos, nota_p1, nota_p2, promedios):
    """
    Muestra los estudiantes que tienen el promedio más alto.

    Parámetros:
    legajos (list): Lista de legajos de los estudiantes.
    nombres (list): Lista de nombres de los estudiantes.
    generos (list): Lista de géneros de los estudiantes.
    nota_p1 (list): Lista de notas del primer parcial.
    nota_p2 (list): Lista de notas del segundo parcial.
    promedios (list): Lista de promedios de los estudiantes.
    
    Retorna:
    None: Esta función solo muestra la información y no retorna ningún valor.
    """
    nota_mas_alta = None
    for p in promedios:
        if p is not None:
            nota_mas_alta = p
            break
            
    # Si la lista de promedios está vacía, no hay estudiantes con promedio calculado
    if nota_mas_alta is None:
        return
    
    # Buscamos el promedio más alto
    for p in promedios:
        # Si el promedio es None, significa que no hay estudiante cargado en esa posición; nos saltamos la comparación
        if p is None: 
            continue
        if p > nota_mas_alta: # Si encuentra un promedio mayor, lo guarda en la variable
            nota_mas_alta = p
            
    print("\n--- Estudiante/s con el Mayor Promedio (", nota_mas_alta, ") ---")
    for i in range(len(promedios)):
        if promedios[i] is None: 
            continue
        if promedios[i] == nota_mas_alta: # Muestra todos los estudiantes que tengan el promedio más alto
            mostrar_un_elemento(legajos[i], nombres[i], generos[i], nota_p1[i], nota_p2[i], promedios[i])

def buscar_estudiante_por_legajo(legajos, nombres, generos, nota_p1, nota_p2, promedios):
    """
    Busca un estudiante por su número de legajo y muestra su información si se encuentra.

    Parámetros:
    legajos (list): Lista de legajos de los estudiantes.
    nombres (list): Lista de nombres de los estudiantes.
    generos (list): Lista de géneros de los estudiantes.
    nota_p1 (list): Lista de notas del primer parcial.
    nota_p2 (list): Lista de notas del segundo parcial.
    promedios (list): Lista de promedios de los estudiantes.

    Retorna:
    None: Esta función solo busca y muestra la información del estudiante si se encuentra, no retorna ningún valor.
    """
    legajo_buscado = input("\nIngrese el número de legajo a buscar: ")
    
    if validar_legajo(legajo_buscado) == False:
        print("Legajo no válido.") # Si el legajo ingresado no es válido, termina la función sin hacer nada más
        return

    legajo_buscado_entero = int(legajo_buscado)
    encontrado = False
    
    for i in range(len(legajos)): # Recorre la lista de legajos para buscar el que coincida con el ingresado por el usuario
        if legajos[i] == legajo_buscado_entero:
            print("\n¡Estudiante encontrado!")
            if len(promedios) == 0: 
                prom = None
            else:
                prom = promedios[i]
                
            mostrar_un_elemento(legajos[i], nombres[i], generos[i], nota_p1[i], nota_p2[i], prom) # Muestra el estudiante encontrado, con o sin promedio
            encontrado = True
            break
            
    if encontrado == False:
        print("No se encontró ningún estudiante con ese legajo.")


# ==========================================
#  SIMULADOR DE CARGA 
# ==========================================

def simular_carga_automatica(legajos, nombres, generos, nota_p1, nota_p2): # Lista de datos predefinidos
    """
    Simula la carga automática de 30 estudiantes con datos predefinidos.

    Parámetros:
    legajos (list): Lista donde se almacenarán los legajos de los estudiantes.
    nombres (list): Lista donde se almacenarán los nombres de los estudiantes.
    generos (list): Lista donde se almacenarán los géneros de los estudiantes.
    nota_p1 (list): Lista donde se almacenarán las notas del primer parcial.
    nota_p2 (list): Lista donde se almacenarán las notas del segundo parcial.
    
    Retorna:
    None: Esta función solo carga los datos en las listas proporcionadas y no retorna ningún valor.
    """
    lista_l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102]
    lista_n = ["Gomez Ana", "Perez Juan", "Lopez Luis", "Diaz Maria", "Paz Jose", "Soto Ines", "Rios Blas", "Vega Rosa", "Cruz Omar", "Roca Hugo",
               "Gomez Elsa", "Perez Raul", "Lopez Alan", "Diaz Sara", "Paz Abel", "Soto Cleo", "Rios Kurt", "Vega Nora", "Cruz Olga", "Roca Axel",
               "Gomez Olga", "Perez Enzo", "Lopez Lola", "Diaz Rene", "Paz Luis", "Soto Jani", "Rios Paul", "Vega Dora", "Cruz Alex", "Roca Yani"]
    lista_g = ["F", "M", "M", "F", "M", "F", "M", "X", "M", "M", "F", "M", "M", "F", "X", "F", "M", "F", "M", "X", "F", "M", "F", "M", "M", "F", "M", "F", "M", "F"]
    lista_1 = [8, 4, 7, 10, 5, 6, 9, 2, 7, 8, 4, 6, 7, 5, 8, 9, 3, 4, 10, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 10]
    lista_2 = [9, 5, 8, 10, 6, 7, 8, 4, 8, 9, 5, 7, 6, 6, 7, 9, 4, 5, 9, 7, 8, 7, 9, 5, 6, 8, 7, 9, 8, 10]

    # Recorre por índice y asigna directamente en el espacio ya reservado
    for i in range(30):
        legajos[i] = lista_l[i]
        nombres[i] = lista_n[i]
        generos[i] = lista_g[i]
        nota_p1[i] = lista_1[i]
        nota_p2[i] = lista_2[i]
    print("\n Se han cargado 30 estudiantes automáticamente.")