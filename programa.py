from funciones import *
from funciones_datos import *


# Nos va a dar un archivo json o csv y vamos a hacer un programa con un menu de opciones.
# ej:
# a- cargar datos desde .csv
# b- cargar datos desde .json
# c- mostrar datos (no poder seleccionar esta opcion si aún no cargue los datos):
#    - mostrar nombres de CSV
#    - mostrar genero y edad de JSON
# d- aumentarle 20% el sueldo a los empleados de 'Femeninos' y guardarlo en un archivo json o csv.
# e, f, etc... - (hacer algo con la lista de diccionario)
# g- guardar en csv o guardar en json.

lista_csv = []
lista_json = []

cambios_lista_csv = []
cambios_lista_json = []


def menu_funciones():
    limpiar_consola()
    print(f'\t---- MENU DE FUNCIONES ----')

    if len(lista_csv) == 0:
        print("Lista CSV: (sin datos cargados)")
    else:
        print(f"Lista CSV: Se cargaron {len(lista_csv)} || {cambios_lista_csv}")
    if len(lista_json) == 0:
        print("Lista JSON: (sin datos cargados)")
    else:
        print(f"Lista JSON: Se cargaron {len(lista_json)} || {cambios_lista_json}")
    print()

    print("A. Cargar datos desde .csv")
    print("B. Cargar datos desde .json")
    print("C. Mostrar datos")
    print("D. Aumentarle 20% el sueldo a los 'Femeninos' del JSON")
    print("E. Ordenar Listas: (CSV, JSON)")
    print("F. Criterios de filtrado: (CSV, JSON)")

    seleccion =  input(f'\n\tIngrese opcion: ').upper()
    while seleccion not in ['A', 'B', 'C', 'D', 'E', 'F']:
        print(f'ERROR: OPCION {seleccion} NO VALIDA')
        seleccion =  input(f'\n\tIngrese opcion: ').upper()
    return seleccion


while True:
    match menu_funciones():
        case 'A':
            lista_csv = leer_csv('personas.csv')
            print(f"LISTA .CSV GUARDADA!")
            pausar_consola()
        case 'B':
            lista_json = leer_json('personas.json')
            print(f"LISTA .JSON GUARDADA!")
            pausar_consola()
        case 'C':
            print("Seleccionar:")
            print("1 mostrar nombres de CSV")
            print("2 mostrar nombres de JSON")
            seleccion = input(f'\n\tIngrese opcion: ').upper()

            if seleccion == '1':
                consultar_lista_esta_vacia(lista_csv, "No hay datos CSV cargados.")
                csv_nombres = mapear_lista(lambda persona: (persona['id'], persona['nombre']), lista_csv)
                mostrar_lista_tupla(csv_nombres)

            elif seleccion == '2':
                consultar_lista_esta_vacia(lista_json, "No hay datos JSON cargados.")
                genero_edad = mapear_lista(lambda persona: (persona['genero'], persona['ubicacion']), lista_json)
                mostrar_lista_tupla(genero_edad)
            pausar_consola()
        case 'D':
            if len(lista_json) == 0:
                print("No hay datos JSON cargados.")
            else:
                sueldos_femeninos = filtrar_lista('genero', lista_json, 'Female')
                seleccion = int(input("¿Cuanto % desea aumentar?: "))
                consultar_numero(seleccion, 1, 100, "Porcentaje no valido.")
                aumentar_por_porcentaje(seleccion, 'sueldo', sueldos_femeninos)
                cambios_lista_json.append(f"{seleccion}% aumento")

            pausar_consola()
        case 'E':
            print("Seleccionar lista a ordenar: (1) CSV || (2) JSON:")
            seleccion = input(f'\n\tIngrese opcion: ')

            while seleccion not in ['1', '2']:
                print("ERROR: OPCION NO VALIDA")
                seleccion = input(f'\n\tIngrese opcion: ')
            

            match seleccion:
                case '1':
                    print("\t(Ordenar CSV)")
                    if len(lista_csv) == 0:
                        print("No hay datos CSV cargados.")
                    else:
                        input_ordenar_lista = input("Ordenamiento: (1) ascendente || (2) descendente: ")
                        while input_ordenar_lista not in ['1', '2']:
                            print("ERROR: OPCION NO VALIDA")
                            input_ordenar_lista = input("Ordenamiento: (1) ascendente || (2) descendente: ")
                        
                        input_clave_ordenar = input("Clave a ordenar ['id', 'nombre', 'apellido', 'genero', 'edad', 'peso']: ")
                        while input_clave_ordenar not in ['id', 'nombre', 'apellido', 'genero', 'edad', 'peso']:
                            print("ERROR: OPCION NO VALIDA")
                            input_clave_ordenar = input("Clave a ordenar ['id', 'nombre', 'apellido', 'genero', 'edad', 'peso']: ")
                        
                        else:
                            if input_ordenar_lista == '1':
                                ordenar_lista(lambda p1, p2: p1[input_clave_ordenar] < p2[input_clave_ordenar], lista_csv)
                            else:
                                ordenar_lista(lambda p1, p2: p1[input_clave_ordenar] > p2[input_clave_ordenar], lista_csv)
                            cambios_lista_csv.append(f"Lista ordenada")
                    # for persona in lista_csv:
                    #     print(f"{persona["nombre"]} {persona["peso"]}")
                   
                case '2':
                    print("\t(Ordenar JSON)")
                    if len(lista_json) == 0:
                        print("No hay datos JSON cargados.")
                    else:
                        input_ordenar_lista = input("Ordenamiento: (1) ascendente || (2) descendente: ")
                        while input_ordenar_lista not in ['1', '2']:
                            print("ERROR: OPCION NO VALIDA")
                            input_ordenar_lista = input("Ordenamiento: (1) ascendente || (2) descendente: ")
                        
                        input_clave_ordenar = input("Clave a ordenar ['id', 'nombre', 'ubicacion', 'genero', 'edad', 'sueldo']: ")
                        while input_clave_ordenar not in ['id', 'nombre', 'ubicacion', 'genero', 'edad', 'sueldo']:
                            print("ERROR: OPCION NO VALIDA")
                            input_clave_ordenar = input("Clave a ordenar ['id', 'nombre', 'ubicacion', 'genero', 'edad', 'sueldo']: ")
                        
                        else:
                            if input_ordenar_lista == '1':
                                ordenar_lista(lambda p1, p2: p1[input_clave_ordenar] < p2[input_clave_ordenar], lista_json)
                            else:
                                ordenar_lista(lambda p1, p2: p1[input_clave_ordenar] > p2[input_clave_ordenar], lista_json)
                            cambios_lista_json.append(f"Lista ordenada")
            pausar_consola()
        case 'F':
            # Filtrar por dos claves
            print("Seleccionar lista a filtrar: (1) CSV || (2) JSON:")
            seleccion = input(f'\n\tIngrese opcion: ')

            while seleccion not in ['1', '2']:
                print("ERROR: OPCION NO VALIDA")
                seleccion = input(f'\n\tIngrese opcion: ')


            match seleccion:
                case '1':
                    if len(lista_csv) == 0:
                        print("no hay datos CSV cargados")

                    else:
                        print("\t(Filtrar CSV)")
                        print("1) filtrar por genero Femino")
                        print("2) filtrar por genero Masculino")
                        selecion_filtro = input(f"\tIngrese la opcion: ")
                        
                        while selecion_filtro not in ['1', '2']:
                            print("ERROR: OPCION NO VALIDA")
                            selecion_filtro = input(f"\tIngrese la opcion: ")

                        else:
                            if selecion_filtro == '1':
                                lista_csv_filtrada = filtrar_lista(lambda p: p["genero"] == "Female", lista_csv)

                            else:
                                lista_csv_filtrada = filtrar_lista(lambda p: p["genero"] == "Male", lista_csv)

                        for persona in lista_csv_filtrada:
                                    print(f"{persona['nombre']} {persona['peso']}")

                        cambios_lista_csv.append(f"Lista filtrada")

                case '2':
                    if len(lista_json) == 0:
                        print("no hay datos JSON cargados")
                    else:
                        print("\t(Filtrar JSON)")
                        print("1) filtrar los 'ubicacion'" )
                        print("2) filtrar por edad menor a 40")
                        selecion_filtro = input(f"\tIngrese la opcion: ")
                        
                        while selecion_filtro not in ['1', '2']:
                            print("ERROR: OPCION NO VALIDA")
                            selecion_filtro = input(f"\tIngrese la opcion: ")

                        else:
                            if selecion_filtro == '1':
                                ubicaciones_disponibles = crear_lista_con_valores_de_clave("ubicacion", lista_json)
                                print(f"\tUbicaciones disponibles: {ubicaciones_disponibles}")
                                seleccionar_ubicacion = input("\tUbicacion: ")

                                while seleccionar_ubicacion not in ubicaciones_disponibles:
                                    print("ERROR: OPCION NO VALIDA")
                                    seleccionar_ubicacion = input("\tUbicacion: ")

                                lista_filtrada = filtrar_lista(lambda persona: persona["ubicacion"] == seleccionar_ubicacion, lista_json)
                        
                        for persona in lista_filtrada:
                            print(f"{persona['nombre']} {persona['ubicacion']}")

                        cambios_lista_json.append(f"Lista filtrada")

            pausar_consola()