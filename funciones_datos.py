# funcion para obtener el directorio actual
def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual,nombre_archivo)

# leer CSV:
def leer_csv(nombre_archivo):
    with open(get_path_actual(nombre_archivo),"r", encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip().split(",")

        for linea in archivo:
            persona = {}
            linea = linea.strip().split(",")

            id, nombre, apellido, genero, edad, peso = linea
            persona["id"] = int(id)
            persona["nombre"] = nombre
            persona["apellido"] = apellido
            persona["genero"] = genero
            persona["edad"] = int(edad)
            persona["peso"] = float(peso)

            lista.append(persona)
    return lista

# leer JSON:
def leer_json(nombre_archivo):
    import json
    with open(get_path_actual(nombre_archivo),"r", encoding="utf-8") as archivo:
        return json.load(archivo)