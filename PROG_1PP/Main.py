import Funciones

def menu_principal():
    lista_legajos = []
    lista_nombres = []
    lista_generos = []
    lista_notas_p1 = []
    lista_notas_p2 = []
    lista_promedios = []
    
    ya_hay_datos = False

    while True:
        print("=== MENÚ DE ESTUDIANTES ===")
        print("1 - Cargar datos manualmente (30 alumnos)")
        print("2 - Mostrar todos los alumnos")
        print("3 - Calcular promedios")
        print("4 - Ordenar y mostrar por promedio (Descendente)")
        print("5 - Mostrar estudiante/s con mayor promedio")
        print("6 - Buscar estudiante por legajo")
        print("7 - Salir del programa")
        print("0 - Carga automática express (Para no escribir a mano)")
        
        opcion = input("Elija una opción (1-7 o 0): ")
        
        # Validación con bandera para no entrar a las opciones sin datos (Nota 1)
        if opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":
            if ya_hay_datos == False:
                print("\n[ERROR] No puede usar esta opción sin cargar datos primero con la opción 1 o 0.\n")
                continue 
                
        if opcion == "1":
            # Limpiamos reasignando a listas vacías
            lista_legajos = []
            lista_nombres = []
            lista_generos = []
            lista_notas_p1 = []
            lista_notas_p2 = []
            lista_promedios = []

            # Carga manual alumno por alumno con las funciones correspondientes
            for i in range(30):
                print("\nCargando datos del estudiante número", i + 1)
                
                legajo = input("Ingrese Legajo: ")
                while Funciones.validar_legajo(legajo) == False:
                    print("Error: El legajo debe ser un número entero mayor a 0.")
                    legajo = input("Ingrese Legajo nuevamente: ")
                lista_legajos.append(int(legajo))
                
                nombre = input("Ingrese Apellido y Nombre: ")
                while Funciones.validar_nombre(nombre) == False:
                    print("Error: El nombre debe contener solo letras y espacios.")
                    nombre = input("Ingrese Apellido y Nombre nuevamente: ")
                lista_nombres.append(nombre)
                
                genero = input("Ingrese Género (F / M / X): ")
                # En lugar de usar .upper(), validamos pidiendo que sea exacto en mayúscula
                while Funciones.validar_genero(genero) == False:
                    print("Error: Opciones válidas F, M o X (Debe ser en Mayúscula).")
                    genero = input("Ingrese Género nuevamente: ")
                lista_generos.append(genero)
                
                n1 = input("Ingrese Nota del Primer Parcial: ")
                while Funciones.validar_nota(n1) == False:
                    print("Error: La nota debe ser un número entero entre 1 y 10.")
                    n1 = input("Ingrese Nota 1 nuevamente: ")
                lista_notas_p1.append(int(n1))
                
                n2 = input("Ingrese Nota del Segundo Parcial: ")
                while Funciones.validar_nota(n2) == False:
                    print("Error: La nota debe ser un número entero entre 1 y 10.")
                    n2 = input("Ingrese Nota 2 nuevamente: ")
                lista_notas_p2.append(int(n2))

            print("\n¡Se cargaron los 30 alumnos con éxito!")
            ya_hay_datos = True 
            
        elif opcion == "2":
            Funciones.recorrer_y_mostrar_elementos(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
            
        elif opcion == "3":
            Funciones.calcular_promedios(lista_notas_p1, lista_notas_p2, lista_promedios)
            
        elif opcion == "4":
            if len(lista_promedios) == 0:
                print("\n[ERROR] Primero debe calcular los promedios con la opción 3.\n")
            else:
                Funciones.ordenar_por_promedio_descendente(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
                Funciones.recorrer_y_mostrar_elementos(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
                
        elif opcion == "5":
            if len(lista_promedios) == 0:
                print("\n[ERROR] Primero debe calcular los promedios con la opción 3.\n")
            else:
                Funciones.mostrar_estudiantes_con_mayor_promedio(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
                
        elif opcion == "6":
            Funciones.buscar_estudiante_por_legajo(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2, lista_promedios)
            
        elif opcion == "7":
            print("\n¡Gracias por usar el sistema! Programa finalizado.")
            break 
            
        elif opcion == "0":
            lista_legajos = []; lista_nombres = []; lista_generos = []; lista_notas_p1 = []; lista_notas_p2 = []; lista_promedios = []
            Funciones.simular_carga_automatica(lista_legajos, lista_nombres, lista_generos, lista_notas_p1, lista_notas_p2)
            ya_hay_datos = True 
        else:
            print("\nOpción incorrecta. Por favor elija un número del menú.\n")

# Iniciamos el menú
menu_principal()