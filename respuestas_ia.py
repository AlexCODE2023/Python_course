import pandas as pd
import random

# Función para generar un IMC aleatorio
def generar_imc():
    return round(random.uniform(18.5, 35), 2)  # IMC saludable y sobrepeso

# Función para generar una nota aleatoria
def generar_nota():
    return random.randint(0, 20)

# 1. Dataset de Ejercicio e IMC
def generar_datos_ejercicio():
    data_ejercicio = []
    for _ in range(100):
        horas_ejercicio = round(random.uniform(0, 10), 1)  # Horas de ejercicio por semana
        imc = generar_imc()
        data_ejercicio.append([horas_ejercicio, imc])

    df_ejercicio = pd.DataFrame(data_ejercicio, columns=['HorasEjercicio', 'IMC'])
    df_ejercicio.to_csv('ejercicio_imc.csv', index=False)

    # 2. Dataset de Juego y Notas
    data_juego = []
    for _ in range(100):
        horas_juego = round(random.uniform(0, 20), 1)  # Horas de juego por semana
        nota = generar_nota()
        data_juego.append([horas_juego, nota])

    df_juego = pd.DataFrame(data_juego, columns=['HorasJuego', 'Nota'])
    df_juego.to_csv('juego_notas.csv', index=False)

    # 3. Dataset de Estudio y Notas
    data_estudio = []
    for _ in range(100):
        horas_estudio = round(random.uniform(0, 30), 1)  # Horas de estudio por semana
        nota = generar_nota()
        data_estudio.append([horas_estudio, nota])

    df_estudio = pd.DataFrame(data_estudio, columns=['HorasEstudio', 'Nota'])
    df_estudio.to_csv('estudio_notas.csv', index=False)

    print("Archivos CSV generados exitosamente.")

generar_datos_ejercicio()