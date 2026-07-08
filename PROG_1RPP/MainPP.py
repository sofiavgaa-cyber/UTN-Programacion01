import FuncionesPP

def menu_principal(): # Inicia las 6 listas vacías y la bandera 
    """
    Inicializa las 6 listas paralelas de datos globales y la bandera de control de carga.
    Despliega un menú interactivo por consola que procesa las opciones elegidas por el usuario, 
    gestionando la lógica principal del sistema.
    """
    lista_legajos = [None] * 30 # Inicia las listas con capacidad para 30 elementos
    lista_nombres = [None] * 30
    lista_generos = [None] * 30
    lista_notas_p1 = [None] * 30
    lista_notas_p2 = [None] * 30
    lista_promedios = [None] * 30
    
    ya_hay_datos = False # Arranca en False porque las listas están vacías

    while True: # Bucle infinito hasta que el usuario elija salir
        print("=== MENÚ DE ESTUDIANTES ===")
        print("1 - Cargar datos manualmente")
        print("2 - Mostrar todos los alumnos")
        print("3 - Calcular promedios")
        print("4 - Ordenar y mostrar por promedio (Descendente)")
        print("5 - Mostrar estudiante/s con mayor promedio")
        print("6 - Buscar estudiante por legajo")
        print("7 - Salir del programa")
        print("0 - Carga automática")
        
        opcion = input("Elija una opción (1-7 o 0): ")
        
        # Validación con bandera para no entrar a las opciones sin datos
        if opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":
            if ya_hay_datos == False:
                print("\n No puede usar esta opción sin cargar datos primero con la opción 1 o 0.\n")
                continue 
                
        if opcion == "1":
            # Asegura que las listas estén vacías
            lista_legajos = [None] * 30
            lista_nombres = [None] * 30
            lista_generos = [None] * 30
            lista_notas_p1 = [None] * 30
            lista_notas_p2 = [None] * 30
            lista_promedios = [None] * 30

            # Hace un bucle para cargar 30 estudiantes
            for i in range(30):
                print("\nCargando datos del estudiante número", i + 1)
                
                legajo = input("Ingrese Legajo: ")
                while FuncionesPP.validar_legajo(legajo) == False:
                    print("El legajo debe ser un número entero mayor a 0.")
                    legajo = input("Ingrese Legajo nuevamente: ")
                lista_legajos[i] = int(legajo) # Asignación directa por índice
                
                nombre = input("Ingrese Apellido y Nombre: ")
                while FuncionesPP.validar_nombre(nombre) == False:
                    print("El nombre debe contener solo letras y espacios.")
                    nombre = input("Ingrese Apellido y Nombre nuevamente: ")
                lista_nombres[i] = nombre 
                
                genero = input("Ingrese Género (F / M / X): ")
                # Validamos pidiendo que sea exacto en mayúscula
                while FuncionesPP.validar_genero(genero) == False:
                    print("Opciones válidas F, M o X.")
                    genero = input("Ingrese Género nuevamente: ")
                lista_generos[i] = genero
                
                n1 = input("Ingrese Nota del Primer Parcial: ")
                while FuncionesPP.validar_nota(n1) == False:
                    print("La nota debe ser un número entero entre 1 y 10.")
                    n1 = input("Ingrese Nota 1 nuevamente: ")
                lista_notas_p1[i] = int(n1)
                
                n2 = input("Ingrese Nota del Segundo Parcial: ")
                while FuncionesPP.validar_nota(n2) == False:
                    print("La nota debe ser un número entero entre 1 y 10.")
                    n2 = input("Ingrese Nota 2 nuevamente: ")
                lista_notas_p2[i] = int(n2)

            print("\n¡Se cargaron los 30 alumnos con éxito!")
            ya_hay_datos = True # Pone la bandera en True para permitir el uso de las demás opciones
            
        elif opcion == "2":
            FuncionesPP.recorrer_y_mostrar_elementos(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
            
        elif opcion == "3":
            FuncionesPP.calcular_promedios(lista_notas_p1, lista_notas_p2, lista_promedios)
            
        elif opcion == "4":
            if len(lista_promedios) == 0:
                print("\n Primero debe calcular los promedios con la opción 3.\n")
            else:
                FuncionesPP.ordenar_por_promedio_descendente(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
                FuncionesPP.recorrer_y_mostrar_elementos(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
                
        elif opcion == "5":
            if len(lista_promedios) == 0:
                print("\n Primero debe calcular los promedios con la opción 3.\n")
            else:
                FuncionesPP.mostrar_estudiantes_con_mayor_promedio(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
                
        elif opcion == "6":
            FuncionesPP.buscar_estudiante_por_legajo(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
            
        elif opcion == "7":
            print("\n Programa finalizado.")
            break 
            
        elif opcion == "0":
            lista_legajos = [None] * 30
            lista_nombres = [None] * 30
            lista_generos = [None] * 30
            lista_notas_p1 = [None] * 30
            lista_notas_p2 = [None] * 30
            lista_promedios = [None] * 30 
        else:
            print("\n Opción incorrecta. Por favor elija un número del menú.\n")

# Iniciamos el menú
menu_principal()