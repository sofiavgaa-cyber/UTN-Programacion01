# ----------------------------------------------------------
# 1. Crear un array con la cantidad de elementos recibida
# ----------------------------------------------------------

def crear_array(cantidad:int) -> list:
    """
    Crea una lista con la cantidad de elementos indicada.
    Inicializa todos los elementos en 0.

    Parámetro:
        cantidad (int): cantidad de elementos.

    Retorna:
        list: lista creada.
    """
    return [0] * cantidad


# ----------------------------------------------------------
# 2. Ingresar números en un array
# ----------------------------------------------------------

def cargar_numeros(cantidad:int) -> list:
    """
    Solicita al usuario ingresar una cantidad determinada
    de números y los almacena en una lista.

    Parámetro:
        cantidad (int): cantidad de números a ingresar.

    Retorna:
        list: lista con los números cargados.
    """
    lista = crear_array(cantidad)

    for i in range(cantidad):
        lista[i] = int(input(f"Ingrese número {i + 1}: "))

    return lista


# ----------------------------------------------------------
# 3. Promedio de todos los números
# ----------------------------------------------------------

def calcular_promedio(lista:list) -> float:
    """
    Calcula el promedio de todos los elementos.

    Parámetro:
        lista (list): lista de enteros.

    Retorna:
        float: promedio.
    """
    suma = 0

    for numero in lista:
        suma += numero

    return suma / len(lista)


# ----------------------------------------------------------
# 4. Promedio de números positivos
# ----------------------------------------------------------

def promedio_positivos(lista:list) -> float:
    """
    Calcula el promedio de los números positivos.

    Parámetro:
        lista (list): lista de enteros.

    Retorna:
        float: promedio de positivos.
    """
    suma = 0
    contador = 0

    for numero in lista:
        if numero > 0:
            suma += numero
            contador += 1

    if contador > 0:
        return suma / contador

    return 0


# ----------------------------------------------------------
# 5. Producto de todos los elementos
# ----------------------------------------------------------

def calcular_producto(lista:list) -> int:
    """
    Calcula el producto de todos los elementos.

    Parámetro:
        lista (list): lista de enteros.

    Retorna:
        int: producto.
    """
    producto = 1

    for numero in lista:
        producto *= numero

    return producto


# ----------------------------------------------------------
# 6. Posición del valor máximo
# ----------------------------------------------------------

def posicion_maximo(lista:list) -> int:
    """
    Retorna la posición del primer valor máximo.

    Parámetro:
        lista (list): lista de enteros.

    Retorna:
        int: índice del máximo.
    """
    indice_max = 0

    for i in range(1, len(lista)):
        if lista[i] > lista[indice_max]:
            indice_max = i

    return indice_max


# ----------------------------------------------------------
# 7. Mostrar posiciones del valor máximo
# ----------------------------------------------------------

def mostrar_posiciones_maximo(lista:list) -> None:
    """
    Muestra todas las posiciones donde se encuentra
    el valor máximo.

    Parámetro:
        lista (list): lista de enteros.
    """
    maximo = max(lista)

    print(f"Valor máximo: {maximo}")
    print("Posiciones:")

    for i in range(len(lista)):
        if lista[i] == maximo:
            print(i)


# ----------------------------------------------------------
# 8. Reemplazar nombres
# ----------------------------------------------------------

def reemplazar_nombres(lista_nombres:list,
                       nombre_antiguo:str,
                       nombre_nuevo:str) -> int:
    """
    Reemplaza todas las apariciones de un nombre.

    Parámetros:
        lista_nombres (list)
        nombre_antiguo (str)
        nombre_nuevo (str)

    Retorna:
        int: cantidad de reemplazos realizados.
    """
    contador = 0

    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            contador += 1

    return contador


# ----------------------------------------------------------
# 9. Intersección de dos arrays
# ----------------------------------------------------------

def interseccion_arrays(array1:list, array2:list) -> None:
    """
    Muestra los elementos que están en ambos arrays.
    """
    interseccion = []

    for elemento in array1:
        if elemento in array2 and elemento not in interseccion:
            interseccion.append(elemento)

    print("Intersección:", interseccion)


# ----------------------------------------------------------
# 10. Unión de dos arrays
# ----------------------------------------------------------

def union_arrays(array1:list, array2:list) -> None:
    """
    Muestra la unión de dos arrays.
    """
    union = array1.copy()

    for elemento in array2:
        if elemento not in union:
            union.append(elemento)

    print("Unión:", union)


# ----------------------------------------------------------
# 11. Diferencia de dos arrays
# ----------------------------------------------------------

def diferencia_arrays(array1:list, array2:list) -> None:
    """
    Muestra los elementos que están en array1
    pero no en array2.
    """
    diferencia = []

    for elemento in array1:
        if elemento not in array2:
            diferencia.append(elemento)

    print("Diferencia:", diferencia)


# ----------------------------------------------------------
# PROGRAMA PRINCIPAL (Ejemplo de uso)
# ----------------------------------------------------------

numeros = [10, 20, -5, 20, 30, 30]

print("Promedio:", calcular_promedio(numeros))
print("Promedio positivos:", promedio_positivos(numeros))
print("Producto:", calcular_producto(numeros))
print("Posición máximo:", posicion_maximo(numeros))

mostrar_posiciones_maximo(numeros)

nombres = ["Ana", "Juan", "Ana", "Pedro", "Ana"]

cantidad = reemplazar_nombres(
    nombres,
    "Ana",
    "María"
)

print("Lista modificada:", nombres)
print("Reemplazos realizados:", cantidad)

array_a = [1, 2, 3, 4, 5]
array_b = [4, 5, 6, 7, 8]

interseccion_arrays(array_a, array_b)
union_arrays(array_a, array_b)
diferencia_arrays(array_a, array_b)