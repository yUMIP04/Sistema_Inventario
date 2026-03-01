import sqlite3
from flask import Flask,g


def create_DB():
    
    if 'db' not in g:
        g.db = sqlite3.connect('Inventario.db')
    return g.db   
        
def create_Table():
    
    conexion = create_DB()
    cursor = conexion.cursor()
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Usuario(
                       id_usuario INT PRIMARY KEY AUTOINCREMENT,
                       nombre_usuario VARCHAR(10),
                       contraseña VARCHAR(8)
                   )
                   ''')
    
    conexion.commit()
    conexion.close()