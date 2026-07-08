import FuncionesSP

def menu():
    lista_estudiantes = []
    datos_cargados = False # Bandera para controlar la Nota 0
    
    while True:
        print("\n================ MENU DE OPCIONES ================")
        print("1 - Leer archivo JSON (data_sp.json)")
        print("2 - Cargar datos de estudiante manualmente")
        print("3 - Mostrar todos los estudiantes")
        print("4 - Calcular promedio de estudiantes")
        print("5 - Mostrar ordenados por promedio DESC")
        print("6 - Mostrar estudiante(s) con mayor promedio")
        print("7 - Buscar estudiante por Legajo")
        print("8 - Exportar lista a JSON")
        print("9 - Exportar lista a CSV")
        print("10 - Salir del programa")
        print("==================================================")
        
        opcion = input("Seleccione una opción (1-10): ")
        
        if opcion == "1":
            lista_estudiantes = FuncionesSP.leer_json("data_sp.json")
            datos_cargados = True # Ya tenemos datos en memoria
            
        elif opcion == "2":
            FuncionesSP.cargar_estudiante_manual(lista_estudiantes)
            datos_cargados = True # Al menos hay un dato cargado de forma manual
            
        elif opcion in ["3", "4", "5", "6", "7", "8", "9"]:
            # Validación de Nota 0: Bloquear accesos si no se ha llamado antes al punto 1 o 2
            if not datos_cargados or len(lista_estudiantes) == 0:
                print("Error (Nota 0): No puede acceder a esta opción sin antes haber cargado datos (Opción 1 o 2).")
            else:
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

        elif opcion == "10":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Ingrese un número entre 1 y 10.")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    menu()