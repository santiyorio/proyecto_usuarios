import sqlite3

def crear_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insertar(nombre, edad):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)",
        (nombre, edad)
    )

    conn.commit()
    conn.close()


def mostrar():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    for fila in cursor.fetchall():
        print(fila)

    conn.close()