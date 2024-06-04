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
    print("D. Aumentarle % el sueldo a los 'Femeninos' del JSON")
    print("E. Ordenar Listas: (CSV, JSON)")
    print("F. Criterios de filtrado: (CSV, JSON)")
    print("G. Guardar datos en nuevo archivo: (CSV, JSON)")


    seleccion =  input(f'\n\tIngrese opcion: ').upper()
    while seleccion not in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        print(f'ERROR: OPCION {seleccion} NO VALIDA')
        seleccion =  input(f'\n\tIngrese opcion: ').upper()
    return seleccion


while True:
    match menu_funciones():
        case 'A':
            lista_csv = leer_csv('personas.csv')
            print(f"LISTA .CSV GUARDADA!")
            cambios_lista_csv = []
            pausar_consola()
        case 'B':
            lista_json = leer_json('personas.json')
            print(f"LISTA .JSON GUARDADA!")
            cambios_lista_json = []
            pausar_consola()
        case 'C':
            print("Seleccionar:")
            print("1 mostrar datos de CSV")
            print("2 mostrar datos de JSON")
            print("3 VOLVER")
            seleccion = input(f'\n\tIngrese opcion: ').upper()

            if seleccion == '1':
                if len(lista_csv) == 0:
                    print("No hay datos CSV cargados.")
                else:
                    personas_cvs = mapear_lista(lambda persona: (persona['id'], persona['nombre'], persona["apellido"], persona["genero"], persona["edad"], persona["peso"]), lista_csv)
                    mostrar_lista_tupla(personas_cvs)
                
            elif seleccion == '2':
                if len(lista_json) == 0:
                    print("No hay datos JSON cargados.")
                else:
                    personas_json = mapear_lista(lambda persona: (persona["id"] , persona["nombre"], persona["ubicacion"], persona["genero"], persona["edad"], persona["sueldo"]), lista_json)
                    mostrar_lista_tupla(personas_json)
            
            elif seleccion == '3':
                continue
            pausar_consola()

        case 'D':
            if len(lista_json) == 0:
                print("No hay datos JSON cargados.")
            else:
                # sueldos_femeninos = filtrar_lista(lambda persona: persona['genero'] == 'Female', lista_json)
                seleccion = int(input("¿Cuanto % desea aumentar?: "))
                consultar_numero(seleccion, 1, 100, "Porcentaje no valido.")
                for persona in lista_json:
                    if persona['genero'] == 'Female':
                        persona['sueldo'] = persona['sueldo'] * (1 + (seleccion / 100))
                print("sueldos F aumentados")
                cambios_lista_json.append(f"{seleccion}% aumento")

            pausar_consola()
        case 'E':
            print("Seleccionar lista a ordenar: (1) CSV || (2) JSON || (3) VOLVER:")
            seleccion = input(f'\n\tIngrese opcion: ')

            while seleccion not in ['1', '2', '3']:
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
                            cambios_lista_csv.append(f"ordenada x {input_clave_ordenar}")
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
                            cambios_lista_json.append(f"ordenada x {input_clave_ordenar}")
                    # for persona in lista_json:
                    #     print(f"{persona["nombre"]} {persona["sueldo"]}")

                case '3':
                    continue

            pausar_consola()
        case 'F':
            # Filtrar por dos claves
            print("Seleccionar lista a filtrar: (1) CSV || (2) JSON || (3) VOLVER:")
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
                                lista_csv = filtrar_lista(lambda p: p["genero"] == "Female", lista_csv)
                                cambios_lista_csv.append(f"filtrada por Femenino")

                            else:
                                lista_csv = filtrar_lista(lambda p: p["genero"] == "Male", lista_csv)
                                cambios_lista_csv.append(f"filtrada por Masculino")

                        for persona in lista_csv:
                                    print(f"{persona['nombre']} {persona['peso']}")

                case '2':
                    if len(lista_json) == 0:
                        print("no hay datos JSON cargados")
                    else:
                        print("\t(Filtrar JSON)")
                        print("1) filtrar los 'ubicacion'" )
                        print("2) filtrar por edad menor a 40")
                        selecion_filtro = input(f"\tIngrese la opcion: ")
                        
                        while selecion_filtro not in ['1', '2', '3']:
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

                                lista_json = filtrar_lista(lambda persona: persona["ubicacion"] == seleccionar_ubicacion, lista_json)
                                cambios_lista_json.append(f"filtrado x {seleccionar_ubicacion}")
                            else:
                                lista_json = filtrar_lista(lambda persona: persona["edad"] < 40, lista_json)
                                cambios_lista_json.append(f"filtrado x edades")
                        
                        for persona in lista_json:
                            print(f"{persona['nombre']} {persona['ubicacion']}")
                case '3':
                    continue
                
        case 'G':
            seleccionar_archivo = input("Seleccionar archivo: (1) CSV || (2) JSON || (3) VOLVER: ")
            while seleccionar_archivo not in ['1', '2', '3']:
                print("ERROR: OPCION NO VALIDA")
                seleccionar_archivo = input("Seleccionar archivo: (1) CSV || (2) JSON: ")

            match seleccionar_archivo:
                case '1':
                    if len(lista_csv) == 0:
                        print("no hay datos CSV cargados")
                    else:
                        print("\t(Guardar CSV)")
                        nombre_archivo = input("Nombre del archivo: ")
                        escribir_csv(nombre_archivo, lista_csv)
                        cambios_lista_csv.append(f"guardada en {nombre_archivo}")

                case '2':
                    if len(lista_json) == 0:
                        print("no hay datos JSON cargados")
                    else:
                        print("\t(Guardar JSON)")
                        nombre_archivo = input("Nombre del archivo: ")
                        escribir_json(nombre_archivo, lista_json)
                        cambios_lista_json.append(f"guardada en {nombre_archivo}")

                case '3':
                    continue

            pausar_consola()