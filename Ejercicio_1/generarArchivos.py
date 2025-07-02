import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Listas de ejemplo para generar datos aleatorios
actividades = [
    "Reunión de planificación", "Mantenimiento de equipos", "Capacitación interna",
    "Supervisión de proyectos", "Atención a clientes", "Elaboración de informes",
    "Revisión de documentos", "Actualización de base de datos", "Inventario de materiales",
    "Evaluación de desempeño"
]
responsables = ["Ana Pérez", "Carlos Ruiz", "Sofía Mendoza", "Jorge Salas", "Lucía Vargas"]
trabajadores = ["Luis Gómez", "María Torres", "Pedro Díaz", "Elena Ríos", "Juan Castro"]
departamentos = [
    "Recursos Humanos", "Sistemas", "Capacitación", "Ventas", "Logística",
    "Contabilidad", "Marketing", "Operaciones"
]
observaciones = [
    "Sin novedades", "Se definieron tareas", "Se realizó limpieza", "Tema: Seguridad informática",
    "Pendiente de aprobación", "Trabajo en equipo", "Requiere seguimiento", "Finalizado correctamente"
]

# Generar 40 registros
fecha_base = datetime(2025, 7, 1)
datos = []
for i in range(40):
    fecha = (fecha_base + timedelta(days=i // 5)).strftime("%Y-%m-%d")
    hora = f"{8 + (i % 10)}:{random.choice(['00', '15', '30', '45'])}"
    actividad = random.choice(actividades)
    responsable = random.choice(responsables)
    trabajador = random.choice(trabajadores)
    departamento = random.choice(departamentos)
    nro_oficina = random.randint(100, 399)
    observacion = random.choice(observaciones)
    datos.append({
        "fecha": fecha,
        "hora": hora,
        "actividad": actividad,
        "responsable": responsable,
        "trabajador": trabajador,
        "departamento": departamento,
        "nro_oficina": nro_oficina,
        "observaciones": observacion
    })

# Crear el DataFrame de la bitácora
bitacora_df = pd.DataFrame(datos)
print(bitacora_df)


carpeta_creados = os.path.join(os.path.dirname(__file__), "creados")
if not os.path.exists(carpeta_creados):
    os.makedirs(carpeta_creados)

# Guardar el DataFrame como CSV en la carpeta "leidos"
nombre_archivo = input("Ingresa nombre de archivo [bitacora_actividades]: ")
nombre_archivo = nombre_archivo if nombre_archivo != '' else "bitacora_actividades"


if os.path.exists(os.path.join(carpeta_creados, f"{nombre_archivo}.csv")):
    #os.makedirs(carpeta_creados)
    i = 1
    while os.path.exists(os.path.join(carpeta_creados, f"{nombre_archivo}_{i}.csv")):
        # nombre_archivo = nombre_archivo + f"_{i}"
        i += 1
    csv_path = os.path.join(carpeta_creados, f"{nombre_archivo}_{i}.csv")
else:
    csv_path = os.path.join(carpeta_creados, f"{nombre_archivo}.csv")
  
bitacora_df.to_csv(csv_path, index=False, encoding="utf-8")
print(f"Archivo CSV guardado en: {csv_path}")