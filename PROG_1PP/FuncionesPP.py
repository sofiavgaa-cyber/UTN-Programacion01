# ==========================================
#  VALIDACIONES 
# ==========================================

def validar_legajo(legajo):
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
    if nombre == "": # Valida que no este vacío
        return False
        
    # Verifica que sean solo letras o espacios
    for caracter in nombre:
        # Chequeamos si NO es una letra (tanto minúscula como mayúscula) y tampoco un espacio
        if not ((caracter >= "a" and caracter <= "z") or (caracter >= "A" and caracter <= "Z") or caracter == " "):
            return False
            
    return True

def validar_genero(genero):
    # Convierte lo que ingresó el usuario a mayúsculas
    genero = genero.upper()

    # Solo acepta las letras exactas 
    if genero == "F" or genero == "M" or genero == "X":
        return True
    else:
        return False

def validar_nota(nota):
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

def mostrar_un_elemento(legajo, nombre, genero, n1, n2, promedio): #Muestra un solo estudiante, con o sin promedio
    if promedio == None: # La función recibe None si no hay promedio calculado, para no mostrarlo
        print("Legajo:", legajo, "| Nombre:", nombre, "| Género:", genero, "| Parcial 1:", n1, "| Parcial 2:", n2)
    else: # Si hay promedio, lo muestra
        print("Legajo:", legajo, "| Nombre:", nombre, "| Género:", genero, "| Parcial 1:", n1, "| Parcial 2:", n2, "| Promedio:", promedio)

def recorrer_y_mostrar_elementos(legajos, nombres, generos, nota_p1, nota_p2, promedios): #Muestra todos los estudiantes, con o sin promedio
    print("\n--- LISTA DE ESTUDIANTES ---")
    cantidad = len(legajos) # Averigua cuántos elementos hay en la lista de legajos (todas las listas tienen la misma cantidad)
    for i in range(cantidad): 
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
    # Vacia la lista de promedios antes de calcularlos nuevamente 
    del promedios[:] 
    for i in range(len(nota_p1)):
        resultado = (nota_p1[i] + nota_p2[i]) / 2
        promedios.append(resultado) # Guarda el promedio en la lista de promedios
    print("\nPromedios calculados correctamente.")


# ==========================================
#  ORDENAMIENTO Y BÚSQUEDA
# ==========================================

def ordenar_por_promedio_descendente(legajos, nombres, generos, nota_p1, nota_p2, promedios):
    n = len(promedios) # Guarda la cantidad de elementos en la lista de promedios para usarla en los bucles
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if promedios[j] < promedios[j + 1]:
                
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
    nota_mas_alta = promedios[0] # Inicia la variable con el primer promedio de la lista
    for p in promedios:
        if p > nota_mas_alta: # Si encuentra un promedio mayor, lo guarda en la variable
            nota_mas_alta = p
            
    print("\n--- Estudiante/s con el Mayor Promedio (", nota_mas_alta, ") ---")
    for i in range(len(promedios)):
        if promedios[i] == nota_mas_alta: # Muestra todos los estudiantes que tengan el promedio más alto
            mostrar_un_elemento(legajos[i], nombres[i], generos[i], nota_p1[i], nota_p2[i], promedios[i])

def buscar_estudiante_por_legajo(legajos, nombres, generos, nota_p1, nota_p2, promedios):
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
# SIMULADOR DE CARGA 
# ==========================================
def simular_carga_automatica(legajos, nombres, generos, nota_p1, nota_p2):
    # Lista de datos predefinidos   
    lista_l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102]
    lista_n = ["Gomez Ana", "Perez Juan", "Lopez Luis", "Diaz Maria", "Paz Jose", "Soto Ines", "Rios Blas", "Vega Rosa", "Cruz Omar", "Roca Hugo",
               "Gomez Elsa", "Perez Raul", "Lopez Alan", "Diaz Sara", "Paz Abel", "Soto Cleo", "Rios Kurt", "Vega Nora", "Cruz Olga", "Roca Axel",
               "Gomez Olga", "Perez Enzo", "Lopez Lola", "Diaz Rene", "Paz Luis", "Soto Jani", "Rios Paul", "Vega Dora", "Cruz Alex", "Roca Yani"]
    lista_g = ["F", "M", "M", "F", "M", "F", "M", "X", "M", "M", "F", "M", "M", "F", "X", "F", "M", "F", "M", "X", "F", "M", "F", "M", "M", "F", "M", "F", "M", "F"]
    lista_1 = [8, 4, 7, 10, 5, 6, 9, 2, 7, 8, 4, 6, 7, 5, 8, 9, 3, 4, 10, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 10]
    lista_2 = [9, 5, 8, 10, 6, 7, 8, 4, 8, 9, 5, 7, 6, 6, 7, 9, 4, 5, 9, 7, 8, 7, 9, 5, 6, 8, 7, 9, 8, 10]

    # Pasamos los datos individuales usando bucles con .append()
    for item in lista_l: legajos.append(item) # .append agrega un elemento al final de la lista
    for item in lista_n: nombres.append(item)
    for item in lista_g: generos.append(item)
    for item in lista_1: nota_p1.append(item)
    for item in lista_2: nota_p2.append(item)
    print("\n Se han cargado 30 estudiantes automáticamente.")