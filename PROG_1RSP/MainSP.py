import FuncionesSP

def menu():
    lista_estudiantes = []
    datos_cargados = False  # Bandera de control
    
    while True:
        print("\n================ MENU DE OPCIONES ================")
        print("1 - Leer archivo JSON")
        print("2 - Cargar datos de estudiante manualmente")
        print("3 - Mostrar todos los estudiantes")
        print("4 - Calcular promedio de estudiantes")
        print("5 - Mostrar estudiantes ordenados por promedio DESC")
        print("6 - Mostrar estudiantes con mayor promedio")
        print("7 - Buscar estudiante por Legajo")
        print("8 - Exportar lista a JSON")
        print("9 - Exportar lista a CSV")
        print("0 - Salir del programa")
        print("==================================================")
        
        opcion = input("Seleccione una opción (0-9): ")
        
        if opcion == "1":
            # Leemos el diccionario del archivo JSON y lo almacenamos en una variable
            diccionario_archivo = FuncionesSP.leer_json("data_sp.json")
            
            # Extraemos la lista real de estudiantes usando la clave 'estudiantes'
            lista_estudiantes = diccionario_archivo["estudiantes"]
            datos_cargados = True
            
        elif opcion == "2": # Carga manual de datos
            lista_estudiantes = FuncionesSP.cargar_estudiantes(lista_estudiantes)
            datos_cargados = True
            
        elif opcion in ["3", "4", "5", "6", "7", "8", "9"]: 
            # Valida que haya datos cargados antes de ejecutar estas opciones
            if not datos_cargados or len(lista_estudiantes) == 0: 
                # Si no hay datos cargados, muestra un mensaje de error
                print("No puede acceder a esta opción sin antes haber cargado datos.")
            else: # Si hay datos cargados, ejecuta la opción correspondiente
                if opcion == "3":
                    FuncionesSP.mostrar_todos_los_elementos(lista_estudiantes)
                elif opcion == "4":
                    FuncionesSP.calcular_todos_los_promedios(lista_estudiantes)
                elif opcion == "5":
                    FuncionesSP.ordenar_estudiantes_por_promedio_desc(lista_estudiantes)
                elif opcion == "6":
                    FuncionesSP.mostrar_mayor_promedio(lista_estudiantes)
                elif opcion == "7":
                    FuncionesSP.buscar_por_legajo(lista_estudiantes)
                elif opcion == "8":
                    FuncionesSP.exportar_json("data_sp_procesado.json", lista_estudiantes)
                elif opcion == "9":
                    FuncionesSP.exportar_csv("data_sp.csv", lista_estudiantes)

        elif opcion == "0": 
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Ingrese un número entre 0 y 9.")

menu()