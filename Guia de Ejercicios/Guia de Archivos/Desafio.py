import csv
import json
from datetime import datetime
from typing import List, Dict, Any


# =========================
# 📥 LECTURA CSV
# =========================
def leer_csv(ruta: str) -> List[Dict[str, Any]]:
    try:
        with open(ruta, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("❌ Archivo no encontrado")
        return []


# =========================
# 🧼 NORMALIZACIÓN
# =========================
def normalizar_datos(datos: List[Dict[str, str]]) -> List[Dict[str, Any]]:
    normalizados = []

    for fila in datos:
        try:
            titulo = fila["titulo"].strip()

            colaboradores = [
                c.strip() for c in fila["colaboradores"].split(",")
                if c.strip()
            ]

            vistas = int(fila["vistas"])

            # convertir duración mm:ss → segundos
            min_, seg = fila["duracion"].split(":")
            duracion = int(min_) * 60 + int(seg)

            link = fila["link"].strip()

            fecha = datetime.strptime(fila["fecha"], "%Y-%m-%d").date()

            normalizados.append({
                "codigo": fila["codigo"],
                "titulo": titulo,
                "colaboradores": colaboradores,
                "vistas": vistas,
                "duracion": duracion,
                "link": link,
                "fecha": fecha
            })

        except Exception as e:
            print(f"⚠️ Error en fila {fila}: {e}")

    return normalizados


# =========================
# 📤 GUARDAR JSON
# =========================
def guardar_json(datos: List[Dict], ruta: str):
    with open(ruta, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, default=str)


# =========================
# 📤 GUARDAR CSV POR COLABORADOR
# =========================
def guardar_colaborador_csv(datos: List[Dict], nombre: str, ruta: str):
    filtrados = [
        c for c in datos if nombre.lower() in
        [col.lower() for col in c["colaboradores"]]
    ]

    with open(ruta, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["codigo", "titulo", "vistas", "duracion"])

        for c in filtrados:
            writer.writerow([c["codigo"], c["titulo"], c["vistas"], c["duracion"]])


# =========================
# 📋 MOSTRAR LISTA
# =========================
def mostrar_lista(datos: List[Dict]):
    print("\n🎵 LISTA DE TEMAS")
    print("-" * 50)
    for c in datos:
        print(f"{c['titulo']} | {c['duracion']} seg")


# =========================
# 🔄 ORDENAR POR DURACIÓN
# =========================
def ordenar_por_duracion(datos: List[Dict]) -> List[Dict]:
    return sorted(datos, key=lambda x: x["duracion"], reverse=True)


# =========================
# 📊 PROMEDIO VISTAS
# =========================
def promedio_vistas(datos: List[Dict]) -> float:
    total = sum(c["vistas"] for c in datos)
    return total / len(datos) / 1_000_000


# =========================
# 🔝 MÁXIMO / MÍNIMO
# =========================
def max_vistas(datos: List[Dict]) -> List[Dict]:
    maximo = max(c["vistas"] for c in datos)
    return [c for c in datos if c["vistas"] == maximo]


def min_vistas(datos: List[Dict]) -> List[Dict]:
    minimo = min(c["vistas"] for c in datos)
    return [c for c in datos if c["vistas"] == minimo]


# =========================
# 🔎 BÚSQUEDA POR CÓDIGO
# =========================
def buscar_por_codigo(datos: List[Dict], codigo: str):
    for c in datos:
        if c["codigo"] == codigo:
            return c
    return None


# =========================
# 👥 POR COLABORADOR
# =========================
def filtrar_por_colaborador(datos: List[Dict], nombre: str) -> List[Dict]:
    return [
        c for c in datos
        if nombre.lower() in [col.lower() for col in c["colaboradores"]]
    ]


# =========================
# 📅 POR MES
# =========================
def filtrar_por_mes(datos: List[Dict], mes: int) -> List[Dict]:
    return [c for c in datos if c["fecha"].month == mes]


# =========================
# 📌 MENÚ
# =========================
def menu():
    print("""
🎵 MENÚ - LADY GAGA PLAYLIST
1. Mostrar lista
2. Ordenar por duración
3. Promedio de vistas
4. Máxima reproducción
5. Mínima reproducción
6. Buscar por código
7. Listar por colaborador (y guardar CSV)
8. Listar por mes
9. Guardar JSON
10. Salir
""")


# =========================
# 🚀 MAIN
# =========================
def main():
    datos_raw = leer_csv("canciones.csv")
    datos = normalizar_datos(datos_raw)

    while True:
        menu()
        opcion = input("👉 Opción: ")

        if opcion == "1":
            mostrar_lista(datos)

        elif opcion == "2":
            ordenados = ordenar_por_duracion(datos)
            mostrar_lista(ordenados)

        elif opcion == "3":
            print(f"📊 Promedio: {promedio_vistas(datos):.2f} millones")

        elif opcion == "4":
            print(max_vistas(datos))

        elif opcion == "5":
            print(min_vistas(datos))

        elif opcion == "6":
            codigo = input("Código: ")
            print(buscar_por_codigo(datos, codigo))

        elif opcion == "7":
            nombre = input("Colaborador: ")
            res = filtrar_por_colaborador(datos, nombre)
            guardar_colaborador_csv(res, nombre, "colaboradores.csv")
            print(res)

        elif opcion == "8":
            mes = int(input("Mes (1-12): "))
            print(filtrar_por_mes(datos, mes))

        elif opcion == "9":
            guardar_json(datos, "canciones.json")
            print("✅ JSON guardado")

        elif opcion == "10":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    main()