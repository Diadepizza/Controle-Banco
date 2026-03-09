from db import conectar
import tkinter as tk

def porhora():
    print("Working")
def pordia():
    print("Working too!")

janela = tk.Tk()
janela.title("CONTROLE PRODUÇÃO")
janela.geometry("1115x900")
janela.configure(bg="#361C29")
conexao = conectar()
cursor = conexao.cursor()

botao1 = tk.Button(text="Produção por Hora",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28,command=porhora)
botao1.grid(row=5, column=0, padx=256, pady=(430,0))
botao2 = tk.Button(text="Produção por Dia",font=("Comic Sans MS", 24),bg="#170C22",fg="white",width=28,command=pordia)
botao2.grid(row=6, column=0, padx=256, pady=(10,0))



#cursor.execute("SELECT COUNT(*) FROM usuarios")



janela.mainloop()
#cursor.close()
#conexao.close()