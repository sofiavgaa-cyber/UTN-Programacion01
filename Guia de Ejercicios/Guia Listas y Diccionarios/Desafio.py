from datetime import datetime

# -----------------------------
# 📌 DATOS DE EJEMPLO
# -----------------------------
videos = [
    {
        "codigo": "LG001",
        "titulo": "Shallow",
        "colaboradores": ["Bradley Cooper", "Lukas Nelson"],
        "vistas": "1900000000",
        "duracion": "3:37",
        "link": "https://www.youtube.com/watch?v=bo_efYh",
        "fecha": "2018-09-27"
    },
    {
        "codigo": "LG002",
        "titulo": "Bad Romance",
        "colaboradores": [],
        "vistas": "1600000000",
        "duracion": "4:54",
        "link": "https://www.youtube.com/watch?v=qrO4YZeyl0I",
        "fecha": "2009-11-10"
    },
    {
        "codigo": "LG003",
        "titulo": "Rain On Me",
        "colaboradores": ["Ariana Grande"],
        "vistas": "1200000000",
        "duracion": "3:03",
        "link": "https://www.youtube.com/watch?v=AoAm4om0wTs",
        "fecha": "2020-05-22"
    }
]

# -----------------------------
# 🔧 NORMALIZACIÓN
# -----------------------------
def convertir_duracion(duracion_str):
    minutos, segundos = duracion_str.split(":")
    return int(minutos) * 60 + int(segundos)

def normalizar_datos(lista):
    for video in lista:
        video["vistas"] = int(video["vistas"])
        video["duracion"] = convertir_duracion(video["duracion"])
        video["fecha"] = datetime.strptime(video["fecha"], "%Y-%m-%d")
    return lista

# -----------------------------
# 📋 MOSTRAR LISTA
# -----------------------------
def mostrar_lista(lista):
    print("\n📌 LISTA DE VIDEOS")
    print("-" * 50)
    for v in lista:
        print(f"{v['titulo']} | {v['duracion']} seg")

# -----------------------------
# 🔃 ORDENAR POR DURACIÓN
# -----------------------------
def ordenar_por_duracion(lista):
    return sorted(lista, key=lambda x: x["duracion"], reverse=True)

# -----------------------------
# 📊 PROMEDIO DE VISTAS
# -----------------------------
def promedio_vistas(lista):
    total = sum(v["vistas"] for v in lista)
    return total / len(lista) / 1_000_000

# -----------------------------
# 🔝 MÁXIMO Y MÍNIMO
# -----------------------------
def max_vistas(lista):
    maximo = max(lista, key=lambda x: x["vistas"])
    return [v for v in lista if v["vistas"] == maximo["vistas"]]

def min_vistas(lista):
    minimo = min(lista, key=lambda x: x["vistas"])
    return [v for v in lista if v["vistas"] == minimo["vistas"]]

# -----------------------------
# 🔎 BÚSQUEDA POR CÓDIGO
# -----------------------------
def buscar_por_codigo(lista, codigo):
    for v in lista:
        if v["codigo"] == codigo:
            return v
    return None

# -----------------------------
# 🎤 FILTRAR POR COLABORADOR
# -----------------------------
def filtrar_por_colaborador(lista, nombre):
    return [v for v in lista if nombre in v["colaboradores"]]

# -----------------------------
# 📅 FILTRAR POR MES
# -----------------------------
def filtrar_por_mes(lista, mes):
    return [v for v in lista if v["fecha"].month == mes]

# -----------------------------
# 🎮 MENÚ
# -----------------------------
def menu():
    print("""
🎵 MENU LADY GAGA
1. Mostrar lista
2. Ordenar por duración
3. Promedio de vistas (millones)
4. Máxima reproducción
5. Mínima reproducción
6. Buscar por código
7. Filtrar por colaborador
8. Filtrar por mes
9. Salir
""")

# -----------------------------
# 🚀 PROGRAMA PRINCIPAL
# -----------------------------
normalizar_datos(videos)

while True:
    menu()
    opcion = input("👉 Elegir opción: ")

    if opcion == "1":
        mostrar_lista(videos)

    elif opcion == "2":
        ordenados = ordenar_por_duracion(videos)
        mostrar_lista(ordenados)

    elif opcion == "3":
        print(f"📊 Promedio de vistas: {promedio_vistas(videos):.2f} millones")

    elif opcion == "4":
        print("🔝 Máxima reproducción:")
        for v in max_vistas(videos):
            print(v["titulo"], v["vistas"])

    elif opcion == "5":
        print("📉 Mínima reproducción:")
        for v in min_vistas(videos):
            print(v["titulo"], v["vistas"])

    elif opcion == "6":
        codigo = input("Ingrese código: ")
        v = buscar_por_codigo(videos, codigo)
        print(v if v else "❌ No encontrado")

    elif opcion == "7":
        nombre = input("Colaborador: ")
        resultados = filtrar_por_colaborador(videos, nombre)
        for v in resultados:
            print(v["titulo"])

    elif opcion == "8":
        mes = int(input("Mes (1-12): "))
        resultados = filtrar_por_mes(videos, mes)
        for v in resultados:
            print(v["titulo"])

    elif opcion == "9":
        print("👋 Saliendo...")
        break

    else:
        print("❌ Opción inválida")