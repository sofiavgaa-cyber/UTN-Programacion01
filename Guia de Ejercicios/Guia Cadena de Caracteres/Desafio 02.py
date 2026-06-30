# Sospechosos.py

sospechosos = [
    {"nombre": "Juan Perez", "adn": "AACGTTTAATG"},
    {"nombre": "Maria Lopez", "adn": "CGTTTAATG"},
    {"nombre": "Carlos Diaz", "adn": "TTGACCGTAA"},
    {"nombre": "Lucia Gomez", "adn": "CGTTTAATGA"}
]

from Sospechosos import sospechosos

ADN_CRIMEN = "CGTTTAATG"


def comparar_adn(adn1: str, adn2: str) -> bool:
    """
    Devuelve True si las secuencias de ADN son exactamente iguales.
    """
    if len(adn1) != len(adn2):
        return False

    for i in range(len(adn1)):
        if adn1[i] != adn2[i]:
            return False

    return True


def buscar_culpable(sospechosos, adn_crimen: str):
    """
    Busca el sospechoso cuyo ADN coincide con el de la escena del crimen.
    """
    for sospechoso in sospechosos:
        if comparar_adn(sospechoso["adn"], adn_crimen):
            return sospechoso["nombre"]

    return None


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

culpable = buscar_culpable(sospechosos, ADN_CRIMEN)

if culpable:
    print("🔴 CULPABLE ENCONTRADO:", culpable)
else:
    print("🟢 SON TODOS INOCENTES")