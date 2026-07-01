from Funciones import *

def menu():
    lista_estudiantes = []
    datos_cargados = False  # Validacion de Nota 0

    while True:
        print("\n================ MENU DE OPCIONES ================")
        print("1 - Leer archivo data_sp.json")
        print("2 - Cargar estudiante manualmente")
        print("3 - Mostrar todos los estudiantes")
        print("4 - Calcular promedios")
        print("5 - Mostrar estudiantes ordenados por promedio (DESC)")
        print("6 - Mostrar estudiante(s) con mayor promedio")
        print("7 - Buscar estudiante por Legajo")
        print("8 - Exportar lista a JSON")
        print("9 - Exportar lista a CSV")
        print("10 - Salir")
        print("==================================================")
        
        opcion = input("Seleccione una opción: ")

        # Validación de Nota 0: Forzar carga antes de operar cualquier otra opción (excepto salir)
        if opcion in ["3", "4", "5", "6", "7", "8", "9"] and not datos_cargados:
            print("⚠️ Error (Nota 0): No se puede acceder a esta opción sin antes haber cargado datos (Opción 1 o 2).")
            continue

        if opcion == "1":
            # Usamos una lista auxiliar para no pisar la anterior si el archivo falla
            lista_auxiliar = leer_json("data_sp_actualizado.json")
            if lista_auxiliar:
                lista_estudiantes = lista_auxiliar
                datos_cargados = True
                print(f"Se cargaron {len(lista_estudiantes)} estudiantes desde el JSON.")
                
        elif opcion == "2":
            nuevo_estudiante = cargar_estudiante_manual()
            lista_estudiantes.append(nuevo_estudiante)
            datos_cargados = True
            print("Estudiante agregado con éxito a la lista.")
            
        elif opcion == "3":
            mostrar_estudiantes(lista_estudiantes)
            
        elif opcion == "4":
            calcular_promedios(lista_estudiantes)
            
        elif opcion == "5":
            lista_ordenada = ordenar_por_promedio_desc(lista_estudiantes)
            print("\n--- Estudiantes Ordenados por Promedio (Descendente) ---")
            mostrar_estudiantes(lista_ordenada)
            
        elif opcion == "6":
            mostrar_mayor_promedio(lista_estudiantes)
            
        elif opcion == "7":
            buscar_por_legajo(lista_estudiantes)
            
        elif opcion == "8":
            exportar_a_json(lista_estudiantes, "data_sp_actualizado.json")
            
        elif opcion == "9":
            exportar_a_csv(lista_estudiantes, "data_sp.csv")
            
        elif opcion == "10":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()