from db import conectar
import tkinter as tk

janela = tk.Tk()
janela.title("CONTROLE PRODUÇÃO")
janela.geometry("1115x900")
janela.configure(bg="#361C29")
conexao = conectar()
cursor = conexao.cursor()

tk.Button(text="Produção por Hora",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28).grid(padx=256,pady=400)




#cursor.execute("SELECT COUNT(*) FROM usuarios")



janela.mainloop()
#cursor.close()
#conexao.close()