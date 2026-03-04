import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="usuario",
        password="senha",
        database="meubanco"
    )