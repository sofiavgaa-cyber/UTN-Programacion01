from typing import Callable, List, Tuple, Dict

# ==============================
# 1. Evaluaciones individuales
# ==============================

def evaluar_por_presupuesto(proyecto: Dict, limite: int) -> bool:
    """
    Aprueba si el presupuesto del proyecto es menor o igual al límite.
    """
    return proyecto["presupuesto"] <= limite


def evaluar_por_impacto(proyecto: Dict, minimo: int) -> bool:
    """
    Aprueba si el impacto del proyecto es mayor o igual al mínimo.
    """
    return proyecto["impacto"] >= minimo


def evaluar_por_duracion(proyecto: Dict, maximo: int) -> bool:
    """
    Aprueba si la duración del proyecto es menor o igual al máximo permitido.
    """
    return proyecto["duracion"] <= maximo


# ==============================
# 2. Evaluación con criterio dinámico
# ==============================

def evaluar_proyecto(
    proyecto: Dict,
    criterio: Callable[[Dict, int], bool],
    parametro: int
) -> bool:
    """
    Evalúa un proyecto usando una función de criterio dinámica.
    """
    return criterio(proyecto, parametro)


# ==============================
# 3. Evaluación con múltiples criterios
# ==============================

def evaluar_varios_criterios(
    proyecto: Dict,
    criterios: List[Tuple[Callable[[Dict, int], bool], int]]
) -> bool:
    """
    Aprueba el proyecto solo si cumple todos los criterios.
    """
    return all(criterio(proyecto, parametro) for criterio, parametro in criterios)


# ==============================
# 4. Ejemplo de uso
# ==============================

if __name__ == "__main__":

    proyecto_ejemplo = {
        "presupuesto": 50000,
        "impacto": 8,
        "duracion": 12
    }

    # Evaluaciones individuales
    print(evaluar_por_presupuesto(proyecto_ejemplo, 60000))  # True
    print(evaluar_por_impacto(proyecto_ejemplo, 7))          # True
    print(evaluar_por_duracion(proyecto_ejemplo, 10))        # False

    # Evaluación dinámica
    print(evaluar_proyecto(proyecto_ejemplo, evaluar_por_impacto, 7))  # True

    # Evaluación múltiple
    criterios = [
        (evaluar_por_presupuesto, 60000),
        (evaluar_por_impacto, 7),
        (evaluar_por_duracion, 15)
    ]

    print(evaluar_varios_criterios(proyecto_ejemplo, criterios))  # True