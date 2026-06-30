def obtener_colaboradores(titulo: str) -> list[str]:
    """
    Devuelve la lista de colaboradores desde un título tipo:
    "Artista1 | Artista2 - Cancion"
    """
    if "-" not in titulo:
        return []

    parte_artistas = titulo.split("-")[0].strip()

    colaboradores = []
    for artista in parte_artistas.split("|"):
        nombre = artista.strip()
        if nombre != "":
            colaboradores.append(nombre)

    return colaboradores

def obtener_nombre_tema(titulo: str) -> str:
    """
    Elimina los colaboradores y devuelve el nombre del tema.
    """
    if "-" not in titulo:
        return titulo.strip()

    return titulo.split("-")[1].strip()

def convertir_vistas_numerico(vistas: str) -> int:
    """
    Convierte '1900 millones' → 1900000000
    """
    vistas = vistas.lower().replace("millones", "").strip()

    numero = int(vistas)

    return numero * 1_000_000

def convertir_duracion_numerico(duracion: str) -> int:
    """
    Convierte "3:37" → 217 segundos
    """
    if ":" not in duracion:
        return 0

    minutos, segundos = duracion.split(":")

    return int(minutos) * 60 + int(segundos)

def obtener_codigo(url: str) -> str:
    """
    Extrae el código de un video de YouTube.
    """
    if "v=" not in url:
        return ""

    partes = url.split("v=")
    codigo = partes[1]

    # por si hay parámetros extra
    if "&" in codigo:
        codigo = codigo.split("&")[0]

    return codigo

def formatear_fecha(fecha: str) -> date:
    """
    Convierte YYYY-MM-DD a objeto date
    """
    try:
        año, mes, dia = fecha.split("-")
        return date(int(año), int(mes), int(dia))
    except:
        return None
    
    