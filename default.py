import pandas as pd
import datetime as dt
import random as rdm

#print(pd.__version__)

departamentos = [
    "Amazonas", "Áncash", "Apurímac", "Arequipa", "Ayacucho", "Cajamarca",
    "Callao", "Cusco", "Huancavelica", "Huánuco", "Ica", "Junín", "La Libertad",
    "Lambayeque", "Lima", "Loreto", "Madre de Dios", "Moquegua", "Pasco",
    "Piura", "Puno", "San Martín", "Tacna", "Tumbes", "Ucayali"
]
sucursal = []
for i in range(50):
    sucursal.append("sucursal_" + str(i))

# sucursal = [sucursal_1,...,sucursal_10]

laboratorio = [
    "Laboratorio A", "Laboratorio B", "Laboratorio C", "Laboratorio D",
    "Laboratorio E", "Laboratorio F", "Laboratorio G", "Laboratorio H",
    "Laboratorio I", "Laboratorio J"
]
