import pandas as pd
import os
import shutil

def leerDatos(ruta_archivo,ruta_leidos):
    """
    Lee un archivo CSV y devuelve un DataFrame de pandas.
    
    :param ruta_archivo: Ruta del archivo CSV a leer.
    :return: DataFrame con los datos del archivo.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"El archivo {ruta_archivo} no existe.")
    
    df = pd.read_csv(ruta_archivo, encoding="utf-8")
    shutil.move(ruta_archivo, ruta_leidos)
    return df

carpeta_creados = os.path.join(os.path.dirname(__file__), "creados")
carpeta_leidos = os.path.join(os.path.dirname(__file__), "leidos")

if not os.path.exists(carpeta_leidos):
    os.makedirs(carpeta_leidos)

archivos = [f for f in os.listdir(carpeta_creados) if os.path.isfile(os.path.join(carpeta_creados, f))]

nombre_archivo = input("Ingresa el nombre del archivo a leer (sin extensión): ")

i = 0
for archivo in archivos:
    if archivo.startswith(nombre_archivo) and archivo.endswith(".csv"):
        ruta_archivo = os.path.join(carpeta_creados, archivo)
        df = leerDatos(ruta_archivo, carpeta_leidos)
        print(df)
        i += 1
if i == 0:
    print(f"No se encontraron archivos'{nombre_archivo}' en la carpeta 'creados'.")