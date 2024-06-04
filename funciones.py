from os import system

def limpiar_consola():
    system('cls')

def pausar_consola():
    system('pause')


def verificar_lista(lista:list) -> None:
    if type(lista) != list:
        raise TypeError("Error. No se puede procesar un objeto que no es lista")
    elif len(lista) == 0:
        raise ValueError("Error. Lista vacia")


def mapear_lista(procesadora, lista: list) -> list:
    """ Recorre una lista de diccionarios y devuelve una lista de tuplas con el resultado de la llamada a la función

    Args:
        procesadora (_type_): pasamos la funcion lambda.
        lista (list): pasamos la lista de diccionarios donde buscar.

    Returns:
        list: Nueva lista de tuplas.
    """
    lista_retorno = []
    for elemento in lista:
        try:
            lista_retorno.append(procesadora(elemento))
        except:
            TypeError("No se puede procesar un objeto que no es lista")
    return lista_retorno
#ej:  mapear_lista(lambda p: (p["id"], p["nombre"]), personas_prueba)

# usamos paradigma funcional: en "filtradora" le pasamos una funcion lambda que procese cada elemento de la lista.
def filtrar_lista(filtradora, lista:list) -> list:
    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada
#ej: filtrar_lista(lambda p: p["genero"] == "Femenino", personas_prueba)

def mostrar_lista_tupla(lista:list) -> None:
    """Imprime una lista de tuplas

    Args:
        lista (list): pasamos la lista de tuplas a imprimir
    """
    for tupla in lista:
        for elemento in tupla:
            print(f"{elemento}", end=" ")
        print()

def consultar_lista_esta_vacia(lista:list, mensaje) -> None:
    if len(lista) == 0:
        print(f"{mensaje}")

def consultar_numero(numero, minimo, maximo, mensaje) -> int:
    if numero < minimo or numero > maximo:
        print(f"{mensaje}")


def aumentar_por_porcentaje(porcentaje, clave, lista:list) -> list:
    for elemento in lista:
        elemento[clave] = elemento[clave] + (elemento[clave] * (porcentaje / 100))



def swap_lista(lista:list, i:int, j:int) -> None:
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


personas_prueba = [
    {"id": 1, "nombre": "Franklyn", "ubicacion": "Avellaneda", "genero": "Male", "edad": 44, "sueldo": 119800},
    {"id": 2, "nombre": "Carri", "ubicacion": "Quilmes", "genero": "Female", "edad": 20, "sueldo": 66900},
    {"id": 3, "nombre": "Ewart", "ubicacion": "San Fernando", "genero": "Male", "edad": 20, "sueldo": 76800},
    {"id": 4, "nombre": "Dugald", "ubicacion": "Lanus", "genero": "Male", "edad": 62, "sueldo": 117900}
]

# def ordenar_por_dos_condiciones(clave1, clave2, lista:list) -> None:
#     tam = len(lista)
#     for i in range(tam -1):
#         for j in range(i + 1, tam):
#             if lista[i][clave1] == lista[j][clave1]:
#                 if lista[i][clave2] > lista[j][clave2]:
#                     swap_lista(lista, i, j)
#             elif lista[i][clave1] > lista[j][clave1]:
#                 swap_lista(lista, i, j)

def ordenar_lista(comparator, lista:list) -> None:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if comparator(lista[i], lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
# uso: ordenar_lista(lambda p1, p2, : p1["sueldo"] < p2["sueldo"], nombre_lista)


# for persona in personas_prueba:
#     print(persona)

# print("-----------")
# clave = 'sueldo'


# ordenar_lista(lambda p1, p2: p1[clave] < p2[clave], personas_prueba)


# for persona in personas_prueba:
#     print(persona)


# obtengo todos los valores que existe de una misma clave en SIN que se repitan
def crear_lista_con_valores_de_clave(clave, lista):
    lista = mapear_lista(lambda p: p[clave], lista)

    nueva_lista = []
    for elemento in lista:
            if elemento not in nueva_lista:
                nueva_lista.append(elemento)
    return nueva_lista