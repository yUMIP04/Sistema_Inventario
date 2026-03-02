import sqlite3
from flask import Flask,g

#🌟CREACION DE LA DB
def create_DB():
    return  sqlite3.connect('Inventario.db')
     

#🌟CREACION DE LA TABLA DE USUARIOS
def create_Table():
    
    conexion = create_DB()
    cursor = conexion.cursor()
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Usuario(
                       id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre_usuario VARCHAR(10) UNIQUE,
                       contraseña VARCHAR(8) UNIQUE
                   )
                   ''')
    
    conexion.commit()
    conexion.close()
    
#🌟INSERTAR UN NUEVO USUARIO

def insert_user(nombre_usuario, contraseña):
    
    conexion = create_DB()
    cursor = conexion.cursor()
    
    
    cursor.execute('''
                   INSERT INTO Usuario(nombre_usuario, contraseña) VALUES (?,?) 
                   ''', (nombre_usuario, contraseña))
    
    conexion.commit()
    conexion.close()