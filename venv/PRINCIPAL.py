from db import conectar

conexao = conectar()
cursor = conexao.cursor()

cursor.execute("SELECT COUNT(*) FROM usuarios")




cursor.close()
conexao.close()