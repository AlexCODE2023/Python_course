import sqlite3

# ...existing code...

# Guardar en SQLite
conn = sqlite3.connect('datos.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS personas (
        nombre TEXT,
        apellido TEXT,
        edad INTEGER,
        telefono TEXT,
        email TEXT,
        sueldo REAL,
        casado BOOLEAN
    )
''')

# Diccionario para guardar una estructura de datos
dataStruct = {
    #Nombres y apellidos en una tabla 
    "nombre": [],
    "apellido": [],
    # Datos personales
    "edad": [],
    "telefono": [],
    "email": [],
    # Datos laborales
    "sueldo": [],
    "casado": [],
}


dataStruct["nombre"].append("Juan")

# Hacer prubas de codigo
print("hello world")
# Esto es un comentario
# Nuestro hola mundo en Python