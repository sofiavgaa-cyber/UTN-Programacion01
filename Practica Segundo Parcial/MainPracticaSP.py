"""
Archivo principal de ejecución (Orquestador del Menú).
"""
from FuncionesSP import (
    opcion_1_leer_json,
    opcion_2_cargar_estudiante,
    opcion_3_mostrar_todos,
    opcion_4_calcular_promedios,
    opcion_5_ordenar_por_promedio_desc,
    opcion_6_mostrar_mayor_promedio,
    opcion_7_buscar_por_legajo,
    opcion_8_exportar_json,
    opcion_9_exportar_csv
)

def main():
    # Lista en memoria que contendrá los diccionarios de estudiantes
    lista_estudiantes = []
    # Bandera para validar la carga previa de datos (Nota 0)
    datos_cargados = False

    while True:
        print("\n=========================================")
        print("          MENÚ DE OPCIONES")
        print("=========================================")
        print("1. Leer archivo data_pp.json")
        print("2. Realizar carga manual de estudiante")
        print("3. Mostrar todos los estudiantes")
        print("4. Calcular promedios")
        print("5. Mostrar estudiantes ordenados por promedio (DESC)")
        print("6. Mostrar estudiante(s) con mayor promedio")
        print("7. Buscar estudiante por legajo")
        print("8. Exportar lista a JSON (data_sp.json)")
        print("9. Exportar lista a CSV (data_sp.csv)")
        print("10. Salir")
        print("=========================================")
        
        opcion = input("Seleccione una opción (1-10): ").strip()

        if opcion == "1":
            lista_estudiantes = opcion_1_leer_json("data_pp.json")
            if lista_estudiantes:
                datos_cargados = True
        
        elif opcion == "2":
            opcion_2_cargar_estudiante(lista_estudiantes)
            datos_cargados = True  # La carga manual también activa la validez de los datos
            
        elif opcion in ["3", "4", "5", "6", "7", "8", "9"]:
            # Validación de la Nota 0
            if not datos_cargados:
                print("\n[ALERTA] Acceso denegado. Primero debe cargar datos (Opción 1 o 2).")
                continue
            
            if opcion == "3":
                opcion_3_mostrar_todos(lista_estudiantes)
            elif opcion == "4":
                opcion_4_calcular_promedios(lista_estudiantes)
            elif opcion == "5":
                opcion_5_ordenar_por_promedio_desc(lista_estudiantes)
            elif opcion == "6":
                opcion_6_mostrar_mayor_promedio(lista_estudiantes)
            elif opcion == "7":
                opcion_7_buscar_por_legajo(lista_estudiantes)
            elif opcion == "8":
                opcion_8_exportar_json(lista_estudiantes, "data_sp.json")
            elif opcion == "9":
                opcion_9_exportar_csv(lista_estudiantes, "data_sp.csv")
                
        elif opcion == "10":
            print("\nGracias por utilizar el sistema. ¡Éxitos en el parcial!")
            break
        else:
            print("\n[ERROR] Opción no válida. Intente de nuevo del 1 al 10.")

if __name__ == "__main__":
    main()