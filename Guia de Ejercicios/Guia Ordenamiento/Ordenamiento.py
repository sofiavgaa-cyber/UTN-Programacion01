#01
def ordenar_array(array, descendente=False):
    """
    Ordena un arreglo de números enteros usando el algoritmo de burbuja.

    Parámetros:
    array (list): lista de enteros
    descendente (bool): si es True ordena de mayor a menor, si no de menor a mayor

    Retorna:
    list: arreglo ordenado
    """

    n = len(array)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if descendente:
                condicion = array[j] < array[j + 1]
            else:
                condicion = array[j] > array[j + 1]

            if condicion:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


#02
def intercalar_vectores(v1, v2, descendente=False):
    """
    Intercala dos vectores ordenados en un único vector ordenado.

    Parámetros:
    v1, v2 (list): vectores ordenados ascendentemente
    descendente (bool): si True devuelve orden descendente

    Retorna:
    list: vector intercalado y ordenado
    """

    i = j = 0
    resultado = []

    while i < len(v1) and j < len(v2):

        if v1[i] <= v2[j]:
            resultado.append(v1[i])
            i += 1
        else:
            resultado.append(v2[j])
            j += 1

    # agregar lo que queda
    while i < len(v1):
        resultado.append(v1[i])
        i += 1

    while j < len(v2):
        resultado.append(v2[j])
        j += 1

    if descendente:
        resultado.reverse()

    return resultado


#03
def negativos_positivos(vector):
    """
    Muestra negativos en orden decreciente y positivos en orden creciente
    usando un solo vector y pocas estructuras repetitivas.
    """

    negativos = []
    positivos = []

    for num in vector:
        if num < 0:
            negativos.append(num)
        else:
            positivos.append(num)

    # ordenar con burbuja reutilizable (sin importar función externa)
    negativos = ordenar_array(negativos, descendente=True)
    positivos = ordenar_array(positivos, descendente=False)

    resultado = negativos + positivos

    print("Resultado:", resultado)
    return resultado